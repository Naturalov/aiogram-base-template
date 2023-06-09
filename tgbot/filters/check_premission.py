from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.models import user
from database.models.user import PermissionEnum
from database.services.user_service import UserService


class PermissionFilter(BaseFilter):
    is_permission: bool = False

    def __init__(self, permission: PermissionEnum):
        self._permission = permission

    async def __call__(self,
                       obj: Message,
                       user_service: UserService) -> bool:
        user = await user_service.get_or_create(obj.from_user.id)

        return user.permission & self._permission
