from aiogram import types

def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🔮 Вытянуть карту")
    keyboard.add("🎓 Записаться на сессию")
    return keyboard
