"""
Topshiriq

1. Foydalanuvchi start bosganida u bilan salomlashsin
2. Agar foydalanuvchi /data commandini bersa
    unga o'zini malumotlarini qaytarsin
    - Ismi
    - Familiyasi
    - Maktabi
    - Yoshi
"""
from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import BotCommand


async def sturtup_answer(bot: Bot):
    """Bu funksiya bot ishga tushganda ishlaydi"""
    await bot.send_message(chat_id=2132289405, text="Bot ishga tushdi!👌")

TOKEN = "6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk"


dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    """
    Foydalanuvchi start bosganida unga salom qaytaradi
    """
    await message.answer(
        f"Salom {message.from_user.first_name}! 1-Ism, 2-yosh keyin manzilingizni kiriting"
    )


@dp.message(Command("data"))
async def data_handler(message: Message):
    """
    Foydalanuvchi /data commandini yuborganda ishlaydi
    """
    data_info = (
        "Ism: Azizbek\n"
        "Familiya: Anvarbekov\n"
        "Maktabi: 6-Maktab\n"
        "Yoshi: 13 yosh"
    )
    await message.answer(data_info)


@dp.message(Command("ism"))
async def data_handler(message: Message):
    """
    Foydalanuvchi ism commandini yuborganda ishlaydi
    """
    data_info = (
        "Ism: Azizbek\n"
    )
    await message.answer(data_info)


@dp.message(Command("yosh"))
async def data_handler(message: Message):
    """
    Foydalanuvchi ism commandini yuborganda ishlaydi
    """
    data_info = (
        "yosh: 13\n"
    )
    await message.answer(data_info)


@dp.message(Command("manzil"))
async def data_handler(message: Message):
    """
    Foydalanuvchi ism commandini yuborganda ishlaydi
    """
    data_info = (
        "Manzil: Andjan\n"
    )
    await message.answer(data_info)


async def main():
    """
    Main methodi botni ishga tushiradi
    """
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/data", description="Sizning ma'lumotlaringizni ko'rsatish"),
        BotCommand(command="/ism", description="Sizning ismingizni ko'rsatish"),
        BotCommand(command="/yosh", description="Sizni yoshingizni korsa tadi"),
        BotCommand(command="/manzil", description="Sizning manzilingizni ko'rsatish"),



    ]
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(commands)

    dp.startup.register(sturtup_answer)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
