"""
Database Connection & Initialization Lifecycle
"""
from app.database.session import engine
from app.database.base import Base
from app.core.logging import logger


async def init_db() -> None:
    """Initialize database tables."""
    logger.info("Initializing database schema...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database schema initialized successfully.")


async def close_db() -> None:
    """Close database engine pool connections on shutdown."""
    logger.info("Closing database connections...")
    await engine.dispose()
    logger.info("Database connections closed.")
