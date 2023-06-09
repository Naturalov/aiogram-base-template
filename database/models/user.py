from enum import IntFlag, auto

from tortoise.models import Model
from tortoise import fields
from tortoise.manager import Manager


class PermissionEnum(IntFlag):
    user = auto()
    worker = auto()
    moder = auto()
    admin = auto()


class User(Model):
    tg_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255, default="none")

    permission = fields.IntEnumField(PermissionEnum, default=PermissionEnum.user)
