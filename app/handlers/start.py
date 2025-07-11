from aiogram.types import Message
from aiogram import types

from app.utils.users import *


async def start_command(message:Message):
    checker = await check_user_exists(telegram_id=message.from_user.id)
    if checker:
        await message.answer("Welcome back!")
    else:
        await create_user(username=message.from_user.username, telegram_id=message.from_user.id,
                    first_name=message.from_user.first_name, last_name=message.from_user.last_name,
                    is_bot=False,is_pro=False
                    )
        await message.answer("Welcome to our bot!\nThis bot help to convert your file to another format!")
