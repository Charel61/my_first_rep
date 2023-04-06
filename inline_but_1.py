from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


API_TOKEM: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'


bot: Bot = Bot(token=API_TOKEM)
dp: Dispatcher = Dispatcher()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',url='https://stepik.org/120924')

url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Документация Telegram Bot API',url='https://core.telegram.org/bots/api')



keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[url_button_1],[url_button_2]])

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='о инлайн-кнопки с параметром "url"', reply_markup=keyboard)



if __name__ == '__main__':
    dp.run_polling(bot)
