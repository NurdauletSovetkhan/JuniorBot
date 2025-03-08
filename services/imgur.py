import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

# Unique client id
IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')

def upload_to_host(file_path: str) -> str:
    # Uploads photo to imgur, then deletes it
    url = "https://api.imgur.com/3/upload"

    headers = {
        "Authorization": f"Client-ID {IMGUR_CLIENT_ID}",
    }

    retries = 3  # Количество попыток
    delay = 5    # Задержка в секундах между попытками

    for attempt in range(retries):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post(url, headers=headers, files={'image': file})

                if response.status_code == 200:
                    result = response.json()
                    if result['success']:
                        return result['data']['link']
                    else:
                        return "Error uploading image"
                else:
                    # Обработка ошибок 429 (слишком много запросов)
                    if response.status_code == 429:
                        print(f"Rate limit exceeded. Retrying in {delay} seconds...")
                        time.sleep(delay)  # Задержка перед повторной попыткой
                    else:
                        return f"Error: {response.status_code}"

        except Exception as e:
            return f"Exception occurred: {e}"

    return "Failed to upload image after several attempts."
