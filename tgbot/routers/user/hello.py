from . import router
from aiogram.filters import CommandStart
from aiogram.types import Message

@router.message()
async def fun(message: Message):
    await message.reply("Аллах с нами!")
