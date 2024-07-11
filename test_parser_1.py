
import json
# # from pydantic import BaseModel
# # import requests
# # from bs4 import BeautifulSoup as bs

# # game: str = input('Enter game: ')

# # def scraperPS(game: str) -> list:
# #     '''
# #     Function returns a list of objects with 
# #     price from all countries related to PS store.
# #     '''      
# #     countries_dict = {
# #         'us': 'United States', 'ca': 'Canada', 'gb': 'United Kingdom',
# #         'de': 'Germany', 'fr': 'France', 'it': 'Italy', 'es': 'Spain',
# #         'jp': 'Japan', 'au': 'Australia', 'nz': 'New Zealand', 'br': 'Brazil',
# #         'mx': 'Mexico', 'kr': 'South Korea', 'hk': 'Hong Kong', 'tw': 'Taiwan',
# #         'sg': 'Singapore', 'my': 'Malaysia', 'id': 'Indonesia', 'th': 'Thailand',
# #         'ph': 'Philippines', 'in': 'India', 'sa': 'Saudi Arabia', 'ae': 'United Arab Emirates',
# #         'za': 'South Africa', 'ru': 'Russia', 'tr': 'Turkey', 'pl': 'Poland', 'no': 'Norway', 'se': 'Sweden',
# #         'dk': 'Denmark', 'fi': 'Finland', 'nl': 'Netherlands', 'be': 'Belgium', 'lu': 'Luxembourg',
# #         'at': 'Austria', 'ch': 'Switzerland', 'pt': 'Portugal', 'gr': 'Greece', 'ie': 'Ireland',
# #         'hu': 'Hungary', 'cz': 'Czech Republic', 'sk': 'Slovakia', 'bg': 'Bulgaria', 'ro': 'Romania',
# #         'hr': 'Croatia', 'si': 'Slovenia', 'il': 'Israel', 'cl': 'Chile', 'ar': 'Argentina',
# #         'co': 'Colombia', 'pe': 'Peru', 'uy': 'Uruguay'
# #     }
    
# #     search_game = game.replace(' ', '-')
    
# #     class Game(BaseModel):
# #         country: str
# #         title: str
# #         price: str
# #         publisher: str
        
# #     game_list: list = []
# #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
# #                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
# #                   'Safari/537.36'}

# #     for k, v in countries_dict.items():
# #         url = f'https://www.playstation.com/en-{k}/games/{search_game}/'
# #         # print(f'Scraping URL: {url}')
# #         try:
# #             page = requests.get(url,headers=headers)
# #             page.raise_for_status()
# #         except requests.RequestException as e:
# #             print(f'Error fetching {url}: {e}')
# #             continue
        
# #         soup = bs(page.content, 'html.parser')
# #         # print(f'Page content for {url[:30]}: {page.content[:100]}...')  # Print a snippet of the page content
# #         res = soup.find_all('div', {'class':"box game-hero__title-content"})
# #         # print(f'Found {len(res)} elements with class "box game-hero__title-content"')

# #         for elements in res:
# #             game_title_elem = elements.find('h1', class_='game-title')
# #             print(f'Game title element: {game_title_elem}')
# #             if game_title_elem:
# #                 game_title = game_title_elem.text.strip()
# #                 print(f'Game title: {game_title}')
# #                 game_price_elem = elements.find('span', class_='psw-l-line-left psw-l-line-wrap')
# #                 print(f'Game price element: {game_price_elem}')
                
# #                 if game_price_elem:
# #                     game_price = game_price_elem.text.strip()
# #                     print(f'Game price: {game_price}')
# #                     publisher_elem = elements.find('div', class_='publisher')
                    
# #                     if publisher_elem:
# #                         publisher = publisher_elem.text.strip()
# #                         game_list.append(Game(country=v, title=game_title, price=game_price, publisher=publisher))
    
# #     return game_list
                
# # if __name__ == '__main__':
# #     scrap = scraperPS(game)
# #     scrap_dicts = [game.dict() for game in scrap]

# #     with open('games_table.json', 'w') as game_fi:
# #         json.dump(scrap_dicts, game_fi, indent=4)
# #     print('Data has been written')
# import json

