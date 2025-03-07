# bot.py
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.config import TOKEN
from handlers import start, cards, payment, session, admin

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрируем обработчики
    start.register_handlers(dp)
    cards.register_handlers(dp)
    payment.register_handlers(dp)
    session.register_handlers(dp)
    admin.register_handlers(dp)

    # Запускаем поллинг
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
