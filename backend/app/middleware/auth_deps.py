"""
Authentication & Authorization FastAPI Dependencies
"""
from typing import List, Optional, Callable
from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.core.security import decode_token
from app.core.permissions import has_permission, get_permissions_for_role
from app.core.exceptions import AuthenticationException, PermissionDeniedException
from app.middleware.tenant_context import current_tenant_id, current_user_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)


class CurrentUser:
    """Authenticated user context object."""
    def __init__(
        self,
        id: str,
        email: str,
        tenant_id: Optional[str],
        role: str,
        permissions: List[str],
        is_active: bool = True,
        is_superuser: bool = False,
    ):
        self.id = id
        self.email = email
        self.tenant_id = tenant_id
        self.role = role
        self.permissions = permissions
        self.is_active = is_active
        self.is_superuser = is_superuser


async def get_current_user_token_payload(
    token: Optional[str] = Depends(oauth2_scheme),
    authorization: Optional[str] = Header(None)
) -> dict:
    """Extract and decode JWT token from Authorization header."""
    auth_token = token
    if not auth_token and authorization and authorization.startswith("Bearer "):
        auth_token = authorization.split(" ")[1]

    if not auth_token:
        raise AuthenticationException("Not authenticated")

    payload = decode_token(auth_token)
    if not payload or payload.get("type") != "access":
        raise AuthenticationException("Invalid or expired token")

    return payload


async def get_current_user(
    payload: dict = Depends(get_current_user_token_payload),
    db: AsyncSession = Depends(get_db)
) -> CurrentUser:
    """Extract and return CurrentUser with resolved role permissions."""
    user_id = payload.get("sub")
    tenant_id = payload.get("tenant_id")
    role = payload.get("role", "employee")
    
    # Resolve all permissions for role
    role_perms = list(get_permissions_for_role(role))
    custom_perms = payload.get("permissions", [])
    all_perms = list(set(role_perms + custom_perms))

    # Set context variables
    current_user_id.set(user_id)
    if tenant_id:
        current_tenant_id.set(tenant_id)

    return CurrentUser(
        id=user_id,
        email=payload.get("email", ""),
        tenant_id=tenant_id,
        role=role,
        permissions=all_perms,
        is_superuser=(role == "platform_owner"),
    )


def require_permission(required_permission: str) -> Callable:
    """
    Decorator dependency checking if the current user possesses the required RBAC permission.
    Example: Depends(require_permission("employee.create"))
    """
    async def permission_checker(current_user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if current_user.is_superuser:
            return current_user
        if not has_permission(current_user.permissions, required_permission):
            raise PermissionDeniedException(required_permission)
        return current_user

    return permission_checker
