from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command

from app.handlers import help, message, callback, start, commands


def register_handlers(dp: Dispatcher):
    # commands
    dp.message(CommandStart())(start.start_command)
    dp.message(Command('admin'))(commands.admin_command)
    # messages

    # callbacks
    dp.callback_query(lambda c: c.data == "admin_users")(callback.admin_all_user_count)

    
