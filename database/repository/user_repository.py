from tortoise.expressions import Q

from database import models


class UserRepository:

    def __init__(self) -> None:
        ...

    @staticmethod
    async def get(tg_id: int | None = None) -> models.User | None:
        if not tg_id:
            raise ValueError("provide one parameter for search")

        user = await models.User.get_or_none(Q(tg_id=tg_id if tg_id else None))
        # |Q(referral_id=referral_id if referral_id else None) |
        # Q(email=email if email else None)

        return user
