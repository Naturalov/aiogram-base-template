from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner
from database.models import user
from database.models.user import PermissionEnum
from tgbot.filters.check_premission import PermissionFilter

# Инициализация роутера
router = Router(name="test")


@router.message(CommandStart(), PermissionFilter(PermissionEnum.user))
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    await message.reply("Вітаю!")
    print(message.from_user)
