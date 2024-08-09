from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import asyncio

async def searcher_name_games(game: str) -> list:
    game = game.replace(' ', '+')
    search_game = game.lower()
    apostrophe = ["'", "®"]
    for symbol in apostrophe:
        search_game = search_game.replace(symbol, '')

    # Setup Selenium WebDriver
    options = Options()
    options.headless = True  # Run in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    url = f'https://www.playstation.com/en-us/search/?q={search_game}&category=games'
    driver.get(url)
    
    # Wait for the page to load
    await asyncio.sleep(5)
    
    # Extract the game titles
    game_name_list = []
    try:
        title_elements = driver.find_elements(By.CLASS_NAME, 'search-results__tile__content-title')
        for title_element in title_elements:
            title = title_element.text.strip()
            if title:
                game_name_list.append(title)
    except Exception as e:
        print(f'Error extracting titles: {e}')
    finally:
        driver.quit()

    return game_name_list
