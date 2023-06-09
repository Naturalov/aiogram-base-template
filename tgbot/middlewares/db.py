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
        user, created = await UserModel.get_or_create(tg_id=event.from_user.id)

        data["user"] = user

        await handler(event, data)


dp.message.outer_middleware(DB())
dp.callback_query.outer_middleware(DB())
