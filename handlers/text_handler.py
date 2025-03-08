import random
from os import getenv
from services.gpt import ask_gpt
from aiogram import Router, F
from aiogram.types import Message, ContentType, URLInputFile
from services.gpt_photo import generate_image


TOKEN = getenv('TOKEN')

router = Router()

# Name of the bot & trigger words
BOT_MENTION = "Nurdaulet Junior"
TRIGGER_WORDS = ["бот", "помощник", "Nurdaulet", "Junior", "собеседник", "Nurdaulet Junior", "nurdaulet junior", "junior", "jun", "младший", "дурак", "джуниор", "everyone", "джун", "жун"]
ASK_FOR_PHOTO = ["нарисуй", "нарисуй мне", "нарисуй картинку", "нарисуй что-нибудь", "хочу фото", "draw", "draw me", "draw a picture", "draw something", "I want a photo"]
ANSWER_PROBABILITY = 30


@router.message(F.content_type == ContentType.TEXT)
async def text_handler(message: Message):
    user_input = message.text

    # Check the mention of the bot
    if any(trigger_word.lower() in user_input.lower() for trigger_word in TRIGGER_WORDS) or message.reply_to_message:
        # Send the input to gpt
        response = await ask_gpt(user_input)
        try:
            # Send answer to the user
            await message.answer(response)
        except TypeError:
            await message.answer("Sad :(")

    elif any(trigger_word.lower() in user_input.lower() for trigger_word in ASK_FOR_PHOTO):
        # Generate an image
        image_url = await generate_image(user_input)

        image = URLInputFile(
            image_url,
            filename="python-logo.png"
        )
        await message.answer_photo(image)

    else:
        # Random message
        if random.randint(1, 100) <= ANSWER_PROBABILITY:
            # Ask the model to check the topic of the message
            question = f"О чем идет речь в следующем сообщении: '{user_input}'?"
            response = await ask_gpt(question)

            # Some comments from gpt
            humor_response = await ask_gpt(f"Отреагируй на следующее сообщение с юмором или комментарием как маленький ребенок, твой ответ должен быть кратким, но без эмоджи'{response}'")

            try:
                # Send our answer to user
                await message.answer(f"{humor_response}")
            except TypeError:
                await message.answer("Sad :(")
        else:
            pass

