import re
from fastapi import FastAPI
import uvicorn
import ps_store_repository 
import names_registry
import file_manager

app = FastAPI()

@app.get('/country-prices/{game_name}')
def country_prices(game_name)->list[ps_store_repository.Game]:
    language_to_country = file_manager.read_countries_languages_file()
    list_of_prices = ps_store_repository.find_ps4_prices(game_name, language_to_country)
    return list_of_prices

@app.get('/ps4-names')
def ps4_games_names() -> list[str]:
    names_list = names_registry.get_all_ps4_games()
    if isinstance(names_list, list):
        game_list_clear = [re.sub(r'\([^()]*\)', '', name).strip() for name in names_list]
        return game_list_clear
    return []
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)