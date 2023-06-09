from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.models import user
from database.models.user import PermissionEnum


class PermissionFilter(BaseFilter):
    is_permission: bool = False

    def __init__(self, permission: PermissionEnum):
        self._permission = permission

    async def __call__(self, obj: Message) -> bool:
        user = await UserModel.get_or_create(obj.from_user.id)
        user = user[0]

        return user.permission & self._permission
