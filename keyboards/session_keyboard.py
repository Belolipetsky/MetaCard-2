from aiogram import types

def get_session_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("🎓 Записаться на личную сессию")
    keyboard.add("🔄 Подумать позже")
    return keyboard