countries = {
    "ar-es": "Argentina",
    "au-en": "Australia",
    "at-de": "Austria (Österreich)",
    "bh-en": "Bahrain (English)",
    "bh-ar": "Bahrain (Arabic)",
    "be-fr": "Belgium (Français)",
    "be-nl": "Belgium (Nederlands)",
    "bo-es": "Bolivia",
    "br-pt": "Brasil",
    "bg-en": "Bulgaria (English)",
    "bg-bg": "Bulgaria (България)",
    "ca-en": "Canada",
    "ca-fr": "Canada (French)",
    "cl-es": "Chile",
    "cn-zh": "中国大陆 (简体中文)",
    "co-es": "Colombia",
    "cr-es": "Costa Rica",
    "hr-en": "Croatia (English)",
    "hr-hr": "Croatia (Hrvatska)",
    "cy-en": "Cyprus",
    "cz-en": "Czech Republic (English)",
    "cz-cs": "Czech Republic (Ceská Republika)",
    "dk-da": "Denmark (Danmark)",
    "dk-en": "Denmark (English)",
    "ec-es": "Ecuador",
    "sv-es": "El Salvador",
    "fi-en": "Finland (English)",
    "fi-fi": "Finland (Suomi)",
    "fr-fr": "France",
    "de-de": "Germany (Deutschland)",
    "gr-en": "Greece (English)",
    "gr-el": "Greece (Ελλαδα)",
    "gt-es": "Guatemala",
    "hn-es": "Honduras",
    "hk-en": "Hong Kong (English)",
    "hk-zh-hans": "Hong Kong (简体中文)",
    "hk-zh-hant": "Hong Kong (繁體中文)",
    "hk-zh-hk-hant": "香港 (繁體中文)",
    "hk-zh-hk-hans": "香港 (简体中文)",
    "hu-en": "Hungary (English)",
    "hu-hu": "Hungary (Magyarország)",
    "is-en": "Iceland (English)",
    "in-en": "India",
    "id-en": "Indonesia (English)",
    "ie-en": "Ireland",
    "il-en": "Israel (English)",
    "il-he": "Israel",
    "it-it": "Italy",
    "jp-ja": "Japan (日本)",
    "kr-ko": "Korea (한국어)",
    "kw-ar": "Kuwait (Arabic)",
    "kw-en": "Kuwait (English)",
    "lb-ar": "Lebanon (Arabic)",
    "lb-en": "Lebanon (English)",
    "lu-de": "Luxembourg (Deutsch)",
    "lu-fr": "Luxembourg (Français)",
    "my-en": "Malaysia (English)",
    "mt-en": "Malta",
    "mx-es": "Mexico (México)",
    "nl-nl": "Nederland",
    "nz-en": "New Zealand",
    "ni-es": "Nicaragua",
    "no-en": "Norway (English)",
    "no-no": "Norway (Norge)",
    "om-ar": "Oman (Arabic)",
    "om-en": "Oman (English)",
    "pa-es": "Panama (Panamá)",
    "py-es": "Paraguay",
    "pe-es": "Peru (Perú)",
    "ph-en": "Philippines (English)",
    "pl-en": "Poland (English)",
    "pl-pl": "Poland (Polska)",
    "pt-pt": "Portugal",
    "qa-ar": "Qatar (Arabic)",
    "qa-en": "Qatar (English)",
    "ro-en": "Romania (English)",
    "ro-ro": "Romania (România)",
    "ru-ru": "Russia (Россия)",
    "sa-ar": "Saudi Arabia (Arabic)",
    "sa-en": "Saudi Arabia (English)",
    "rs-sr": "Serbia (Srbija)",
    "sg-en": "Singapore (English)",
    "si-en": "Slovenia (English)",
    "si-sl": "Slovenia (Slovenija)",
    "sk-en": "Slovakia (English)",
    "sk-sk": "Slovakia (Slovenská Republika)",
    "za-en": "South Africa",
    "es-es": "Spain (España)",
    "se-en": "Sweden (English)",
    "se-sv": "Sweden (Sverige)",
    "ch-de": "Switzerland (Deutsch)",
    "ch-fr": "Switzerland (Français)",
    "ch-it": "Switzerland (Italiano)",
    "tw-en": "Taiwan (English)",
    "tw-zh-hant": "Taiwan (台灣繁體中文)",
    "th-en": "Thailand (English)",
    "th-th": "Thailand (ภาษาไทย)",
    "tr-en": "Turkey (English)",
    "tr-tr": "Turkey (Türkiye)",
    "ua-ru": "Ukraine (Російська мова)",
    "ua-uk": "Ukraine (Українська мова)",
    "ae-ar": "United Arab Emirates/ Middle East (Arabic)",
    "ae-en": "United Arab Emirates/ Middle East (English)",
    "us-en": "United States",
    "uk-en": "United Kingdom",
    "uy-es": "Uruguay",
    "vn-en": "Vietnam (English)"
}

# with open("countries_lang.json", "w") as outfile:
#     json.dump(countries, outfile, indent=4)



modified_country = {}

for k in countries.keys():
    key_country = k[:2]
    key_lang = k[3:]
    new_key = f"{key_lang}-{key_country}"
    modified_country[new_key] = countries[k]

with open("all_lang_countries.json", "w") as outfile: 
    json.dump(modified_country, outfile, indent=4)
    


