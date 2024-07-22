from bs4 import BeautifulSoup as bs
import requests


def check_all_exist_ps4_games():
    base_url = "https://www.truetrophies.com/ps4/games/"
    games_page_urls = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0":
        games_page_urls.append(base_url + letter)
    game_list: list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'\
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0'\
        'Safari/537.36'
    }

    for games_page_url in games_page_urls:
        try:
            page = requests.get(url=games_page_url, headers=headers)
            page.raise_for_status()
            html = bs(page.content, 'html.parser')
            game_cells = html.find_all('td', {'class':"game"})
            for game_cell in game_cells:
                game_title = game_cell.find('a')
                if game_title:
                    game_list.append(game_title.text)
        except Exception as e:
            print(f'Error fetching {games_page_url}: {e}')
            continue
    
    return game_list

# with open('file.txt', 'w') as file:
#     for game in game_list:
#         try:
#             file.write(game + '\n')
#         except:
#             print(f'Error writing {game} into file')
