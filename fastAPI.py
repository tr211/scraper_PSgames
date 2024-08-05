from fastapi import FastAPI
import uvicorn
import ps_store_repository 
import names_registry
import file_manager
import test_func


app = FastAPI()

@app.get('/country-prices/{game_name}')
def country_prices(game_name)->list[ps_store_repository.Game]:
    language_to_country = file_manager.read_countries_languages_file()
    list_of_prices = ps_store_repository.find_ps4_prices(game_name, language_to_country)
    return list_of_prices

@app.get('/ps4-names')
def ps4_games_names()->list[str]:
    names_list = names_registry.get_all_ps4_games()
    return names_list 

@app.get('/test/{game}')
def test_funk(game)->list[dict]:
    test_d = test_func.read_countries_languages_file()
    game_info_df = test_func.find_ps4_prices(game, test_d)
    return game_info_df

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)