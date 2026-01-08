import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "5891489513:AAHUDQ1L4ZQajLUtWM_3-ulNWhncCbCBf7g"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    name = message.from_user.full_name
    await message.answer(f"Hello, {name}")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        chat_id = message.chat.id
        await message.send_copy(chat_id=chat_id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    """
    Running bot
    """
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
