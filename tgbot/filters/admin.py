from main import dp

from aiogram.filters import BaseFilter
from aiogram.types import Message

from models import UserModel


class AdminFilter(BaseFilter):
    is_admin: bool = False

    async def __call__(self, obj: Message) -> bool:
        user = await UserModel.get_or_create(obj.from_user.id)
        user = user[0]

        return user.admin

