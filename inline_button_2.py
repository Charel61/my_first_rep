from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message


API_TOKEM: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'
#  https://api.telegram.org/6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg/getUpdates

bot: Bot = Bot(token=API_TOKEM)
dp: Dispatcher = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed')

big_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed')
# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],[big_button_2]])

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    print(message.json(indent=4, exclude_none=True))
    await message.answer(text='Это инлайн-кнопки. Нажми на любую!', reply_markup=keyboard)

@dp.callback_query(Text(text=['big_button_1_pressed']))
async def process_button_1_press(callback: CallbackQuery):
    print(callback.json(indent=4, exclude_none=True))
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup)
    await callback.answer()

@dp.callback_query(Text(text=['big_button_2_pressed']))
async def process_button_2_press(callback: CallbackQuery):
    print(callback.json(indent=4, exclude_none=True))
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup)
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
