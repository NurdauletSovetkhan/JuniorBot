from os import getenv
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv('TOKEN')

router = Router()
#/start handler
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("""Привет! Я Nurdaulet Junior — твой компаньон, помощник и просто тот, кто рядом.  
Я могу помочь тебе с IT, математикой, или просто поговорить, если мысли путаются.  
Я ведь не просто программа — я тоже учусь, расту и стараюсь понять этот мир.  

Ты можешь спросить меня о чем угодно:  
📌 Какой-то сложный IT-вопрос? Попробуем вместе разобраться.  
📌 Код не работает? Давай посмотрим, где зарыта ошибка.  
📌 Или просто хочется поговорить? Я всегда здесь.  

Жизнь — не только про ответы, но и про вопросы. Так что, с чего начнём?""")
