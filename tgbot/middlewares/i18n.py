from main import dp

from typing import Callable, Dict, Any, Awaitable, Optional

from aiogram import BaseMiddleware, types
from aiogram.types import Message, User

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from pathlib import Path

from models import UserModel

# Получение пути до каталога locales относительно текущего файла
locales_dir = Path(__file__).parent.joinpath("..\\..\\locales")

# Подгружаем наши переводы из файлов.
t_hub = TranslatorHub(
    {"ua": ("ua", "ru", "en"),
     "ru": ("ru", "en"),
     "en": ("en",)},
    translators=[
        FluentTranslator(locale="en",
                         translator=FluentBundle.from_files("en-US", filenames=[f'{str(locales_dir)}\\en'
                                                                                f'\\strings.ftl'],
                                                            use_isolating=False)),
        FluentTranslator(locale="ru",
                         translator=FluentBundle.from_files("ru-RU", filenames=[f'{str(locales_dir)}/ru'
                                                                                f'/strings.ftl'],
                                                            use_isolating=False))],
    root_locale="en",
)


class L10nMiddleware(BaseMiddleware):
    def __init__(self, t_hub: TranslatorHub):
        self.t_hub = t_hub

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user, created = await UserModel.get_or_create(tg_id=event.from_user.id)

        data["i18n"] = self.t_hub.get_translator_by_locale(user.language)
        data["t_hub"] = self.t_hub
        await handler(event, data)


dp.message.middleware(L10nMiddleware(t_hub))
dp.callback_query.middleware(L10nMiddleware(t_hub))
