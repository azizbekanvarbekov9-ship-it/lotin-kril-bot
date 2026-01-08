import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = ""

dp = Dispatcher()


@dp.message(CommandStart())
async def son_kirit(message: Message):
    """Ushbu funksiya foydalanuvchidan son kiritishini yozadi"""
    await message.answer("Salom!Menga hohlagan son yuboring, men uni 2 ga kopaytiraman.")


@dp.message()
async def tekshirish(message: Message):
    """Ushbu funksiya foydalanuvchidan sonni olib uni 2 ga kopaytirib beradi"""
    if message.text.isdigit():
        number = int(message.text)
        result = number * 2
        await message.answer(f"Natija: {result} (mana sizning soningi)")
    else:
        await message.answer("Siz ning siningiz hato boshqa son yuboring")


async def finish():
    """Ushbu funksiya natijani chiqaradi"""
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(finish())
