from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from models import UserModel
from . import router


@router.message(CommandStart())
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    print(message)
    await message.reply("Вітаю!")
