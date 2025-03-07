from aiogram import types, Dispatcher
from keyboards.session_keyboard import get_session_keyboard

SESSION_INFO = (
    "💡 Я могу провести личную сессию по нейрографике, чтобы помочь тебе осознать и трансформировать ситуацию.\n"
    "🎁 Бонус: вживую я предложу вытащить карту из уникальных колод, которых нет в этом боте.\n\n"
    "✨ На сессии мы:\n"
    "   - разберём твой запрос с помощью нейрографики\n"
    "   - найдём скрытые смыслы и решения\n"
    "   - создадим символический рисунок, запускающий изменения\n\n"
    "📌 Готов попробовать?"
)

async def session_command(message: types.Message):
    await message.answer(SESSION_INFO, reply_markup=get_session_keyboard())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(session_command, text="🎓 Записаться на сессию", state="*")
