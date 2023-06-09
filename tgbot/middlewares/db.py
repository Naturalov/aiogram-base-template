from database.dependency.services import user_service
from database.services.user_service import UserService
from main import dp

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from database.models import user


class DB(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        await user_service.update_username(tg_id=event.from_user.id,
                                           username=event.from_user.username)
        data["user_service"] = user_service

        await handler(event, data)
