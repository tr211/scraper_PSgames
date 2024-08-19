from pydantic import BaseModel
from typing import List, Optional
import requests
from bs4 import BeautifulSoup as bs
import json

class GameInfo(BaseModel):
    country: str
    title: Optional[str] = "No name available"
    currency: Optional[str] = "Unknown"
    price: Optional[float] = 0.0
    image: Optional[str] = "No image available"
    platforms: Optional[str] = "No platforms available"

def find_ps4_prices(game: str, countries_dict: dict) -> List[GameInfo]:
    game = game.replace(' ', '-')
    search_game = game.lower()
    symbols_to_remove = ["'", "®"]
    for symbol in symbols_to_remove:
        search_game = search_game.replace(symbol, '')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    game_source = []
    spetial_price_coyntry = ["Hungary", "India", "Japan", "South Korea"]

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
        
        if country in spetial_price_coyntry:
            price=game_info.get('price')
            price_str = str(price).replace('.', '')  # Convert price to string and remove dots
            price = int(price_str)

        # Create a GameInfo object and append it to the list
        game_source.append(GameInfo(
            image=game_info.get('image', "No image available"),
            title=game_info.get('name', "No name available"),
            platforms=', '.join(game_info.get('platforms', [])) if game_info.get('platforms') else "No platforms available",
            price=game_info.get('price', 0.0),
            currency=game_info.get('priceCurrency', "Unknown"),
            country=country
        ))
        

    return game_source