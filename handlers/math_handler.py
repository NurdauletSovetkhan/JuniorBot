from os import getenv
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services.gpt import ask_gpt
from services.math import render_latex_to_image

TOKEN = getenv('TOKEN')

router = Router()

@router.message(Command("math"))
async def math_handler(message: Message):
        await message.answer("Сию минуту, друг")

        user_input = message.text.replace("/math", "").strip()
        if not user_input:
            await message.answer("Я не понял твою задачу!")
            return

        user_input += " It's a math problem. PLEASE DONT USE LATEX AT ALL, JUST WRITE IT IN TEXT FORM"

        response = await ask_gpt(user_input)
        if not response:
            await message.answer("Я не смог посчитать это..")
            return

        await message.answer(response)


        # image_path = render_latex_to_image(response)
        # if not image_path:
        #     await message.answer("❌ Ошибка рендеринга LaTeX.")
        #     return
        #
        # try:
        #     await message.answer_photo(FSInputFile(image_path))
        # except Exception as e:
        #     await message.answer(f"❌ Ошибка отправки изображения: {e}")


