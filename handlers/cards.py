from aiogram import types, Dispatcher
from utils.texts import CARD_INSTRUCTION_TEXT

# Пример описаний карт
CARD_DESCRIPTIONS = {
    "1": "🔮 Описание карты 1: Твои скрытые возможности скоро проявятся.",
    "2": "🔮 Описание карты 2: Время для перемен настало.",
    "3": "🔮 Описание карты 3: Новые перспективы уже рядом."
}

async def draw_card_command(message: types.Message):
    # Здесь можно добавить проверку баланса попыток из базы
    await message.answer(CARD_INSTRUCTION_TEXT)

async def card_number_handler(message: types.Message):
    card_number = message.text.strip()
    if card_number in CARD_DESCRIPTIONS:
        await message.answer(CARD_DESCRIPTIONS[card_number])
    else:
        await message.answer(
            "❌ Такого номера нет, выбери карту в канале и попробуй снова.\n"
            "Повтори попытку, перейдя в канал: https://t.me/+Io5-yW5dgyEyNjhi"
        )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(draw_card_command, text="🔮 Вытянуть карту", state="*")
    dp.register_message_handler(card_number_handler, lambda message: message.text.isdigit(), state="*")
