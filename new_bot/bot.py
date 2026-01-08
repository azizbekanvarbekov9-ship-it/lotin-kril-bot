from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from asyncio import run
import functions
import states

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(2132289405, "Bot ishga tushdi👌")


async def shutdown_answer(bot: Bot):
    await bot.send_message(2132289405, "Bot ishdan to'xtadi")


async def start():
    # bot internal logic
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    # user handler logics
    dp.message.register(functions.start_command_answer, CommandStart())
    dp.message.register(functions.get_user_realy_name_answer, states.get_user_realy_name.name)
    dp.message.register(functions.get_ref_link_answer, F.text == "Referal havola")
    dp.message.register(functions.get_user_ball_answer, F.text == "Mening ballarim")

    bot = Bot("6143382079:AAF4CHF8nu1fhWxr5ej6KY1UZfNebePd7Dk")
    await dp.start_polling(bot, polling_timeout=1)

run(start())
