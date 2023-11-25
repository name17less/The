from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc import Test


async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n\n"
                         "Вопрос 1.\n"
                         "Арбуз или дыня?")

    await Test.Q1.set()


async def answer_Q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("Вопрос 2.\n"
                         "Пики точёные или хуи дрочёные?")

    await Test.Q2.set()


async def answer_Q2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer2=answer)

    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    await message.answer("Спасибо за прохождение нашего IQ теста.")
    await message.answer(f"Ваши ответы:\n"
                         f"Ответ 1: {answer1}\n"
                         f"Ответ 2: {answer2}")

    await state.reset_state(with_data=False)


def register_test(dp: Dispatcher):
    dp.register_message_handler(enter_test, Command("Test"))
    dp.register_message_handler(answer_Q1, state=Test.Q1)
    dp.register_message_handler(answer_Q2, state=Test.Q2)
