from main import dp
from tgbot.routers import start, hello

dp.include_router(start.router)
dp.include_router(hello.router)
