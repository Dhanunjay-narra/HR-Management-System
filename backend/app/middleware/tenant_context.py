"""
Tenant Context Middleware & ContextVars
"""
from contextvars import ContextVar
from typing import Optional
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import uuid

# Context Variables for async execution flow
current_tenant_id: ContextVar[Optional[str]] = ContextVar("current_tenant_id", default=None)
current_user_id: ContextVar[Optional[str]] = ContextVar("current_user_id", default=None)
current_request_id: ContextVar[str] = ContextVar("current_request_id", default="")


class TenantContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware that captures request IDs and Tenant-ID headers for request isolation.
    """
    async def dispatch(self, request: Request, call_next) -> Response:
        req_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        current_request_id.set(req_id)

        # Check for tenant header (if explicitly passed)
        tenant_hdr = request.headers.get("X-Tenant-ID")
        if tenant_hdr:
            current_tenant_id.set(tenant_hdr)

        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        return response
