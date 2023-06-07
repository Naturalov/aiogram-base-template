from main import dp

from typing import Callable, Dict, Any, Awaitable, Optional

from aiogram import BaseMiddleware, types
from aiogram.types import Message, User

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from pathlib import Path

from models import UserModel

# Получение пути до каталога locales относительно текущего файла
locales_dir = Path(__file__).parent.joinpath("..//..//locales")
print(locales_dir)

# Подгружаем наши переводы из файлов.
t_hub = TranslatorHub(
    {"ua": ("ua", "ru", "en"),
     "ru": ("ru", "en"),
     "en": ("en",)},
    translators=[
        FluentTranslator(locale="en",
                         translator=FluentBundle.from_files("en-US", filenames=[f'{str(locales_dir)}/en'
                                                                                f'/strings.ftl'],
                                                            use_isolating=False)),
        FluentTranslator(locale="ru",
                         translator=FluentBundle.from_files("ru-RU", filenames=[f'{str(locales_dir)}/ru'
                                                                                f'/strings.ftl'],
                                                            use_isolating=False))],
    root_locale="en",
)


class I18nMiddleware(BaseMiddleware):
    def __init__(self, t_hub: TranslatorHub):
        self.t_hub = t_hub

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data["i18n"] = self.t_hub.get_translator_by_locale(data["user"].language)
        data["t_hub"] = self.t_hub
        await handler(event, data)


dp.message.outer_middleware(I18nMiddleware(t_hub))
dp.callback_query.outer_middleware(I18nMiddleware(t_hub))
