"""
Authentication API Endpoints
"""
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.modules.auth.schemas import (
    UserRegister, UserLogin, TokenResponse, TokenRefreshRequest,
    MFASetupResponse, MFAVerifyRequest, UserProfileResponse
)
from app.modules.auth.services import AuthService
from app.middleware.auth_deps import get_current_user, CurrentUser

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserProfileResponse, status_code=status.HTTP_201_CREATED)
async def register(data: UserRegister, db: AsyncSession = Depends(get_db)):
    """Register a new user account."""
    user = await AuthService.register(db, data)
    return user


@router.post("/login", response_model=TokenResponse)
@router.post("/token", response_model=TokenResponse)
async def login(
    data: UserLogin,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    """Authenticate user with email and password (and MFA if enabled)."""
    ip = request.client.host if request.client else None
    ua = request.headers.get("User-Agent")
    return await AuthService.authenticate(db, data, ip_address=ip, user_agent=ua)


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    data: TokenRefreshRequest,
    db: AsyncSession = Depends(get_db)
):
    """Rotate and refresh access token with a valid refresh token."""
    return await AuthService.refresh_access_token(db, data.refresh_token)


@router.get("/me", response_model=UserProfileResponse)
async def get_current_user_profile(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)
):
    """Get profile of currently logged-in user."""
    user = await AuthService.get_by_id(db, current_user.id)
    user_dict = {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "full_name": user.full_name,
        "role": user.role,
        "tenant_id": user.tenant_id,
        "is_active": user.is_active,
        "is_verified": user.is_verified,
        "is_mfa_enabled": user.is_mfa_enabled,
        "last_login_at": user.last_login_at,
        "permissions": current_user.permissions,
        "created_at": user.created_at,
    }
    return user_dict


@router.post("/mfa/setup", response_model=MFASetupResponse)
async def setup_mfa(
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)
):
    """Initialize MFA setup for user and receive TOTP QR code."""
    return await AuthService.setup_mfa(db, current_user.id)


@router.post("/mfa/verify")
async def verify_mfa(
    data: MFAVerifyRequest,
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)
):
    """Verify submitted 6-digit code and activate MFA on account."""
    success = await AuthService.verify_and_enable_mfa(db, current_user.id, data.code)
    return {"success": success, "message": "MFA has been successfully verified and enabled."}
