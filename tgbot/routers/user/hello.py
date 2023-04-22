from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from models import UserModel
from . import router


@router.message()
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    await message.answer(i18n.start.hello(username=message.from_user.username))
