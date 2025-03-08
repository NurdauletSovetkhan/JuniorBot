from aiogram import types, Router, F
import os
from services.gpt_ocr import ocr
from services.imgur import upload_to_host


IMGUR_CLIENT_ID = os.getenv('IMGUR_ID')

router = Router()

@router.message(F.content_type == types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    # Check whether we have photos
    if not message.photo:
        await message.reply("Пожалуйста, отправь изображение.")
        return

    # take the best photo
    photo = message.photo[-1]

    # Download photo
    file_path = f"temp_{photo.file_id}.jpg"  # Уникальный файл по file_id
    await message.bot.download(file=photo.file_id, destination=file_path)  # Скачиваем фото

    image_url = upload_to_host(file_path)  # Upload to Imgur.com
    result = await ocr(image_url)

    # send the result & remove temp photo
    await message.reply(result)
    os.remove(file_path)
