import random
from youtubesearchpython import VideosSearch

class RandomVideo:
    name = ""
    length = ""
    link = ""
    stats = ""

def get_random_video():
    #ключевые слова для поиска(выбираются рандомно)
    searchQuery = ["майнкрафт", "обзор", "влог", "дота", "аниме", "манга", "дорама", "гайд", "пересказ", "интервью", "стендап", "сериал"]
    searchQuery = random.choice(searchQuery)
    print(searchQuery)
    random_video_number = random.randint(0, 9)

    videosSearch = VideosSearch(searchQuery, limit = 10, region="ru", language="ru")

    video = RandomVideo()
    video.name = videosSearch.result()["result"][random_video_number]["title"]
    video.length = videosSearch.result()["result"][random_video_number]["duration"]
    video.link = videosSearch.result()["result"][random_video_number]["link"]
    video.stats = f"{videosSearch.result()["result"][random_video_number]["publishedTime"]} | {videosSearch.result()["result"][random_video_number]["viewCount"]["short"]}"

    return video