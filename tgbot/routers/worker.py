from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner
from database.models import user
from database.models.user import PermissionEnum
from database.services.user_service import UserService
from tgbot.filters.check_premission import PermissionFilter

# Инициализация роутера
router = Router(name="test")


@router.message(CommandStart(), PermissionFilter(PermissionEnum.worker))
async def fun(message: Message,
              user_service: UserService,
              i18n: TranslatorRunner):
    await message.reply("Вітаю!")
