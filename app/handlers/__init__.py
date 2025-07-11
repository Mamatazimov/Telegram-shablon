from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram import F

from app.handlers import help, message, callback, start, commands


def register_handlers(dp: Dispatcher):
    # commands
    dp.message(CommandStart())(start.start_command)
    dp.message(Command('admin'))(commands.admin_command)
    # messages

    # message files
    dp.message(F.document)(message.document_converter)

    # callbacks
    dp.callback_query(lambda c: c.data == "admin_users")(callback.admin_all_user_count)
    # callback files
    dp.callback_query(lambda s: s.data.startswith("docs"))(callback.docs_con)

    
