from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


COMPETITION_LINK = 'https://c633-178-34-151-83.ngrok-free.app/split_compare/?user_id_1=416&user_id_2=1829&event_id=6&competition_date=2024-07-16'
# COMPETITION_LINK = 'https://matchtv.ru'
BOT_TOKEN = '6094114160:AAHWebApBjhj-42-kP_yrUR7agD3x2JoeCY'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types. Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url=COMPETITION_LINK)))

    await message.answer('Hello, split bot', reply_markup=markup)

executor.start_polling(dp)