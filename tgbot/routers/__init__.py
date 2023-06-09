from main import dp
from tgbot.routers import worker, user

dp.include_router(start.router)
dp.include_router(hello.router)
