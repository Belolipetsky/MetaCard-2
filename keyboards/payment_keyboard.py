# keyboards/payment_keyboard.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def payment_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Купить 1 карту – 89₽", callback_data="buy_1"))
    keyboard.add(InlineKeyboardButton("Купить 5 карт – 356₽", callback_data="buy_5"))
    keyboard.add(InlineKeyboardButton("Купить 10 карт – 699₽", callback_data="buy_10"))
    return keyboard
