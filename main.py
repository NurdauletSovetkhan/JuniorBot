import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from http.server import SimpleHTTPRequestHandler, HTTPServer
import asyncio
import threading
from handlers.start_handler import router as start_router
from handlers.text_handler import router as text_router
from handlers.image_handler import router as image_router
from handlers.math_handler import router as math_router

# Загружаем переменные окружения
load_dotenv()
TOKEN = getenv("TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start_router)
dp.include_router(math_router)
dp.include_router(text_router)
dp.include_router(image_router)

# Асинхронная инициализация бота
async def start_bot():
    # Запуск бота
    await dp.start_polling(bot)

# Класс обработчика для здоровья сервера
class HealthCheckHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
            logging.info("Health check passed")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Not Found")

# Функция для запуска HTTP-сервера
def run_server():
    port = int(getenv('PORT', 8000))  # Порт для сервера
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    logging.info(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Запуск HTTP-сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Запуск бота
    asyncio.run(start_bot())