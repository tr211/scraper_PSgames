import json
import os

def read_countries_languages_file()-> dict:
    file_path = os.path.abspath('ps_countries.json')
    with open(file_path, 'r') as countries_dict:
      return json.load(countries_dict)
