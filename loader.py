from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from creat_db import BotDB
from tgbot.config import load_config

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
dp = Dispatcher(bot, storage=storage)
bot['config'] = config
cache_rating = {}

BotDB = BotDB("bot.db")