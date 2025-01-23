from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.database import Base


class User(Base):
    __tablename__ = "users"

    """
    SQLAlchemy model representing a user.

    Attributes:
        telegram_id (int): The unique Telegram ID of the user.
        username (str | None): The username of the user (optional).
        first_name (str | None): The first name of the user (optional).
        last_name (str | None): The last name of the user (optional).
    """
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)  # Unique Telegram ID for the user
    username: Mapped[str | None]  # Optional username of the user
    first_name: Mapped[str | None]  # Optional first name of the user
    last_name: Mapped[str | None]  # Optional last name of the user

    def __repr__(self) -> str:
        """
        Generate a string representation of the User instance.

        Returns:
            str: A string containing the user's ID, Telegram ID, and username.
        """
        return f"<User(id={self.id}, telegram_id={self.telegram_id}, username='{self.username}')>"
