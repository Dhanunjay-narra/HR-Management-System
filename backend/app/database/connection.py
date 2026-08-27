"""
Database Connection & Initialization Lifecycle with Seed Data
"""
from sqlalchemy import select
from app.database.session import engine, AsyncSessionLocal
from app.database.base import Base
from app.core.logging import logger
from app.core.security import get_password_hash
from app.modules.tenants.models import Tenant
from app.modules.auth.models import User


async def init_db() -> None:
    """Initialize database tables and seed default superuser."""
    logger.info("Initializing database schema...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database schema initialized successfully.")

    # Seed default tenant and superuser if not present
    async with AsyncSessionLocal() as db:
        try:
            # Check default tenant
            res_t = await db.execute(select(Tenant).where(Tenant.id == "default"))
            tenant = res_t.scalar_one_or_none()
            if not tenant:
                tenant = Tenant(
                    id="default",
                    name="Global Enterprise",
                    slug="global-enterprise",
                    domain="peoplepulse.io",
                    is_active=True
                )
                db.add(tenant)
                await db.flush()

            # Check admin user
            res_u = await db.execute(select(User).where(User.email == "admin@peoplepulse.io"))
            admin = res_u.scalar_one_or_none()
            if not admin:
                admin = User(
                    email="admin@peoplepulse.io",
                    hashed_password=get_password_hash("Admin@123456"),
                    first_name="System",
                    last_name="Administrator",
                    role="super_admin",
                    tenant_id="default",
                    is_active=True,
                    is_verified=True
                )
                db.add(admin)
                await db.flush()
                logger.info("Default superuser admin@peoplepulse.io seeded successfully.")

            await db.commit()
        except Exception as e:
            logger.error(f"Error during default data seeding: {e}")
            await db.rollback()


async def close_db() -> None:
    """Close database engine pool connections on shutdown."""
    logger.info("Closing database connections...")
    await engine.dispose()
    logger.info("Database connections closed.")
