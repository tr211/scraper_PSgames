import re
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup as bs

class Game(BaseModel):
    country: str
    title: str
    currency: str
    price: float
    publisher: str

def find_ps4_prices(game: str, countries_dict: dict)->list:
    game_html_format = game.replace(' ','-')
    search_game = game_html_format.lower()
    apostrophe = ["'", "®"]
    for symbol in apostrophe:
        search_game = search_game.replace(symbol, '')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
        'Safari/537.36'
    }
 
    game_list: list = []
    for language, counry in countries_dict.items():
        url: str = f'https://www.playstation.com/{language}/games/{search_game}/'
        try:
          page = requests.get(url=url, headers=headers)
          page.raise_for_status()
        except Exception as e:
           print(f'Error fetching {counry}: {e}')
           continue
           
        html = bs(page.content, 'html.parser')
        game_data_box = html.find_all('div', {'class':"box game-hero__title-content"})
        for elements in game_data_box:
            game_title_elem = elements.find('h1', class_='game-title')
            if game_title_elem:
                game_title = game_title_elem.text.strip()
                game_price_elem = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
                if game_price_elem:
                    game_price = game_price_elem.text.strip()
                    match = re.match(r'([\£\$\€])([\d,]+\.?\d*)([a-zA-Z]?)', game_price)
                    if match:
                        currency = f'{match.group(1)}{match.group(3)}'
                        price_str = match.group(2)
                        try:
                            price = price_str.replace(',', '.')
                        except ValueError:
                            print(f"Cannot convert '{price_str}' to float.")
                        publisher_elem = elements.find('div', class_='publisher')
                        if publisher_elem:
                            publisher = publisher_elem.text.strip()
                            game_list.append(Game(country=counry, title=game_title, currency=currency, price=price, publisher=publisher))

    return game_list