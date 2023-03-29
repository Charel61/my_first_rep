from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_comand(messge: Message):
    await messge.answer('Привет!\n  Меня зовут Эхо-бот!\nНапиши мне что-нибудь')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь. В ответ я пришлю тебе твое сообщение')

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
