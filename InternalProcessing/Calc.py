import requests
from bs4 import BeautifulSoup
import webbrowser

MAX_PKM_NUMBER = 892
POKEDEX_NUMBER_URL = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk="
POKEDEX_NAME_URL = "https://www.pokemon.com/es/pokedex/"


def calculate_pokemon(day, month, name):
    pkm_number = day * month * len(name)
    while pkm_number > MAX_PKM_NUMBER:
        pkm_number //= 2

    return pkm_number


def get_pokemon_from_pokedex(pkm_number):
    response = requests.get(POKEDEX_NUMBER_URL + str(pkm_number))
    pkm_name = ""

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        pkm_name_tag = soup.findAll("span", {"class": "mini"})[0]
        pkm_name = pkm_name_tag.get_text()
    else:
        print(f"ERROR: Status code {response.status_code}")

    return pkm_name


def open_pokedex(pkm_name):
    if pkm_name:
        webbrowser.open(POKEDEX_NAME_URL + pkm_name.lower())
    else:
        print("ERROR: Invalid pokemon name")
