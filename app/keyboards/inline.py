from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_kb():
    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text="Userlar soni",callback_data="admin_users"))
    ikb = ikb.as_markup()
    return ikb

