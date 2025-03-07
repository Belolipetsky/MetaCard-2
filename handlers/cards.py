# handlers/cards.py
from aiogram import types, Dispatcher
from utils.texts import CARD_INSTRUCTION, WRONG_CARD_NUMBER

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_draw_card, lambda message: message.text == "🔮 Вытянуть карту", state="*")
    dp.register_message_handler(process_card_number, lambda message: message.text.isdigit(), state="*")

async def cmd_draw_card(message: types.Message):
    # Инструкция для выбора карты
    await message.answer(CARD_INSTRUCTION)
    # В реальной реализации можно перевести пользователя в состояние ожидания ввода номера карты

async def process_card_number(message: types.Message):
    card_number = message.text.strip()
    if not card_number.isdigit():
        await message.answer(WRONG_CARD_NUMBER)
        return
    # Здесь можно получить описание карты из списка или БД
    card_description = f"🔮 Описание карты {card_number}: Здесь будет текст описания выбранной карты."
    await message.answer(card_description)
