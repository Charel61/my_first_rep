from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, Text
from aiogram.types import Message

API_TOKEN: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()



# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',','').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        else:
            return False


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа

@dp.message(Text(startswith='найди числа', ignore_case=True), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Нашел: {str(", ".join(str(num) for num in numbers))}')

# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисе


@dp.message(Text(startswith='найди числа', ignore_case=True))
async def proccess_of_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')

@dp.message()
async def proccess_somthing_another(message: Message):
    await message.answer(text='OLOLOLO')


if __name__ == '__main__':
    dp.run_polling(bot)
