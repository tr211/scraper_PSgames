import os
import json
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


def json_to_dict(fi)-> dict:
   with open(fi, 'r') as countries_dict:
      return json.load(countries_dict)



def scraperPS(game: str, countries_dict: dict)->list:
    
    search_game = game.replace(' ','-')
    game_list: list = []
    # game_price_list: list = []
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
                  'Safari/537.36'}

    for k, v in countries_dict.items():
        url: str = f'https://www.playstation.com/{k}/games/{search_game}/'
       
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
                    match = re.match(r'([A-Za-z]{1,3}?\$|[\€\$\¥\£\₹\₽\₺\₪\₫\฿\₩]|[A-Za-z]{1,3})?[\s]?([\d,]+\.?\d*|\d+\.\d+)[\s]?([A-Za-z]{1,3})?', game_price)
                    if match:
                        currency = match.group(1) or match.group(3) or ''
                        price_str = match.group(2)
                        currency = currency.strip() if currency else ''

                        try:
                            price = price_str.replace(',', '.')
                        except ValueError:
                            print(f"Cannot convert '{price_str}' to float.")
                        publisher_elem = elements.find('div', class_='publisher')
                        if publisher_elem:
                            publisher = publisher_elem.text.strip()
                            game_list.append(Game(country=v, title=game_title, currency=currency, price=price, publisher=publisher))


    return game_list


