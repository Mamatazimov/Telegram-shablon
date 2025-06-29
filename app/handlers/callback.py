from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.utils.users import *


async def admin_all_user_count(call:CallbackQuery):
    users = await get_all_users()
    
    await call.message.answer(f"{len(users)} ta user bor!")

