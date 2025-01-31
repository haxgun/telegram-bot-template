from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()

@router.message(Command("start"))
async def _(message: Message,
            i18n: TranslatorRunner):
    await message.answer(i18n.welcome_text())