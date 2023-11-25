from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.misc.throttling import rate_limit


@rate_limit(4, key="start")
async def user_start(message: Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
