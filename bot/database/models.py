from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.database import Base


class User(Base):
    __tablename__ = "users"

    """
    SQLAlchemy model representing a user in the database.

    Attributes:
        telegram_id (int): The unique Telegram ID of the user.
        username (str | None): The username of the user (optional).
        first_name (str): The first name of the user.
        last_name (str | None): The last name of the user (optional).
        language_code (str | None): The language code of the user (optional).
        is_premium (bool | None): Whether the user has a premium Telegram account (optional).
    """
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)  # Unique Telegram ID
    username: Mapped[str | None]  # Optional Telegram username
    first_name: Mapped[str]  # First name of the user
    last_name: Mapped[str | None]  # Optional last name
    language_code: Mapped[str | None] = None  # Optional language code
    is_premium: Mapped[bool | None] = None  # Optional premium status


    def __repr__(self) -> str:
        """
        Generate a string representation of the User instance.

        Returns:
            str: A formatted string containing the user's ID, Telegram ID, and username.
        """
        return f"<User(id={self.id}, telegram_id={self.telegram_id}, username={self.username!r})>"
