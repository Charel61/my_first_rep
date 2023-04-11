from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

API_TOKEN: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


admin_ids: list[int] = [480772923]
# admin_ids: list[int] = [480772921]

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:

        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


@dp.message()
async def answer_if_mot_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)
