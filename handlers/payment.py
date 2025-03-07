# Пока функционал оплаты не используется в MVP, весь код ниже закомментирован.

# from aiogram import types, Dispatcher
#
# async def payment_handler(message: types.Message):
#     # Здесь должен быть код для обработки платежей.
#     await message.answer("Платежная система временно недоступна.")
#
# def register_payment_handlers(dp: Dispatcher):
#     dp.register_message_handler(payment_handler, lambda message: message.text.startswith("Купить"))
