import requests

class RandomAnime:
    name = ""
    length = ""
    description = ""
    poster = ""

url = f"https://api.anilibria.tv/v3/title/random"


def get_random_anime():
    response = requests.get(url)
    response = response.json()
    anime = RandomAnime()
    anime.name = response['names']['ru']
    anime.length = response["type"]["full_string"]
    anime.description = response["description"]
    anime.poster = "https://www.anilibria.tv" + response["posters"]["original"]["url"]
    return anime


