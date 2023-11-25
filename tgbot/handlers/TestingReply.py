from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.reply import Keyboard


async def get_reply(message: types.Message):
    await message.answer(text="Los Pinguinos"
                              "ne la van a Mascar",
                         reply_markup=Keyboard)


async def get_Kawazaki(message: types.Message):
    await message.answer_animation("CgACAgQAAxkBAAOhZWHtFSHKgJSj4zBS6LPsDvTuW9QAAlIEAALtPcxSB5BAnV9iysszBA")


async def get_Cago(message: types.Message):
    await message.answer_animation("CgACAgQAAxkBAAOfZWHs3AtVJNITdhXeMOzH8kWLnbAAArAEAAIWt4VScYpzr4gha3kzBA")


async def get_Krico(message: types.Message):
    await message.answer_animation("CgACAgQAAxkBAAOgZWHs99128H_zaDqIPsQcPdCzOysAAr4EAAJqyoRS88KUfVz-e_ozBA")


async def get_Estriper(message: types.Message):
    await message.answer_animation(animation="CgACAgQAAxkBAAOYZWHskq_vUPlh_NHK7h3OGmK-EqYAAuIEAAKT0sVSI4FoWmIXDDszBA")


async def get_cancel(message: types.Message):
    await message.answer(text="really pizdec", reply_markup=ReplyKeyboardRemove())


def register_reply(dp: Dispatcher):
    dp.register_message_handler(get_reply, Command("menu"))
    dp.register_message_handler(get_Kawazaki, text="Kawazaki")
    dp.register_message_handler(get_Cago, text="Cago")
    dp.register_message_handler(get_Krico, text="Krico")
    dp.register_message_handler(get_Estriper, text="Estriper")
    dp.register_message_handler(get_cancel, text="OMAGQD")

