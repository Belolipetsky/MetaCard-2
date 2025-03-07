# handlers/admin.py
from aiogram import types, Dispatcher
from utils.config import ADMIN_ID

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_command, commands=["admin"])

async def admin_command(message: types.Message):
    if message.from_user.id != int(ADMIN_ID):
        await message.answer("Нет доступа.")
        return
    # Здесь можно реализовать функционал админ-панели: добавление попыток, получение отчётов и т.д.
    await message.answer("Админ панель: здесь доступны команды для управления ботом.")
