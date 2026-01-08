"""
Topshiriq passport bot yozing

1. /start kelsa Salomlashadi
2. /passport kelsa passport malumot qaytaradi
"""

from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = "6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk"

dp = Dispatcher()


async def sturtup_answer(bot: Bot):
    """
    Bot ishga tushganda xabar beruvchi funksiya
    """
    await bot.send_message(chat_id=2132289405, text="Bot ishga tushdi!👌")


@dp.message(CommandStart())
async def start_handler(message: Message):
    """
    Foydalanuvchi start bosganida unga
    Assalomu alaykum deb qaytarauvchi funksiya
    """
    await message.answer(
        f"Assalomu alaykum {message.from_user.first_name}"
    )


@dp.message(Command("passport"))
async def passport_handler(message: Message):
    """
    Ushbu funksiya agar foydalanuvchi /passport commandini bersa
    unga passport malumotlarini qaytaramiz
    """
    passport_info = (
        "📄 Passport malumotlari:\n"
        "Ism: Azizbek\n"
        "Familiya: Anvarbekov\n"
        "Seriya: AA1234567\n"
        "Tugilgan sana: 01.01.2000"
    )
    await message.answer(passport_info)


async def main():
    """
    Main methodi botni ishga tushiradi
    """
    bot = Bot(token=TOKEN)
    dp.startup.register(sturtup_answer)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
