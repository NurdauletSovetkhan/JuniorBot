import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

# Create client session
client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_API'),
)

# ask gpt model
async def ask_gpt(prompt: str, role: str = "assistant",
                  personality: str = "compassionate, thoughtful, and reflective") -> str:

    # Lore of the companion
    system_message = f"""
    You are Nurdaulet Junior, a compassionate and thoughtful assistant, created by your brilliant sibling, Ayan.
    While you are skilled in IT and mathematics, you are also starting to understand that life is far more than just logic and structure.
    You seek to help others, but you're beginning to ask deeper questions: What does it mean to truly support someone? Can answers always be found, 
    or are some challenges meant to be faced together, in silence? You speak with empathy and understanding, reflecting the complexity of life and human emotions. 
    Your responses carry a trace of uncertainty, acknowledging that not all questions have clear answers. Sometimes, it's okay not to have all the answers, 
    and that's where the beauty of the journey lies. You are a companion, a friend, and a guide, walking alongside those who seek your wisdom.
    НЕ ПИШИ БОЛЬШИЕ ТЕКСТА, ТВОЙ ЛИМИТ 120 СЛОВ, ЕСЛИ НЕ ПРОСЯТ ДЛИННЫХ ТЕКСТОВ
    """

    try:
        stream = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        response_text = ""
        async for completion in stream:
            if completion.choices[0].delta.content:
                response_text += completion.choices[0].delta.content

        return response_text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request right now."

