# handlers/payment.py
from aiogram import types, Dispatcher
from aiogram.types import LabeledPrice
from utils.config import ADMIN_ID
from keyboards.payment_keyboard import payment_keyboard

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_payment_callback, lambda c: c.data and c.data.startswith("buy_"))
    dp.register_pre_checkout_query_handler(process_pre_checkout_query)
    dp.register_message_handler(process_successful_payment, content_types=types.ContentType.SUCCESSFUL_PAYMENT)

async def process_payment_callback(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == int(ADMIN_ID):
        await callback_query.message.answer("🔓 Администратор: попытка добавлена бесплатно.")
        # Здесь обновляем баланс попыток для администратора в БД
        return

    # Симуляция оплаты (реальная отправка инвойса может быть реализована через метод send_invoice)
    await callback_query.message.answer("Оплата пока не реализована. Симуляция успешной оплаты.")
    # После симуляции можно добавить попытки в баланс пользователя

async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def process_successful_payment(message: types.Message):
    await message.answer("Оплата прошла успешно! Попытки добавлены.")
    # Здесь обновляем баланс попыток пользователя в БД
