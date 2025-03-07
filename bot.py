import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.config import API_TOKEN, ADMIN_ID
import handlers.start as start_handler
import handlers.cards as cards_handler
import handlers.payment as payment_handler
import handlers.session as session_handler
import handlers.admin as admin_handler

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

def register_handlers(dp):
    start_handler.register_handlers(dp)
    cards_handler.register_handlers(dp)
    payment_handler.register_handlers(dp)
    session_handler.register_handlers(dp)
    admin_handler.register_handlers(dp)

async def main():
    register_handlers(dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())

