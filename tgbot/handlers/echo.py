import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    text = "Упс...Неизвестная команда. Попробуйте ещё раз.\n" \
           "/menu - Перейти в раздел \"Главное меню\""
    await message.answer(text=text)
