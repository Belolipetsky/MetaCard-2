from aiogram import types, Dispatcher
from utils.texts import WELCOME_MESSAGE, MAIN_MENU_TEXT
from utils.database import add_user
from datetime import datetime
from utils.config import ADMIN_ID
from keyboards.main_menu import get_main_menu_keyboard

async def start_command(message: types.Message):
    # Клавиатура для запроса номера телефона
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton("📱 Отправить номер", request_contact=True)
    markup.add(button_phone)
    await message.answer(WELCOME_MESSAGE, reply_markup=markup)

async def contact_handler(message: types.Message):
    if message.contact:
        phone = message.contact.phone_number
        await message.answer("✨ Отлично! Теперь скажи, как тебя зовут?", reply_markup=types.ReplyKeyboardRemove())
        # Сохранение номера можно реализовать через FSM или напрямую в базе
    else:
        await message.answer("Пожалуйста, отправь свой номер, используя кнопку ниже.")

async def name_handler(message: types.Message):
    name = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username or ""
    phone = "unknown"  # Здесь необходимо получить сохранённый ранее номер телефона
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_user(user_id, username, name, phone, registration_date)
    # Отправка главного меню
    await message.answer(MAIN_MENU_TEXT.format(name=name), reply_markup=get_main_menu_keyboard())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start", state="*")
    dp.register_message_handler(contact_handler, content_types=types.ContentType.CONTACT, state="*")
    # Обработка ввода имени (при условии, что это не команда и не другое сообщение)
    dp.register_message_handler(name_handler, lambda message: message.text and not message.text.startswith("/"), state="*")
