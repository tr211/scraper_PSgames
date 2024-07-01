import json
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup as bs

'''
for lokal json file 
variable "game" need uncomment
'''
# game: str = input('enter game: ')

def scraperPS(game: str)->list:
    '''
    function retern list of objects with 
    price from all countries realetet PS store
    '''      
    countries_dict = {
    'us': 'United States', 'ca': 'Canada', 'gb': 'United Kingdom',
      'de': 'Germany', 'fr': 'France', 'it': 'Italy', 'es': 'Spain',
        'jp': 'Japan', 'au': 'Australia', 'nz': 'New Zealand', 'br': 'Brazil',
          'mx': 'Mexico', 'kr': 'South Korea', 'hk': 'Hong Kong', 'tw': 'Taiwan',
            'sg': 'Singapore', 'my': 'Malaysia', 'id': 'Indonesia', 'th': 'Thailand',
              'ph': 'Philippines', 'in': 'India', 'sa': 'Saudi Arabia', 'ae': 'United Arab Emirates',
                'za': 'South Africa', 'ru': 'Russia', 'tr': 'Turkey', 'pl': 'Poland', 'no': 'Norway', 'se': 'Sweden',
                  'dk': 'Denmark', 'fi': 'Finland', 'nl': 'Netherlands', 'be': 'Belgium', 'lu': 'Luxembourg',
                    'at': 'Austria', 'ch': 'Switzerland', 'pt': 'Portugal', 'gr': 'Greece', 'ie': 'Ireland',
                      'hu': 'Hungary', 'cz': 'Czech Republic', 'sk': 'Slovakia', 'bg': 'Bulgaria', 'ro': 'Romania',
                        'hr': 'Croatia', 'si': 'Slovenia', 'il': 'Israel', 'cl': 'Chile', 'ar': 'Argentina',
                          'co': 'Colombia', 'pe': 'Peru', 'uy': 'Uruguay'
                          }
    
    search_game = game.replace(' ','-')
    

    class Game(BaseModel):
        country: str
        title: str
        price: str
        publisher: str
        
    game_list: list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
                  'Safari/537.36'}


    for k, v in countries_dict.items():
        url: str = f'https://www.playstation.com/en-{k}/games/{search_game}/'
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
            game_titl = elements.find('h1', class_='game-title')
            if game_titl:
                game_title = game_titl.text.strip()
                game_pris = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
                if game_pris:
                  game_price = game_pris.text.strip()
                  publisher_elem = elements.find('div', class_='publisher')
                  if publisher_elem:
                    publisher = publisher_elem.text.strip()
                    game_list.append(Game(country=v, title=game_title, price=game_price, publisher=publisher))

    
             
    return game_list
                
if __name__== '__main__':
    pass
# '''
# if need lokal json file with game
# uncomment code below
# '''
#   scrap = scraperPS(game)
#   scrap_dicts = [game.dict() for game in scrap]

# with open('games_table.json', 'w') as game_fi:
#     json.dump(scrap_dicts, game_fi, indent=4)
# print('Data has bin writen')