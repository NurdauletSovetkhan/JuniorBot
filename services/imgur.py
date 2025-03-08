import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Unq client id
IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')


def upload_to_host(file_path: str) -> str:
    # Uploads photo to imgur then delete it
    url = "https://api.imgur.com/3/upload"

    headers = {
        "Authorization": f"Client-ID {IMGUR_CLIENT_ID}",
    }

    with open(file_path, 'rb') as file:
        response = requests.post(url, headers=headers, files={'image': file})

        if response.status_code == 200:
            result = response.json()
            if result['success']:
                return result['data']['link']
            else:
                return "Error uploading image"
        else:
            return f"Error: {response.status_code}"