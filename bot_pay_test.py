from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка хуй жопа', 'Покупка хуй трахать жопа', 'invoice', config.pay_token, 'RUB', [types.LabeledPrice('Покупка хуй жопа', 1*100)])

@dp.message_handler(content_types= types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f'Success: {message.successful_payment.order_info}')

executor.start_polling(dp)