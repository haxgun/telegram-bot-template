from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    """
    Class for managing application settings.

    Attributes:
        BOT_TOKEN (str): Token for the Telegram bot.
        ADMIN_IDS (list[int]): List of administrator Telegram IDs.
        FORMAT_LOG (str): Format string for logging messages.
        LOG_ROTATION (str): File size or duration before log rotation.
        DB_URL (str): Database connection URL.

    The settings are loaded from an environment file (default is `.env`).
    """
    BOT_TOKEN: str
    ADMIN_IDS: list[int]
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    DB_URL: str = "sqlite+aiosqlite:///data/database.db"

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


def configure_logging(log_file: Path, log_format: str, log_rotation: str) -> None:
    """
    Configures the logging system.

    Args:
        log_file (str): Path to the log file.
        log_format (str): Format of log messages.
        log_rotation (str): Rotation strategy for log files (e.g., file size or time interval).
    """
    logger.add(log_file, format=log_format, level="INFO", rotation=log_rotation)


# Load application settings from environment variables or `.env` file
settings = Settings()

# Configure logging based on the loaded settings
log_file_path = BASE_DIR / "log.txt"
configure_logging(log_file_path, settings.FORMAT_LOG, settings.LOG_ROTATION)

t_hub = TranslatorHub(
    locales_map = {
        "ru": ("ru", "en"),
        "en": ("en", "ru"),
    },
    translators=[
        FluentTranslator(
            "ru",
            translator=FluentBundle.from_files(
                "ru-RU",
                filenames=[
                    f"{BASE_DIR}/bot/i18n/ru/text.ftl",
                    f"{BASE_DIR}/bot/i18n/ru/button.ftl",
                ]
            ),
        ),
        FluentTranslator(
            "en",
            translator=FluentBundle.from_files(
                "en-US",
                filenames=[
                    f"{BASE_DIR}/bot/i18n/en/text.ftl",
                    f"{BASE_DIR}/bot/i18n/en/button.ftl",
                ]
            ),
        )
    ],
    root_locale="ru",
)

# Create a bot instance with the specified token and default properties
bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# Create a dispatcher instance with an in-memory storage for FSM
dp = Dispatcher(
    t_hub=t_hub,
    storage=MemoryStorage()
)

# List of administrator IDs
admins = settings.ADMIN_IDS

# Database connection URL
database_url = settings.DB_URL
