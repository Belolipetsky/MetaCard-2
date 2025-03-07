from aiogram import types

def get_payment_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Купить 1 карту – 89₽")
    keyboard.add("Купить 5 карт – 356₽ (Экономия 20%)")
    keyboard.add("Купить 10 карт – 699₽ (Самая выгодная цена!)")
    return keyboard
