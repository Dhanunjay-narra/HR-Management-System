"""
HR Management System - Enterprise FastAPI Application Entrypoint
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import logger
from app.core.exceptions import HRManagementSystemException
from app.database.connection import init_db, close_db
from app.middleware.tenant_context import TenantContextMiddleware

# Import module routes
from app.modules.auth.routes import router as auth_router
from app.modules.tenants.routes import router as tenants_router
from app.modules.audit.routes import router as audit_router
from app.modules.notifications.routes import router as notifications_router
from app.modules.organization.routes import router as organization_router
from app.modules.employees.routes import router as employees_router
from app.modules.employee_360.routes import router as employee_360_router
from app.modules.attendance.routes import router as attendance_router
from app.modules.leave.routes import router as leave_router
from app.modules.recruitment.routes import router as recruitment_router
from app.modules.onboarding.routes import router as onboarding_router
from app.modules.goals.routes import router as goals_router
from app.modules.skills.routes import router as skills_router
from app.modules.learning.routes import router as learning_router
from app.modules.service_desk.routes import router as service_desk_router
from app.modules.engagement.routes import router as engagement_router
from app.modules.communication.routes import router as communication_router
from app.modules.workflows.routes import router as workflows_router
from app.modules.approvals.routes import router as approvals_router
from app.modules.payroll.routes import router as payroll_router
from app.modules.expenses.routes import router as expenses_router
from app.modules.assets.routes import router as assets_router
from app.modules.documents.routes import router as documents_router
from app.modules.analytics.routes import router as analytics_router
from app.modules.ai_assistant.routes import router as ai_assistant_router
from app.modules.ai_documents.routes import router as ai_documents_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application Startup and Shutdown Lifecycles."""
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.PROJECT_VERSION} in {settings.ENVIRONMENT} mode...")
    await init_db()
    yield
    logger.info("Shutting down application...")
    await close_db()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Enterprise HR Management & Employee Relationship Intelligence Platform",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# Custom Exception Handler
@app.exception_handler(HRManagementSystemException)
async def custom_exception_handler(request: Request, exc: HRManagementSystemException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )

# Middlewares
app.add_middleware(TenantContextMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base healthcheck endpoint
@app.get("/health", tags=["Health"])
@app.get(f"{settings.API_V1_STR}/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "environment": settings.ENVIRONMENT,
    }

# Register API Routers
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(tenants_router, prefix=settings.API_V1_STR)
app.include_router(audit_router, prefix=settings.API_V1_STR)
app.include_router(notifications_router, prefix=settings.API_V1_STR)
app.include_router(organization_router, prefix=settings.API_V1_STR)
app.include_router(employees_router, prefix=settings.API_V1_STR)
app.include_router(employee_360_router, prefix=settings.API_V1_STR)
app.include_router(attendance_router, prefix=settings.API_V1_STR)
app.include_router(leave_router, prefix=settings.API_V1_STR)
app.include_router(recruitment_router, prefix=settings.API_V1_STR)
app.include_router(onboarding_router, prefix=settings.API_V1_STR)
app.include_router(goals_router, prefix=settings.API_V1_STR)
app.include_router(skills_router, prefix=settings.API_V1_STR)
app.include_router(learning_router, prefix=settings.API_V1_STR)
app.include_router(service_desk_router, prefix=settings.API_V1_STR)
app.include_router(engagement_router, prefix=settings.API_V1_STR)
app.include_router(communication_router, prefix=settings.API_V1_STR)
app.include_router(workflows_router, prefix=settings.API_V1_STR)
app.include_router(approvals_router, prefix=settings.API_V1_STR)
app.include_router(payroll_router, prefix=settings.API_V1_STR)
app.include_router(expenses_router, prefix=settings.API_V1_STR)
app.include_router(assets_router, prefix=settings.API_V1_STR)
app.include_router(documents_router, prefix=settings.API_V1_STR)
app.include_router(analytics_router, prefix=settings.API_V1_STR)
app.include_router(ai_assistant_router, prefix=settings.API_V1_STR)
app.include_router(ai_documents_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
