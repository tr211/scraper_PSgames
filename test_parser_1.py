
import json
# from pydantic import BaseModel
# import requests
# from bs4 import BeautifulSoup as bs

# game: str = input('Enter game: ')

# def scraperPS(game: str) -> list:
#     '''
#     Function returns a list of objects with 
#     price from all countries related to PS store.
#     '''      
#     countries_dict = {
#         'us': 'United States', 'ca': 'Canada', 'gb': 'United Kingdom',
#         'de': 'Germany', 'fr': 'France', 'it': 'Italy', 'es': 'Spain',
#         'jp': 'Japan', 'au': 'Australia', 'nz': 'New Zealand', 'br': 'Brazil',
#         'mx': 'Mexico', 'kr': 'South Korea', 'hk': 'Hong Kong', 'tw': 'Taiwan',
#         'sg': 'Singapore', 'my': 'Malaysia', 'id': 'Indonesia', 'th': 'Thailand',
#         'ph': 'Philippines', 'in': 'India', 'sa': 'Saudi Arabia', 'ae': 'United Arab Emirates',
#         'za': 'South Africa', 'ru': 'Russia', 'tr': 'Turkey', 'pl': 'Poland', 'no': 'Norway', 'se': 'Sweden',
#         'dk': 'Denmark', 'fi': 'Finland', 'nl': 'Netherlands', 'be': 'Belgium', 'lu': 'Luxembourg',
#         'at': 'Austria', 'ch': 'Switzerland', 'pt': 'Portugal', 'gr': 'Greece', 'ie': 'Ireland',
#         'hu': 'Hungary', 'cz': 'Czech Republic', 'sk': 'Slovakia', 'bg': 'Bulgaria', 'ro': 'Romania',
#         'hr': 'Croatia', 'si': 'Slovenia', 'il': 'Israel', 'cl': 'Chile', 'ar': 'Argentina',
#         'co': 'Colombia', 'pe': 'Peru', 'uy': 'Uruguay'
#     }
    
#     search_game = game.replace(' ', '-')
    
#     class Game(BaseModel):
#         country: str
#         title: str
#         price: str
#         publisher: str
        
#     game_list: list = []
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
#                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
#                   'Safari/537.36'}

#     for k, v in countries_dict.items():
#         url = f'https://www.playstation.com/en-{k}/games/{search_game}/'
#         # print(f'Scraping URL: {url}')
#         try:
#             page = requests.get(url,headers=headers)
#             page.raise_for_status()
#         except requests.RequestException as e:
#             print(f'Error fetching {url}: {e}')
#             continue
        
#         soup = bs(page.content, 'html.parser')
#         # print(f'Page content for {url[:30]}: {page.content[:100]}...')  # Print a snippet of the page content
#         res = soup.find_all('div', {'class':"box game-hero__title-content"})
#         # print(f'Found {len(res)} elements with class "box game-hero__title-content"')

#         for elements in res:
#             game_title_elem = elements.find('h1', class_='game-title')
#             print(f'Game title element: {game_title_elem}')
#             if game_title_elem:
#                 game_title = game_title_elem.text.strip()
#                 print(f'Game title: {game_title}')
#                 game_price_elem = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
#                 print(f'Game price element: {game_price_elem}')
                
#                 if game_price_elem:
#                     game_price = game_price_elem.text.strip()
#                     print(f'Game price: {game_price}')
#                     publisher_elem = elements.find('div', class_='publisher')
                    
#                     if publisher_elem:
#                         publisher = publisher_elem.text.strip()
#                         game_list.append(Game(country=v, title=game_title, price=game_price, publisher=publisher))
    
#     return game_list
                
# if __name__ == '__main__':
#     scrap = scraperPS(game)
#     scrap_dicts = [game.dict() for game in scrap]

#     with open('games_table.json', 'w') as game_fi:
#         json.dump(scrap_dicts, game_fi, indent=4)
#     print('Data has been written')
countries = {
    "us-en": "United States",
    "us-es": "Estados Unidos",
    "ca-en": "Canada",
    "ca-fr": "Canada",
    "mx-es": "México",
    "br-pt": "Brasil",
    "ar-es": "Argentina",
    "cl-es": "Chile",
    "co-es": "Colombia",
    "pe-es": "Perú",
    "uk-en": "United Kingdom",
    "de-de": "Deutschland",
    "fr-fr": "France",
    "fr-en": "France",
    "it-it": "Italia",
    "it-en": "Italy",
    "es-es": "España",
    "es-en": "Spain",
    "nl-nl": "Nederland",
    "nl-en": "Netherlands",
    "be-nl": "België",
    "be-fr": "Belgique",
    "at-de": "Österreich",
    "at-en": "Austria",
    "ch-de": "Schweiz",
    "ch-fr": "Suisse",
    "ch-it": "Svizzera",
    "se-sv": "Sverige",
    "no-no": "Norge",
    "no-en": "Norway",
    "dk-da": "Danmark",
    "fi-fi": "Suomi",
    "ie-en": "Ireland",
    "pt-pt": "Portugal",
    "gr-el": "Ελλάδα",
    "gr-en": "Greece",
    "ru-ru": "Россия",
    "ru-en": "Russia",
    "pl-pl": "Polska",
    "pl-en": "Poland",
    "cz-cs": "Česká republika",
    "cz-en": "Czech Republic",
    "hu-hu": "Magyarország",
    "hu-en": "Hungary",
    "jp-ja": "日本",
    "jp-en": "Japan",
    "kr-ko": "대한민국",
    "kr-en": "South Korea",
    "hk-zh": "香港",
    "hk-en": "Hong Kong",
    "tw-zh": "台灣",
    "tw-en": "Taiwan",
    "sg-en": "Singapore",
    "my-ms": "Malaysia",
    "my-en": "Malaysia",
    "th-th": "ประเทศไทย",
    "th-en": "Thailand",
    "id-id": "Indonesia",
    "id-en": "Indonesia",
    "ph-en": "Philippines",
    "au-en": "Australia",
    "nz-en": "New Zealand",
    "sa-ar": "المملكة العربية السعودية",
    "ae-en": "United Arab Emirates",
    "za-en": "South Africa",
    "il-he": "ישראל",
    "il-en": "Israel",
    "tr-tr": "Türkiye",
    "tr-en": "Turkey",
    "eg-ar": "مصر",
    "eg-en": "Egypt"
    
}

# with open('all_lang_countries.json', 'w') as fi:
    # fi.write(countries)
with open("all_lang_countries.json", "w") as outfile: 
    json.dump(countries, outfile, indent=4)