from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import users, get_user_ball
from states import get_user_realy_name
from keyboards import main_menu


def register_user(user_id: str, reffer_id=None):
    users[user_id] = {
        "reffer_id": reffer_id,
        "user_realy_name": None,
        "flag": True
    }


async def start_command_answer(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    text = message.text.strip()

    args = text.split(maxsplit=1)

    if user_id in users:
        if users[user_id].get("user_realy_name"):
            await message.answer("Asosiy menyudasiz!", reply_markup=main_menu)
        else:
            await message.answer("Ism-familyangizni kiriting.")
            await state.set_state(get_user_realy_name.name)
        return

    reffer_id = None
    if len(args) == 2 and args[1].isdigit():
        if args[1] == user_id:
            await message.answer("Ozingizga referal bola olmaysiz!")
            return
        reffer_id = args[1]

    print(f"reffer_id: {reffer_id}")
    register_user(user_id, reffer_id)

    await state.set_state(get_user_realy_name.name)
    await message.answer("Menga haqiqiy ismingizni kiriting.")


async def get_user_realy_name_answer(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)

    users[user_id]["user_realy_name"] = message.text.strip()

    await message.answer(
        f"{message.text}sizni eslab qoldim ✅",
        reply_markup=main_menu
    )
    await state.clear()


async def get_ref_link_answer(message: Message):
    user_id = str(message.from_user.id)

    if user_id not in users:
        register_user(user_id)
        await message.answer("Avval ismingizni kiriting.")
        return

    ref_link = f"https://t.me/amalyot1_bot?start={user_id}"
    await message.answer(
        f"Sizning referal havolangiz:\n\n{ref_link}"
    )


async def get_user_ball_answer(message: Message):
    user_id = str(message.from_user.id)

    if user_id not in users:
        register_user(user_id)
        await message.answer("Avval ismingizni kiriting.")
        return

    ball = get_user_ball(user_id)
    await message.answer(f"Sizning ballingiz: {ball} ball")
