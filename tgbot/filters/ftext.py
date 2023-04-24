from aiogram.filters import BaseFilter
from aiogram.types import Message
from fluentogram import TranslatorRunner


class FText(BaseFilter):
    __slots__ = "text"

    def __init__(self, text: str, **kwargs):
        self.text = text
        self.kwargs = kwargs

    async def __call__(self, message: Message, i18n: TranslatorRunner) -> bool:
        return message.text == i18n.get(self.text, **self.kwargs)
