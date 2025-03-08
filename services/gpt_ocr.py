import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from services.gpt import ask_gpt

load_dotenv()

# CLient session
client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_API'),
)

async def ocr(image_url: str):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    # Main logic
    answer = response.choices[0].message.content
    prompt = answer + "It's a analysis of image. If it's quiz, then just give answers e.g. A, B, D also if it's дай просто ответ, а не обьяснения. ЕСЛИ ЭТО МАТЕМАТИКА, ТО ПЕРЕПИШИ ЕЕ, В ИНОМ СЛУЧАЕ ПРОСТО ПОГОВОРИ О ФОТО, СПРОСИ КАК ВАМ И Т.Д."
    answer = await ask_gpt(prompt)
    return answer

