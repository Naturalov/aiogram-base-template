from tortoise.models import Model
from tortoise import fields
from tortoise.manager import Manager


class UserModel(Model):
    tg_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255, default="none")

    language = fields.CharField(max_length=4, default="en")
