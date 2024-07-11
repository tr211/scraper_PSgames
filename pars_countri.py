import os
import json
import re
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup as bs

# game: str = input('enter game: ')
class Game(BaseModel):
    country: str
    title: str
    currency: str
    price: float
    publisher: str

# pythonfile = 'all_lang_countries.json'
# fi = os.path.abspath(pythonfile)
# countries_dict = {}

def json_to_dict(fi)-> dict:
   with open(fi, 'r') as countries_dict:
      return json.load(countries_dict)

# game = 'god of war'

def scraperPS(game: str, countries_dict: dict)->list:
    
    search_game = game.replace(' ','-')
    game_list: list = []
    # game_price_list: list = []
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
                  'Safari/537.36'}

    for k, v in countries_dict.items():
        url: str = f'https://www.playstation.com/{k}/games/{search_game}/'
        # print(f'Sraping element: {url}')
        try:
          page = requests.get(url=url, headers=headers)
          page.raise_for_status()
        except requests.RequestException as e:
           print(f'Error fetching {v}: {e}')
           continue
           
        soupe = bs(page.content, 'html.parser')
        res = soupe.find_all('div', {'class':"box game-hero__title-content"})

        for elements in res:
            game_title_elem = elements.find('h1', class_='game-title')
            if game_title_elem:
                game_title = game_title_elem.text.strip()
                game_price_elem = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
                if game_price_elem:
                    game_price = game_price_elem.text.strip()
                    match = re.match(r'([\£\$\€])([\d,]+\.?\d*)([a-zA-Z]?)', game_price)
                    if match:
                        currency = match.group(1) + match.group(3)
                        price_str = match.group(2)
                        try:
                            price = float(price_str)
                        except ValueError:
                            print(f"Cannot convert '{price_str}' to float.")
                        # price = float(price_str)
                        publisher_elem = elements.find('div', class_='publisher')
                        if publisher_elem:
                            publisher = publisher_elem.text.strip()
                            game_list.append(Game(country=v, title=game_title, currency=currency, price=price, publisher=publisher))

    return game_list

