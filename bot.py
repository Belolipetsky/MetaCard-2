import logging
from aiogram import Bot, Dispatcher, executor
from utils import config
from handlers import start, cards, session
# from handlers import payment, admin  # Пока не используются

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

def register_all_handlers(dp):
    start.register_start_handlers(dp)
    cards.register_cards_handlers(dp)
    session.register_session_handlers(dp)
    # payment.register_payment_handlers(dp)
    # admin.register_admin_handlers(dp)

register_all_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
