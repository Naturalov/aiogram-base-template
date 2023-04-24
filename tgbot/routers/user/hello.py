from tgbot.filters import FText
from aiogram.types import Message
from fluentogram import TranslatorRunner

from models import UserModel
from . import router


#Example @router.message(FText("start-hello"))
@router.message()
async def fun(message: Message, user: UserModel, i18n: TranslatorRunner):
    await message.answer(i18n.get("start-hello", username=message.from_user.username))
