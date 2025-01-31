import logging
from typing import Any, Awaitable, Callable, Dict

from fluentogram import TranslatorHub
from aiogram import BaseMiddleware
from aiogram.types import Update
from cachetools import TTLCache

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Caches to store throttling data (user requests) with a short TTL
caches = {
    "default": TTLCache(maxsize=10_000, ttl=0.1)
}


class TranslateMiddleware(BaseMiddleware):
    """
    Middleware for handling translations using Fluentogram.

    This middleware retrieves the user's preferred language and provides a translator
    instance to be used within handlers.
    """

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        # Determine user language, defaulting to 'ru' if not found
        language = data['user'].language_code if 'user' in data else 'ru'

        # Retrieve TranslatorHub instance from context
        hub: TranslatorHub = data.get('t_hub')

        # Store translator instance in request data
        data['i18n'] = hub.get_translator_by_locale(language)

        return await handler(event, data)


class ThrottlingMiddleware(BaseMiddleware):
    """
    Middleware for rate-limiting user requests to prevent spam.

    This middleware uses a TTLCache to ensure that users do not send multiple requests
    within a very short period of time.
    """

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any],
    ) -> Any:
        # Ensure event has a valid user before proceeding
        if not hasattr(event, "from_user") or event.from_user is None:
            return await handler(event, data)

        # If user is found in cache, they have sent a request recently, so ignore
        if event.from_user.id in caches["default"]:
            return

        # Add user to cache to prevent further requests within TTL period
        caches["default"][event.from_user.id] = None
        return await handler(event, data)

# class DataBaseMiddleware(BaseMiddleware):
#     """
#     Middleware for handling database sessions.
#
#     This middleware provides an async database session within the request context,
#     ensuring proper resource management.
#     """
#     def __init__(self, db: async_sessionmaker):
#         super().__init__()
#         self.db = db
#
#     async def __call__(
#             self,
#             handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
#             event: Update,
#             data: Dict[str, Any],
#     ) -> Any:
#         async with self.db() as session:
#             data["db"] = session
#             return await handler(event, data)
