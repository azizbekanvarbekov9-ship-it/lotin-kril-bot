from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from asyncio import run

import functions

bot = Bot(token="TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message):
    await functions.menu_chiqar(message)


@dp.message()
async def all_messages(message):
    await functions.tugma_bosildi(message)


async def main():
    await dp.start_polling(bot)

run(main())
