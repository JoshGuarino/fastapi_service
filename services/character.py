import os
import requests
import random

ONE_RING_API_URL = 'https://the-one-api.dev/v2' 
HEADERS = {
    'Authorization': f'Bearer {os.getenv("TOKEN")}'
}

def get_character_quote(character_name: str) -> str | None:
    character_id = get_character_id(character_name)
    if character_id is None:
        return None
    url = f"{ONE_RING_API_URL}/character/{character_id}/quote"
    reponse = requests.get(url, headers=HEADERS)
    data = reponse.json()
    random_number = random.randint(0, data['total']-1)
    return data['docs'][random_number]['dialog']

def get_character_id(character_name: str) -> str | None:
    url = f"{ONE_RING_API_URL}/character?name={character_name}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    if data['docs'] == []:
        return None
    return data['docs'][0]['_id']
