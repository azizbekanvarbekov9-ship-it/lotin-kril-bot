import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def start_handler(message: Message):
    await message.answer("Menga rasm yuboring 🙂")


async def photo_echo(message: Message):
    await message.answer_photo(
        photo=message.photo[-1].file_id
    )


async def main():
    dp.message.register(start_handler, CommandStart())
    dp.message.register(photo_echo, F.photo)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
