from aiogram.dispatcher.filters import Command,Text
from bot import BotDB
from loader import dp
from aiogram.types import Message,ReplyKeyboardRemove
from tgbot.keyboards.inline import choice

@dp.message_handler(Command("start"))
async def star(message: Message):
    text = """Привет, молодой инвестор!

Теперь в Вашем распоряжении есть я, интерактивный помощник!

Что я умею?
1. Помочь Вам собрать портфель акций!
2. Присылать Вам каждый день уведомление с информацией об изменениях и показывать, сколько Вы заработали или потеряли.
3. Вычислять процентные изменения стоимости акций за определённый промежуток времени.
4. Выводить графики изменений акций нужной компании

На этом пока всё!

Но Вы можете оставлять
свои предложения
и пожелания по
ссылке
ниже:
@kartuzova_elizzers

Ты автоматически подписался на ежедневную рассылку полезных уведомлений, чтобы её отключить, нажми /off

Чтобы перейти в главное меню, пропиши /menu"""
    await message.answer(text=text)

@dp.message_handler(Command("menu"))
async def show_items(message: Message):
    text = """*Выберите из Главного Меню, интересующий Вас, раздел*"""
    await message.answer(text=text,reply_markup=choice,parse_mode="Markdown")
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
        BotDB.add_notifications(message.from_user.id)

@dp.message_handler(Command("on"))
async def notif (message:Message):
    await message.answer("Вы подписались на ежедневную рассылку")
    BotDB.update_notifications(user_id=message.from_user.id,check=False)

@dp.message_handler(Command("off"))
async def notif (message:Message):
    await message.answer("Вы отписались от ежедневной рассылки, чтобы возабновить подписку, используйте "
                         "команду /on")
    BotDB.update_notifications(user_id=message.from_user.id)

# @dp.message_handler(Command("menu"))
# async def show_menu(message:Message):
#     await message.answer("Вы находитесь на главной странице бота",reply_markup=menu)

@dp.message_handler(Text(equals=["Профиль","Информация о боте","Портфель"]))
async def Main_menu(message: Message):
    await message.answer(f"Вы находитесь в {message.text}",reply_markup=ReplyKeyboardRemove())
