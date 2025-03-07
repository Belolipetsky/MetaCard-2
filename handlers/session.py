# handlers/session.py
from aiogram import types, Dispatcher
from keyboards.session_keyboard import session_keyboard
from utils.texts import SESSION_INFO

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_session_signup, lambda c: c.data == "session_signup")

async def process_session_signup(callback_query: types.CallbackQuery):
    await callback_query.message.answer(SESSION_INFO, reply_markup=session_keyboard())
