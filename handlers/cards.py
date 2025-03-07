from aiogram import types, Dispatcher
from utils import texts

def register_cards_handlers(dp: Dispatcher):

    @dp.message_handler(lambda message: message.text == "🔮 Вытянуть карту")
    async def send_card_instruction(message: types.Message):
        await message.answer(texts.CARD_INSTRUCTION_TEXT)

    @dp.message_handler(lambda message: message.text.strip().isdigit())
    async def process_card_number(message: types.Message):
        card_number = message.text.strip()
        if card_number in texts.CARD_DESCRIPTIONS:
            description = texts.CARD_DESCRIPTIONS[card_number]
            await message.answer(description)
        else:
            await message.answer(texts.INVALID_CARD_TEXT)
            await message.answer(texts.CARD_INSTRUCTION_TEXT)

def register_handlers(dp):
    register_cards_handlers(dp)
