from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.filters import Command

from tgbot.config import load_config
from tgbot.misc.items import Tesla_CyberSex, Sanya


async def get_shop(message: types.Message):
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    await bot.send_invoice(message.from_user.id,
                           **Tesla_CyberSex.generate_invoice(),
                           payload="123456"
                           )
    await bot.send_invoice(message.from_user.id,
                           **Sanya.generate_invoice(),
                           payload="654321")


async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                  ok=True)
    await bot.send_message(chat_id=query.from_user.id, text="Спасибо за покупку, додик")


def register_payments(dp: Dispatcher):
    dp.register_message_handler(get_shop, Command("shop"))
    dp.register_pre_checkout_query_handler(process_pre_checkout_query)