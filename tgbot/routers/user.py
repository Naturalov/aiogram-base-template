from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

from database.services.user_service import UserService

# Инициализация роутера
router = Router(name="user")


@router.message()
async def fun(message: Message,
              i18n: TranslatorRunner,
              user_service: UserService):
    await message.answer(i18n.get("start-hello", username=message.from_user.username))
