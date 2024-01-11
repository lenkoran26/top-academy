import requests
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message
from scripts.get_weather import get_weather_spb
from scripts.get_course import get_course
from scripts.get_vacancy_python import get_random_vacancy

TOKEN_API: str = "6965973018:AAGgRnKIoelhshJsqInMKwg2IWpq9MaQdjE"

# создаем объекты бота и диспетчера
bot: Bot = Bot(token=TOKEN_API)
dp: Dispatcher = Dispatcher()

# Этот хендлер будет срабатывать на команду /start
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет\n Спроси меня о чем-нибудь')

# Этот хендлер будет срабатывать на команду /weather
@dp.message(Command(commands=['weather']))
async def process_weather_command(message: Message):
    weather = get_weather_spb()
    date = weather[0]
    pass

# Этот хендлер будет срабатывать на команду /course
@dp.message(Command(commands=['course']))
async def process_course_command(message: Message):
    courses = get_course()
    pass

# Этот хендлер будет срабатывать на команду /python
@dp.message(Command(commands=['python']))
async def process_python_command(message: Message):
    vacancies = get_random_vacancy()
    pass

# Этот хендлер будет срабатывать на команду /help
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Этот бот умеет выдавать информацию:\nо погоде,\nкурсе валют,\nвакансиях python')

# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)

@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply(message.sticker.emoji)

@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)




dp.run_polling(bot)
