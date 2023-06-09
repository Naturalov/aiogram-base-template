from main import dp

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from fluentogram import TranslatorHub

from ..utils import create_translator_hub_from_directory

# Подгружаем наши переводы из файлов.
t_hub = create_translator_hub_from_directory('locales', 'ru')


class I18nMiddleware(BaseMiddleware):
    def __init__(self, t_hub: TranslatorHub):
        self.t_hub = t_hub

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data["i18n"] = self.t_hub.get_translator_by_locale(event.from_user.language_code)
        data["t_hub"] = self.t_hub
        await handler(event, data)
