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
from aiogram.filters import BaseFilter


async def sturtup_answer(bot: Bot):
    """Bu funksiya bot ishga tushganda ishlaydi"""
    await bot.send_message(chat_id=2132289405, text="Bot ishga tushdi!👌")

TOKEN = "6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk"


dp = Dispatcher()
ADMINS = [2132289405]


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMINS


@dp.message(Command("start"))
async def start_handler(message: Message):
    """
    Foydalanuvchi start bosganida unga salom qaytaradi
    """
    await message.answer(
        f"Salom {message.from_user.first_name}!"
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


async def main():
    """
    Main methodi botni ishga tushiradi
    """
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="data", description="Sizning ma'lumotlaringizni ko'rsatish"),
        BotCommand(command="ism", description="Sizning ismingizni ko'rsatish"),
        BotCommand(command="yosh", description="Sizning ma'lumotlaringizni ko'rsatish"),
        BotCommand(command="manzil", description="Sizning ma'lumotlaringizni ko'rsatish"),
        BotCommand(command="admin", description="Adminni korish"),




    ]
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(commands)

    dp.startup.register(sturtup_answer)
    await dp.start_polling(bot)


@dp.message(Command("admin"), IsAdmin())
async def admin_handler(message: Message):
    """Ush bu funksiya adminemas odamga siz admin siz deb habar yuboradi"""

    await message.answer("👌Siz admin siz👌")


@dp.message(Command("admin"))
async def not_admin(message: Message):
    """Ush bu funksiya adminemas odamga siz admin emassiz deb habar yuboradi"""
    await message.answer("Siz admin emassiz")

if __name__ == "__main__":
    run(main())
