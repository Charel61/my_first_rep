from aiogram import Bot, Dispatcher
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text
from aiogram.exceptions import TelegramBadRequest

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# BOT_TOKEN = 'BOT TOKEN HERE'
BOT_TOKEN = '6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()
LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAICRGQ1R-EwAuSiCZ_p1jKIyj6kGsXEAAJWxDEb0ZioSaOm8zeUa9kEAQADAgADcwADLwQ',
    'photo_id2': 'AgACAgIAAxkBAAICRWQ1SYS0g_L0jkAjcE7_TUJrcP2dAAJhxDEb0ZioSeDoU6uCrJtiAQADAgADcwADLwQ',
    'voice_id1': 'AwACAgIAAxkBAAICTGQ1S26ZQs6sKEADnzZe_i8tb_M9AAJ-JwAC0ZioSSyXeiJ1AYoAAS8E',
    'voice_id2': 'AwACAgIAAxkBAAICTWQ1S4uegfyZlZbj1wndCZGOu1BfAAKAJwAC0ZioSX3IxGgKyh0wLwQ',
    'audio_id1': 'CQACAgIAAxkBAAICRmQ1Sjtw867hltgqfxh7W3wWWynTAAJxJwAC0ZioSXW0qr4jJEd2LwQ',
    'audio_id2': 'CQACAgIAAxkBAAICR2Q1Smxi81lm20AoEZcAAaFOYxzQZwACgyYAAkZhIUlWyUZn3-RbWC8E',
    'document_id1': 'BQACAgIAAxkBAAICYWQ1W2H1SyPCaW5YjBmBcfLC3htOAAKpKwAC0ZioSS-jHvXQHLjlLwQ',
    'document_id2': 'BQACAgIAAxkBAAICZmQ1W_mxx0c61UFFk-ky0IEdsEFjAAKuKwAC0ZioSYenCxoFEhCcLwQ',
    'video_id1': 'BAACAgIAAxkBAAICa2Q1XLfuRdOrBmpexgYnrO929FahAAJ4JwAC0ZioSUR6zqcttCRsLwQ',
    'video_id2': 'BAACAgIAAxkBAAICcGQ1XX5cHzt8r-R7VzqUqXwwSfZfAAJ7JwAC0ZioSVP-IM_qHC9oLwQ',
    }


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder =InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton]=[]
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON[button] if button in LEXICON
            else button,
            callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text,callback_data=button))


    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'video')
    await message.answer_video(
                        video=LEXICON['video_id1'],
                        caption='Это видео 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'video')
    try:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaVideo(
                                media=LEXICON['video_id2'],
                                caption='Это видео 2'),
                        reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaVideo(
                                media=LEXICON['video_id1'],
                                caption='Это видео 1'),
                        reply_markup=markup)


@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(text='Do not understand')


if __name__=='__main__':
    dp.run_polling(bot)
