import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import betterlogging as bl

from tortoise import Tortoise

from aiogram.fsm.strategy import FSMStrategy
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from commands import set_bot_commands
from config_reader import config

# Создаем экземпляр бота.
storage = MemoryStorage()
bot = Bot(token=config.bot_token, parse_mode="HTML")
dp = Dispatcher(storage=storage)

# Создаем экземпляр таймера по Московскому времени.
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

# Загружаем логгер.
logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)


async def main():
    logging.basicConfig(
        level=log_level,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    # Регистрация /-команд в интерфейсе.
    await set_bot_commands(bot)
    from tgbot import dp

    logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
    logging.getLogger('aiogram.event').setLevel(logging.DEBUG)

    await Tortoise.init({
        'connections': {
            'default': config.database_dsn
        },
        "apps": {
            "models": {
                "models": ["models"],
                "default_connection": "default",
            },
        },
    })
    await Tortoise.generate_schemas()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
