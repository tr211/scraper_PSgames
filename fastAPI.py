import os
from fastapi import FastAPI
import uvicorn
from pars_countri import json_to_dict ,scraperPS, Game
from names_registry import check_all_exist_ps4_games


app = FastAPI()
pythonfile = 'ps_countries.json'
fi = os.path.abspath(pythonfile)

@app.get('/show_table/{game_name}')
def show_table(game_name)->list[Game]:
    countries = json_to_dict(fi)
    list_of_games = scraperPS(game_name, countries)

    return list_of_games


@app.get('/list_exist_ps4_games')
def list_exist_ps4_games():
    game_list = check_all_exist_ps4_games()
    
    return game_list 



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)