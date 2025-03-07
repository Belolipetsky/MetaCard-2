from aiogram import types, Dispatcher
from utils import texts
from keyboards import session_keyboard

def register_session_handlers(dp: Dispatcher):

    @dp.message_handler(lambda message: message.text == "🎓 Записаться на сессию")
    async def send_session_info(message: types.Message):
        await message.answer(texts.SESSION_INFO_TEXT, reply_markup=session_keyboard.get_session_keyboard())

    @dp.message_handler(lambda message: message.text == "🎓 Записаться на личную сессию")
    async def confirm_session_booking(message: types.Message):
        await message.answer(texts.SESSION_CONFIRM_TEXT)
        # Здесь можно добавить уведомление для администратора или логирование заявки.
        
def register_handlers(dp):
    register_session_handlers(dp)
