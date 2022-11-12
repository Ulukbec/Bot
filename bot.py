from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.utils import executor

token = '5653597708:AAE_4NwehPSBGSF4RnSjfeYwIuCf_H-KhU8'
bot = Bot(token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    this_bot = await bot.get_me()
    await bot.send_message(message.chat.id, f'Вас приветствует {this_bot.first_name}')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.chat.id,
                           '/my_info - выводит ифромаццию о вас\n/download_photo - скачивает изображение профиля\n'
                           '/show_movies - выводит список фильмов и сайт с этими фильмами\n'
                           '/send_my_info” - пользователь пишет свое имя, фамилия, возраст, чем занимается и список '
                           'любимых фильмов или сериалов и бот группирует это в сообщение')


@dp.message_handler(commands=['my_info'])
async def my_info(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'{message.from_user.id} {message.from_user.first_name}  {message.from_user.last_name}')


@dp.message_handler(commands=['download_photo'])
async def download_photo(message: types.Message):
    photos = await bot.get_user_profile_photos(message.from_user.id)
    await bot.get_file(photos.photos[0][0].file_id)
    await bot.send_photo(message.chat.id, photos.photos[0][0].file_id)


@dp.message_handler(commands=['show_movies'])
async def show_movies(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Побег из Шоушенка\nЗеленая миля\nСписок Шиндлера\nhttps://www.kinopoisk.ru/lists/movies/top500/')


@dp.message_handler(commands=['send_my_info'])
async def send_my_info(message: types.Message):
    arguments = message.text.split('\n')
    print(arguments)
    await bot.send_message(message.chat.id, f'1. Вас зовут {arguments[1]} {arguments[2]}\n'
                                            f'2. Вам {arguments[3]} лет\n'
                                            f'3. Вы занимаетесь {arguments[4]}\n'
                                            f'4. Список ваших любимых сериалов и фильмов {arguments[5]}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
