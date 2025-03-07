from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils import texts, database
from keyboards import main_menu

class Form(StatesGroup):
    waiting_for_contact = State()
    waiting_for_name = State()

async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="📱 Отправить номер", request_contact=True)
    keyboard.add(button)
    await message.answer(texts.WELCOME_TEXT, reply_markup=keyboard)
    await Form.waiting_for_contact.set()

async def process_contact(message: types.Message, state: FSMContext):
    if message.contact is None:
        await message.answer("Пожалуйста, используй кнопку для отправки номера.")
        return
    # Сохраняем номер телефона в состоянии
    await state.update_data(phone=message.contact.phone_number)
    await message.answer(texts.ASK_NAME_TEXT, reply_markup=types.ReplyKeyboardRemove())
    await Form.waiting_for_name.set()

async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    user_data = await state.get_data()
    phone = user_data.get("phone", "N/A")
    # Сохраняем пользователя (в будущем в Google Sheets)
    database.save_user(message.from_user.id, message.from_user.username, name, phone)
    text = texts.MAIN_MENU_TEXT.format(name=name)
    await message.answer(text, reply_markup=main_menu.get_main_menu_keyboard())
    await state.finish()

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start", state="*")
    dp.register_message_handler(process_contact, content_types=types.ContentType.CONTACT, state=Form.waiting_for_contact)
    dp.register_message_handler(process_name, state=Form.waiting_for_name)
