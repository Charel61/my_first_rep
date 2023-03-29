from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_comand(message: Message):
    print(message.json(indent=4,exclude_none=True))
    await message.answer('Привет!\n  Меня зовут Эхо-бот!\nНапиши мне что-нибудь')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь. В ответ я пришлю тебе твое сообщение')

# async def send_photo_echo(message: Message):
#     print(message)
#     await message.reply_photo(message.photo[0].file_id)

# async def send_audio_echo(message: Message):
#     print(message)
#     await message.answer_audio(message.audio.file_id)

# dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# dp.message.register(send_audio_echo, F.content_type == ContentType.AUDIO)

@dp.message(F.voice)
async def process_sent_voice(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришло голосовое
    await message.answer(text='Вы прислали голосовое сообщение!')


@dp.message()
async def send_echo(message: Message):
    print(message.json(indent=4,exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.reply(text='Данный тип апдейтов не поддерживается методом  send_copy')



if __name__ == '__main__':
    dp.run_polling(bot)
