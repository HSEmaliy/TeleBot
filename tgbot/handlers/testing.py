from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types

from tgbot.states import Test



@dp.message_handler(text="/test")
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестированиею\n"
                         "Вопрос №1. \n\n"
                         "Сколько будет 1 + 1?\n")

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def anser_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    if answer == "2":
        await message.answer("Правильно!\nВопрос 2\n"
                            "Сколько будет 2 + 2?\n")
    else:
        await message.answer("Ответ неверный!\nВопрос 2\n"
                             "Сколько будет 2 + 2?\n")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def anser_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ответы")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    await state.finish()



