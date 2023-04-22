from tortoise.models import Model
from tortoise import fields
from tortoise.manager import Manager


class User(Model):
    tg_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255, default="none")
