from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from ggttt import create_inline_kb


BUTTONS: dict[str, str] = {'btn_1': '1',
                           'btn_2': '2',
                           'btn_3': '3',
                           'btn_4': '4',
                           'btn_5': '5'}


API_TOKEM: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'
#  https://api.telegram.org/6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg/getUpdates

bot: Bot = Bot(token=API_TOKEM)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(3, 'but_1', 'but_2', 'but_3', 'but_4', 'but_5', last_btn='Последняя кнопка')
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
