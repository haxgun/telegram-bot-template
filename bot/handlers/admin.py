from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import admins

router = Router()
router.message.filter(F.from_user.id.in_(admins))

@router.message(Command("admin"))
async def _(message: Message):
    await message.answer("Admin panel")