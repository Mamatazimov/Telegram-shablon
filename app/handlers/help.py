from aiogram import types

async def help_command(message: types.Message):
    await message.answer("Yordam kamandasini chaqirdingiz")