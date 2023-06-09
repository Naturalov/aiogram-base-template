from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

from database.models import user

# Инициализация роутера
router = Router(name="user")


@router.message()
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    await message.answer(i18n.get("start-hello", username=message.from_user.username))
