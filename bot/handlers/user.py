from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()

@router.message(CommandStart())
async def _(message: Message, i18n: TranslatorRunner) -> None:
    welcome_text = i18n.welcome_text()
    repository_link = i18n.repository_link()
    click_on_link = i18n.click_on_link()

    text = f"{welcome_text}\n{repository_link}\n{click_on_link}"
    await message.reply(text)