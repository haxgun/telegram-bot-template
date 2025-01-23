from datetime import datetime
from bot.config import database_url
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession

# Create an asynchronous database engine using the provided database URL
engine = create_async_engine(url=database_url)

# Create an asynchronous session factory for database interactions
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

class Base(AsyncAttrs, DeclarativeBase):
    """
    Base class for SQLAlchemy models.

    Attributes:
        id (int): Primary key of the table, auto-incremented.
        created_at (datetime): Timestamp of when the record was created, set by default.
        updated_at (datetime): Timestamp of when the record was last updated, automatically updated.
    """
    __abstract__ = True  # Indicates that this class is meant to be inherited, not instantiated directly.

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now()
    )  # Automatically sets the creation timestamp when a record is added.

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )  # Automatically updates the timestamp when a record is modified.

    @classmethod
    @property
    def __tablename__(cls) -> str:
        """
        Generates the table name for the model by converting the class name to lowercase and appending an 's'.

        Returns:
            str: The table name.
        """
        return cls.__name__.lower() + 's'
