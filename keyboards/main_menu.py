from aiogram import types

def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🔮 Вытянуть карту", "🎓 Записаться на сессию")
    return keyboard
