from aiogram import Router
from main import dp

router = Router(name="user")

from .start import router
from .hello import router

dp.include_router(router)
