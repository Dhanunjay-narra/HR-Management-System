"""
Application-wide Enterprise Exceptions
"""
from typing import Any, Optional, Dict
from fastapi import HTTPException, status


class PeoplePulseException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        code: str = "GENERIC_ERROR",
        extra: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "error": True,
                "code": code,
                "message": detail,
                "extra": extra or {}
            }
        )


class AuthenticationException(PeoplePulseException):
    def __init__(self, detail: str = "Invalid credentials or authentication token"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            code="AUTHENTICATION_FAILED"
        )


class PermissionDeniedException(PeoplePulseException):
    def __init__(self, required_permission: Optional[str] = None):
        detail = f"Permission denied. Required: {required_permission}" if required_permission else "Access forbidden"
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            code="PERMISSION_DENIED",
            extra={"required_permission": required_permission} if required_permission else None
        )


class ResourceNotFoundException(PeoplePulseException):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} with identifier '{identifier}' not found",
            code="RESOURCE_NOT_FOUND",
            extra={"resource": resource, "identifier": str(identifier)}
        )


class DuplicateResourceException(PeoplePulseException):
    def __init__(self, resource: str, field: str, value: Any):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{resource} with {field} '{value}' already exists",
            code="DUPLICATE_RESOURCE",
            extra={"resource": resource, "field": field, "value": str(value)}
        )


class TenantIsolationException(PeoplePulseException):
    def __init__(self, detail: str = "Cross-tenant access violation"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            code="TENANT_ISOLATION_VIOLATION"
        )


class ValidationException(PeoplePulseException):
    def __init__(self, detail: str, extra: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
            code="VALIDATION_FAILED",
            extra=extra
        )
