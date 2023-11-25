from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from tgbot.keyboards.inline import Keyboard


async def get_inline(message: types.Message):
    await message.answer("Тест InlineKeyboard прямо здесь", reply_markup=Keyboard)


async def get_sheesh(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали sheeeeeshki")


async def get_peesh(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали peeeeeeeshki")


async def get_cancel(call: types.CallbackQuery):
    await call.answer("Cancel", show_alert=True)
    await call.message.edit_reply_markup()


def register_inline(dp: Dispatcher):
    dp.register_message_handler(get_inline, Command("inlineshit"))
    dp.register_callback_query_handler(get_sheesh, text="sheesh")
    dp.register_callback_query_handler(get_peesh, text="peesh")
    dp.register_callback_query_handler(get_cancel, text="cancel")
