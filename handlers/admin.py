from aiogram import types, Dispatcher

async def admin_command(message: types.Message):
    # Пример простой админ-команды для тестирования
    await message.answer("Админ-панель: здесь можно добавлять попытки и просматривать отчёты.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_command, commands="admin", state="*")
