# import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.config import Bot_Token
from app.handlers import register_handlers
from app.database.db import init_db

# logging.basicConfig(level=logging.INFO, filename='logs/bot.log', filemode='a',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


dp = Dispatcher()
bot = Bot(Bot_Token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
register_handlers(dp)


# logging.info("Bot ishga tushdi")


async def main():
    await init_db()
    await dp.start_polling(bot, skip_updates=True)




if __name__ == "__main__":
    # try:
    asyncio.run(main())
    # except Exception as e:
    #     print(e)
        # logging.error(f"Bot ishlashida xato: {e}")


