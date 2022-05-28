import asyncio
import logging
from api import apii,grapf
from loader import dp,bot,config
from datetime import date, timedelta
import aioschedule
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.middlewares.db import DbMiddleware

from creat_db import BotDB
#Artem
BotDB = BotDB("bot.db")

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    # register_user(dp)

    # register_echo(dp)

async def noon_print():
    stocks_name = BotDB.get_stock()
    users = BotDB.get_users()
    today = date.today() - timedelta(days=1)
    slovar = {}
    mass_api = []
    for i in stocks_name:
        mass_api = apii(i[0],today,today,check=False)
        slovar[i[0]] = mass_api
    for i in slovar.keys():
        a = BotDB.push(i)
        for j in a:
            state = BotDB.check_notifications(j[0])
            if(state == 1):
                res = (slovar[i][2] - slovar[i][1])*j[1]
                result =float("%.3f" % res)
                if(result > 0):
                    await bot.send_message(chat_id=j[0],text=f"Акции {i} за прошлый день выросли на {slovar[i][0]}%\n"
                                                             f"И вы на этом заработали {result}")
                else:
                    result = result*(-1)
                    proc = float(slovar[i][0])*(-1)
                    await bot.send_message(chat_id=j[0], text=f"Акции {i} за прошлый день упали на {proc}%\n"
                                                              f"И вы из-за этого потеряли {result}")

async def scheduler():
    aioschedule.every(1).minute.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
async def on_startup():
    asyncio.create_task(scheduler())

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    # await on_startup()
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)


    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
