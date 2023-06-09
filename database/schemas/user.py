from database.schemas.base import SchemaBase


class User(SchemaBase):
    tg_id: int
    username: str
