from main import dp
from .db import DB
from .i18n import I18nMiddleware, t_hub

dp.message.outer_middleware(DB())
dp.callback_query.outer_middleware(DB())

dp.message.outer_middleware(I18nMiddleware(t_hub))
dp.callback_query.outer_middleware(I18nMiddleware(t_hub))
