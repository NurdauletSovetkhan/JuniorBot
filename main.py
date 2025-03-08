import logging
import sys
from os import getenv
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers.start_handler import router as start_router
from handlers.text_handler import router as text_router
from handlers.image_handler import router as image_router
from handlers.math_handler import router as math_router

load_dotenv()
TOKEN = getenv("TOKEN")

# turn on logging
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(start_router)
    dp.include_router(math_router)
    dp.include_router(text_router)
    dp.include_router(image_router)
    # And the run events dispatching
    await dp.start_polling(bot)

@app.get("/")
async def read_root():
    return {"message": "Bot is running"}

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvicorn.run(app, host="0.0.0.0", port=8000)