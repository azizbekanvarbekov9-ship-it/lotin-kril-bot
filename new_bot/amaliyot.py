from aiogram import Bot, Dispatcher
from asyncio import run


dp = Dispatcher()


async def sturtup_answer(bot: Bot):
    await bot.send_message(chat_id=2132289405, text="Bot ishga tushdi!👌")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=2132289405, text="Bot ishdan tohtadi😥")
