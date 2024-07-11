import os
from fastapi import FastAPI
import uvicorn
from pars_countri import json_to_dict ,scraperPS, Game

app = FastAPI()
pythonfile = 'all_lang_countries.json'
fi = os.path.abspath(pythonfile)

@app.get('/show_table/{game_name}')
def show_table(game_name)->list[Game]:
    countries = json_to_dict(fi)
    list_of_games = scraperPS(game_name, countries)
    scrap_dicts = [game_name.dict() for game_name in list_of_games]

    return list_of_games

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)