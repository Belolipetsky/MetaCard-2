# keyboards/session_keyboard.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def session_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🎓 Записаться на личную сессию", callback_data="session_signup"))
    keyboard.add(InlineKeyboardButton("🔄 Подумать позже", callback_data="session_later"))
    return keyboard
