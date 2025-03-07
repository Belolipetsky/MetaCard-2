from aiogram import types, Dispatcher
from utils.config import ADMIN_ID
from keyboards.payment_keyboard import get_payment_keyboard

# Пример функции проверки попыток (в реальном проекте обращаться к БД)
def has_attempts(user_id):
    # Здесь реализуйте проверку из базы данных
    return False

async def payment_command(message: types.Message):
    user_id = message.from_user.id
    if str(user_id) == ADMIN_ID:
        await message.answer("🔓 Администратор: попытка добавлена бесплатно.")
        # Логика добавления попытки для админа
        return

    if not has_attempts(user_id):
        await message.answer(
            "💳 Для вытягивания карты нужно пополнить баланс. Выбери один из пакетов:",
            reply_markup=get_payment_keyboard()
        )
    else:
        await message.answer("У тебя есть попытки. Продолжаем!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(payment_command, lambda message: message.text.startswith("Купить"), state="*")
