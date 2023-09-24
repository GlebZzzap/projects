from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import MediaGroup
import config

bot = Bot(config.bot_token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True)
    markup.add(types.KeyboardButton("Начать работу!"))
    await message.answer("Привет! Я - бот, который поможет тебе сделать заказ в нашем магазине!", reply_markup= markup)

@dp.message_handler()
async def choose(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('1-1.jpg'),'Хуйня')
    media.attach_photo(types.InputFile('1-2.jpg'))
    media.attach_photo(types.InputFile('1-3.jpg'))

    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup1.row(types.KeyboardButton("Заказать"), types.KeyboardButton("Поддержка"))
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup2.row(types.KeyboardButton("Из наличия"), types.KeyboardButton("На заказ"))
    if message.text.lower() == "начать работу!":
        await message.answer("Выбери, что тебе необходимо", reply_markup=markup1)
    elif message.text.lower() == "заказать":
        await message.answer("Хорошо, теперь выбери пожалуйста, чего именно ты хочешь?", reply_markup=markup2)
    elif message.text.lower() == "поддержка":
        await message.answer(f'Подождите пожалуйста. {message.from_user.id}')
    elif message.text.lower() == "из наличия":
        await bot.send_media_group(message.chat.id, media)


executor.start_polling(dp)