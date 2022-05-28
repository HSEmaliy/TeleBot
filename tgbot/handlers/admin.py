from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart,AdminFilter
from loader import config



async def admin_start(message: Message):
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, CommandStart(),user_id=config.tg_bot.admin_ids, state="*")
