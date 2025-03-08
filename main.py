import logging
import sys
from os import getenv
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from handlers.start_handler import router as start_router
from handlers.text_handler import router as text_router
from handlers.image_handler import router as image_router
from handlers.math_handler import router as math_router

load_dotenv()
TOKEN = getenv("TOKEN")

# turn on logging
logging.basicConfig(level=logging.INFO)


# Создаем FastAPI приложение с использованием lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация бота и диспетчера
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(math_router)
    dp.include_router(text_router)
    dp.include_router(image_router)

    # Запуск бота
    await dp.start_polling(bot)

    yield  # Код для завершения работы можно вставить сюда


# Создаем объект FastAPI с использованием lifespan
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Bot is running"}


if __name__ == "__main__":
    import uvicorn

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Запуск FastAPI через Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
