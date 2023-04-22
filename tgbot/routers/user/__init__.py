from aiogram import Router
from main import dp

#Инициализация роутера
router = Router(name="user")

#Импорт хендлеров
from .start import router
from .hello import router

dp.include_router(router)
