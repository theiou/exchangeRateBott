import requests

class RandomAnime:
    name = ""
    length = ""
    description = ""
    poster = ""


url = "https://api.kinopoisk.dev/v1.4/movie/random?rating.kp=7-10"

headers = {
    "accept": "application/json",
    "X-API-KEY": "FE4Y8P6-N7F44PZ-J2QJ2T2-S4SFKGE"
}

def get_random_content():
    response = requests.get(url, headers=headers).json()
    film = RandomAnime()
    film.name = response["name"]
    film.length = f"Продолжительность: {response["movieLength"]} минут"
    film.description = response["description"]
    film.poster = response["poster"]["url"]
    return film