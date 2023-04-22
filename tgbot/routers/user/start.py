from . import router
from aiogram.filters import CommandStart
from aiogram.types import Message

@router.message(CommandStart())
async def fun(message: Message):
    print(message)
    await message.reply("Вітаю!")
