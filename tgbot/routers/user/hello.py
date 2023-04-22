from fluentogram import TranslatorRunner

from . import router
from aiogram.filters import CommandStart
from aiogram.types import Message


@router.message()
async def fun(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.start.hello(username=message.from_user.username))
