"""
Authentication Service
"""
from datetime import datetime, timezone, timedelta
from typing import Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.modules.auth.models import User, UserSession, LoginHistory
from app.modules.auth.schemas import (
    UserRegister, UserLogin, TokenResponse, MFASetupResponse
)
from app.core.security import (
    verify_password, get_password_hash, create_access_token,
    create_refresh_token, decode_token, generate_mfa_secret,
    get_mfa_provisioning_uri, generate_mfa_qr_base64, verify_mfa_totp
)
from app.core.permissions import get_permissions_for_role
from app.core.exceptions import (
    AuthenticationException, DuplicateResourceException, ResourceNotFoundException, ValidationException
)
from app.core.config import settings
from app.events.event_bus import event_bus, DomainEvent


class AuthService:
    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> Optional[User]:
        result = await db.execute(select(User).where(User.email == email.lower(), User.is_deleted == False))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: str) -> User:
        result = await db.execute(select(User).where(User.id == user_id, User.is_deleted == False))
        user = result.scalar_one_or_none()
        if not user:
            raise ResourceNotFoundException("User", user_id)
        return user

    @staticmethod
    async def register(db: AsyncSession, data: UserRegister) -> User:
        existing = await AuthService.get_by_email(db, data.email)
        if existing:
            raise DuplicateResourceException("User", "email", data.email)

        user = User(
            email=data.email.lower(),
            hashed_password=get_password_hash(data.password),
            first_name=data.first_name,
            last_name=data.last_name,
            tenant_id=data.tenant_id,
            role=data.role or "employee",
            is_active=True,
            is_verified=True,
        )
        db.add(user)
        await db.flush()

        # Publish domain event
        await event_bus.publish(DomainEvent(
            event_type="auth.user.registered",
            tenant_id=user.tenant_id,
            actor_id=user.id,
            payload={"user_id": user.id, "email": user.email, "role": user.role}
        ))
        return user

    @staticmethod
    async def authenticate(
        db: AsyncSession,
        data: UserLogin,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> TokenResponse:
        user = await AuthService.get_by_email(db, data.email)
        if not user:
            raise AuthenticationException("Invalid email or password")

        now = datetime.now(timezone.utc)
        if user.locked_until and user.locked_until > now:
            raise AuthenticationException("Account is temporarily locked due to excessive failed attempts. Try again later.")

        if not user.is_active:
            raise AuthenticationException("User account is inactive. Please contact your administrator.")

        # Verify password
        if not verify_password(data.password, user.hashed_password):
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 5:
                user.locked_until = now + timedelta(minutes=15)
            
            # Log failed attempt
            db.add(LoginHistory(
                user_id=user.id,
                status="FAILED",
                ip_address=ip_address,
                user_agent=user_agent,
                failure_reason="Invalid password"
            ))
            await db.flush()
            raise AuthenticationException("Invalid email or password")

        # MFA check if enabled
        if user.is_mfa_enabled:
            if not data.mfa_code:
                return TokenResponse(
                    access_token="",
                    refresh_token="",
                    expires_in=0,
                    user_id=user.id,
                    email=user.email,
                    role=user.role,
                    tenant_id=user.tenant_id,
                    mfa_required=True
                )
            if not verify_mfa_totp(user.mfa_secret or "", data.mfa_code):
                db.add(LoginHistory(
                    user_id=user.id,
                    status="FAILED",
                    ip_address=ip_address,
                    user_agent=user_agent,
                    failure_reason="Invalid MFA token"
                ))
                await db.flush()
                raise AuthenticationException("Invalid 6-digit MFA verification code")

        # Success - reset lock & failed counter
        user.failed_login_attempts = 0
        user.locked_until = None
        user.last_login_at = now
        user.last_login_ip = ip_address

        # Generate tokens
        role_perms = list(get_permissions_for_role(user.role))
        custom_perms = user.custom_permissions or []
        all_perms = list(set(role_perms + custom_perms))

        access_token = create_access_token(
            subject=user.id,
            tenant_id=user.tenant_id,
            role=user.role,
            permissions=all_perms,
        )
        refresh_token = create_refresh_token(
            subject=user.id,
            tenant_id=user.tenant_id,
        )

        # Store session
        db.add(UserSession(
            user_id=user.id,
            refresh_token=refresh_token,
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        ))
        db.add(LoginHistory(
            user_id=user.id,
            status="SUCCESS",
            ip_address=ip_address,
            user_agent=user_agent
        ))
        await db.flush()

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user_id=user.id,
            email=user.email,
            role=user.role,
            tenant_id=user.tenant_id,
            mfa_required=False
        )

    @staticmethod
    async def refresh_access_token(db: AsyncSession, refresh_token_str: str) -> TokenResponse:
        payload = decode_token(refresh_token_str)
        if not payload or payload.get("type") != "refresh":
            raise AuthenticationException("Invalid or expired refresh token")

        user_id = payload.get("sub")
        result = await db.execute(
            select(UserSession).where(
                UserSession.refresh_token == refresh_token_str,
                UserSession.is_revoked == False
            )
        )
        session = result.scalar_one_or_none()
        if not session:
            raise AuthenticationException("Session revoked or expired")

        user = await AuthService.get_by_id(db, user_id)
        if not user.is_active:
            raise AuthenticationException("User is inactive")

        role_perms = list(get_permissions_for_role(user.role))
        custom_perms = user.custom_permissions or []
        all_perms = list(set(role_perms + custom_perms))

        # Rotate tokens
        new_access_token = create_access_token(
            subject=user.id,
            tenant_id=user.tenant_id,
            role=user.role,
            permissions=all_perms,
        )
        new_refresh_token = create_refresh_token(
            subject=user.id,
            tenant_id=user.tenant_id,
        )

        session.refresh_token = new_refresh_token
        session.expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        await db.flush()

        return TokenResponse(
            access_token=new_access_token,
            refresh_token=new_refresh_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user_id=user.id,
            email=user.email,
            role=user.role,
            tenant_id=user.tenant_id,
            mfa_required=False
        )

    @staticmethod
    async def setup_mfa(db: AsyncSession, user_id: str) -> MFASetupResponse:
        user = await AuthService.get_by_id(db, user_id)
        secret = generate_mfa_secret()
        user.mfa_secret = secret
        await db.flush()

        uri = get_mfa_provisioning_uri(secret, user.email)
        qr_b64 = generate_mfa_qr_base64(uri)

        return MFASetupResponse(
            secret=secret,
            provisioning_uri=uri,
            qr_code_base64=qr_b64
        )

    @staticmethod
    async def verify_and_enable_mfa(db: AsyncSession, user_id: str, code: str) -> bool:
        user = await AuthService.get_by_id(db, user_id)
        if not user.mfa_secret:
            raise ValidationException("MFA setup has not been initialized")
        
        if not verify_mfa_totp(user.mfa_secret, code):
            raise ValidationException("Invalid MFA code")

        user.is_mfa_enabled = True
        await db.flush()
        return True
