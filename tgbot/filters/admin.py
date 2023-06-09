from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.models import user
from database.services.user_service import UserService


class AdminFilter(BaseFilter):
    is_admin: bool = False

    async def __call__(self, obj: Message) -> bool:
        user = await UserService.get(tg_id=obj.from_user.id)

        return user.admin
