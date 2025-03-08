import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers.start_handler import router as start_router
from handlers.text_handler import router as text_router
from handlers.image_handler import router as image_router
from handlers.math_handler import router as math_router

# Получается роутеры прилегают к диспатчеру. Диспатчер типа центр, хаб, а хендлеры как источники

load_dotenv()
TOKEN = getenv("TOKEN")

# turn on logging
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(start_router)
    dp.include_router(math_router)
    dp.include_router(text_router)
    dp.include_router(image_router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())