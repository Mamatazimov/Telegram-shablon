from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    is_bot = fields.BooleanField(default=False)

    def __str__(self):
        return f"User(id={self.id}, user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name}, username={self.username})"