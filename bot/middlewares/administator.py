from typing import Any, Awaitable, Callable, Dict
from typing import Union

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

from bot.config import admins


async def is_admin(user_id: str) -> bool:
    try:
        if user_id in admins:
            return True
        return False
    except TelegramBadRequest:
        return False


class AdministatorMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Union[None, Callable[[Message, Dict[str, Any]], Awaitable[Any]]]:
        telegram_id = str(event.from_user.id)
        if not await is_admin(telegram_id):
            return
        return await handler(event, data)