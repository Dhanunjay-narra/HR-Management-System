"""
Database Engine & Async Session Management
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncEngine
)
from app.core.config import settings

# Configure SQLite or PostgreSQL async engine
connect_args = {}
if "sqlite" in settings.async_database_url:
    connect_args = {"check_same_thread": False}

engine: AsyncEngine = create_async_engine(
    settings.async_database_url,
    echo=settings.DB_ECHO_LOG,
    connect_args=connect_args,
    future=True,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency yielding an async database session wrapped in a transaction context.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
