# handlers/start.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils.texts import START_MESSAGE, ASK_NAME_MESSAGE
from keyboards.main_menu import main_menu

# Состояния для авторизации
class StartStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_name = State()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(process_contact, content_types=types.ContentType.CONTACT, state=StartStates.waiting_for_phone)
    dp.register_message_handler(process_name, state=StartStates.waiting_for_name)

async def cmd_start(message: types.Message):
    # Отправляем приветственное сообщение с кнопкой для отправки номера
    phone_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    phone_button = types.KeyboardButton("📱 Отправить номер", request_contact=True)
    phone_keyboard.add(phone_button)
    await message.answer(START_MESSAGE, reply_markup=phone_keyboard)
    await StartStates.waiting_for_phone.set()

async def process_contact(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
        await state.update_data(phone=phone)
        await message.answer(ASK_NAME_MESSAGE)
        await StartStates.waiting_for_name.set()
    else:
        await message.answer("Пожалуйста, отправьте номер телефона через кнопку ниже.")

async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    data = await state.get_data()
    phone = data.get("phone")
    # Здесь можно сохранить данные пользователя в БД (например, через utils/database.py)
    await message.answer(f"Спасибо, {name}! Теперь всё готово!", reply_markup=main_menu())
    await state.finish()
