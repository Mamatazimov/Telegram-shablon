from app.database.models import User


async def create_user(username: str, telegram_id: int, first_name: str, last_name: str, is_bot: bool):
    user = await User.create(username=username, user_id=telegram_id, first_name=first_name, last_name=last_name, is_bot=is_bot)
    return user

async def get_user_by_telegram_id(telegram_id: int):
    user = await User.get(user_id=telegram_id)
    return user

async def get_all_users():
    users = await User.all()
    return users

async def check_user_exists(telegram_id: int)->bool:
    user = await User.get_or_none(user_id=telegram_id)
    return True if user is not None else False

