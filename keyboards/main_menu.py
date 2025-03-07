# keyboards/main_menu.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_card = KeyboardButton("🔮 Вытянуть карту")
    button_session = KeyboardButton("🎓 Записаться на сессию")
    keyboard.add(button_card, button_session)
    return keyboard
