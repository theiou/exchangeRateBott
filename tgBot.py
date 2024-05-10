import asyncio
import logging
import sys, random
import anime, kinosearch, youtube

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7075552558:AAG_fi40phBF1rk1rJEnBE0T03ULmZA-Xzk"

dp= Dispatcher()

keyboard_main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Рандом")], 
                                              [KeyboardButton(text="Рандом фильм"), KeyboardButton(text="Рандом аниме"), KeyboardButton(text="Рандом видео на YT")]],
                                              resize_keyboard=True)

@dp.message(F.text == "Рандом")
async def random_roll_handler(message: Message) -> None:
    all_content = ["youtube", "anilibria", "kinopoisk"] #источники контента
    random_content = random.choice(all_content)
    
    match random_content:
        case "kinopoisk":
            await random_film_handler(message)
        case "anilibria":
            await random_anime_handler(message)
        case "youtube":
            await random_youtube_handler(message)

@dp.message(F.text == "Рандом фильм")
async def random_film_handler(message: Message) -> None:
    film = kinosearch.get_random_content()
    await message.answer(film.name  + "\n" + film.length + "\n" + film.description)
    await message.answer_photo(film.poster)

@dp.message(F.text == "Рандом аниме")
async def random_anime_handler(message: Message) -> None:
    anime_random = anime.get_random_anime()
    await message.answer(anime_random.name + "\n" + anime_random.length+ "\n" + anime_random.description)
    await message.answer_photo(anime_random.poster)

@dp.message(F.text == "Рандом видео на YT")
async def random_youtube_handler(message: Message) -> None:
    video = youtube.get_random_video()
    await message.answer(video.name + "\n" + video.length + "\n" + video.stats)
    await message.answer(video.link)
    
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Что ищем?", reply_markup=keyboard_main)   
    
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

