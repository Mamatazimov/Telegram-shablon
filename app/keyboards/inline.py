from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_kb():
    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text="Userlar soni",callback_data="admin_users"))
    ikb = ikb.as_markup()
    return ikb

def choose_kb(typ,ff,files,fn):
    ikb = InlineKeyboardBuilder()
    for file in files:
        ikb.row(InlineKeyboardButton(text=f"{ff} to {file}",callback_data=f"{typ}_{ff}_{file}_{fn}"))
    ikb = ikb.as_markup()
    return ikb
