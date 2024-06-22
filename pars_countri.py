import json
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup as bs


# game: str = input('enter game: ')
game = 'god of war'
# game_list: list = []
def scraperPS(game: str):
    # countries: list =[
    # 'us','ca','gb','de','fr','it','es','jp','au','nz','br','mx','kr','hk','tw','sg','my','id','th','ph','in','sa','ae','za','ru','tr','pl','no','se','dk','fi','nl','be','lu','at','ch','pt','gr','ie','hu','cz','sk','bg','ro','hr','si','il','cl','ar','co','pe','uy'
    #  ]
    # countries = ['us','ca','gb','de','fr','it','es','jp','au']
   
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
    
    game_list: list = []

    class Game(BaseModel):
        country: str
        title: str
        prise: str
        
    for k, v in countries_dict.items():
        url: str = f'https://www.playstation.com/en-{k}/games/{search_game}/'

        page = requests.get(url=url)

        soupe = bs(page.content, 'html.parser')

        res = soupe.find_all('div', class_="box game-hero__title-content")

        

        for elements in res:
            game_titl = elements.find('h1', class_='game-title')
            if game_titl:
                game_title = game_titl.text.strip()
                game_pris = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
                if game_pris:
                    game_prise = game_pris.text.strip()
                    
                    game_list.append(Game(country=v, title=game_title, prise=game_prise))
    
             
    return game_list
                
# if __name__== '__main__':
#     pass
'''
if need lokal json file with game
'''
scrap = scraperPS(game)
scrap_dicts = [game.dict() for game in scrap]
with open('games_table.json', 'w') as game_fi:
    json.dump(scrap_dicts, game_fi, indent=4)
print('Data has bin writen')