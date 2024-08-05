from typing import List
import requests
from bs4 import BeautifulSoup as bs
import json
import os



def read_countries_languages_file() -> dict:
    file_path = os.path.abspath('ps_countries.json')
    with open(file_path, 'r') as countries_dict:
        return json.load(countries_dict)

def find_ps4_prices(game: str, countries_dict: dict) -> List[dict]:
    game_html_format = game.replace(' ', '-')
    search_game = game_html_format.lower()
    symbols_to_remove = ["'", "®"]
    for symbol in symbols_to_remove:
        search_game = search_game.replace(symbol, '')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    game_source = []

    for language, country in countries_dict.items():
        url = f'https://www.playstation.com/{language}/games/{search_game}/'
        try:
            page = requests.get(url, headers=headers)
            page.raise_for_status()
        except requests.RequestException as e:
            print(f'Error fetching: {e} for country: {country}')
            continue

        html = bs(page.content, 'html.parser')
        body_tag = html.find('body')
        if not body_tag:
            print(f'Body tag not found for country: {country}')
            continue

        data_product_info = body_tag.get('data-product-info')
        if not data_product_info:
            print(f'data-product-info attribute not found for country: {country}')
            continue

        game_info = json.loads(data_product_info)
        # Append the data to the game_source list
        game_source.append({
            'image': game_info.get('image'),
            'name': game_info.get('name'),
            'platforms': ', '.join(game_info.get('platforms', [])),
            'price': game_info.get('price'),
            'priceCurrency': game_info.get('priceCurrency'),
            'country': country
        })
    
    return game_source
