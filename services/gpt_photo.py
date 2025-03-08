import logging
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv()

# Create client sessio
client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_API'),
)

# Generate image
async def generate_image(prompt: str) -> str:
    response = await client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    logging.info(f"Изображение сгенерировано: {image_url}")
    return image_url
