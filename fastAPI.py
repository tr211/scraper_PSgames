from fastapi import FastAPI
import uvicorn
from pars_countri import scraperPS

app = FastAPI()

@app.get('/show_table/{game_name}')
def show_table(game_name):
    list_of_games = scraperPS(game_name)
    scrap_dicts = [game_name.dict() for game_name in list_of_games]

    return scrap_dicts

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)