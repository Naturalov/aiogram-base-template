from database import models, schemas
from database.repository.user_repository import UserRepository


class UserNotFound(Exception):
    ...


class UserExists(Exception):
    def __init__(self, user: schemas.User) -> None:
        self.user = user


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
    ) -> None:
        self._user_repository = user_repository

    @staticmethod
    async def construct_schema_by_model(
            user: models.User) -> schemas.User:
        return schemas.User(tg_id=user.tg_id,
                            username=user.username,
                            permission=user.permission)

    async def get(self,
                  tg_id: int | None = None):
        user = await self._user_repository.get(tg_id=tg_id)
        if not user:
            raise UserNotFound()

        return await self.construct_schema_by_model(user=user)

    async def get_or_create(self,
                            tg_id: int | None = None):
        user = await self._user_repository.get_or_create(tg_id=tg_id)

        return await self.construct_schema_by_model(user=user)

    async def update_username(self,
                              tg_id: int,
                              username: str):
        user = await self._user_repository.update_username(tg_id=tg_id,
                                                           username=username)

        return await self.construct_schema_by_model(user=user)
