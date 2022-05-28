import logging
import time
import emoji
from tabulate import tabulate
import os
from pathlib import Path
from api import apii,grapf
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.utils.markdown import hlink
from bot import BotDB
from loader import dp,bot
from tgbot.states import Test
from tgbot.keyboards.inline import choice, update, back_portfile, Prof, Info,all_stock1,all_stock2,all_stock3,briefcase,amount_stock,back_to_promotion_menu,API




@dp.callback_query_handler(text_contains="prof")
async def click_prof(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    date = BotDB.get_date(call.from_user.id)[0][0][:10]
    id= emoji.emojize(":smiling_face_with_sunglasses:")
    nik = emoji.emojize(":clown_face:")
    clock = emoji.emojize(":twelve_o’clock:")
    text = f"""
    ------------------------------------------
    Ваш профиль:
    {id}Ваш ID: {call.from_user.id}
    {nik}Ваш Никнейм: @{call.from_user.username}
    {clock}Дата регистрации: {date}
    ------------------------------------------
    """
    await call.message.answer(text=text,reply_markup=Prof)

@dp.callback_query_handler(text_contains="info")
async def click_info(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    i = "xxx969xxx"
    y = "kartuzova_elizzers"
    text2 = f"""Вы перешли в раздел «Инструкции»: 
1.Чтобы подписаться на ежедневную рассылку, напишите в чат /on

2.Чтобы отписаться от ежедневной рассылки, напишите в чат /off

3.Чтобы получить **График** котировок акций, нажмите в **Главном меню**
“ “->”График”,  дальше я попрошу  ввести название компании(правильность ввода компании, можно посмотреть в разделе /menu ->”Портфель”->” Все акции“). Затем введите нужную дату в формате “ГГГГ-ММ-ДД”

4. Чтобы узнать процент изменения акций определенной компании, нажмите в *Главном меню*
“ “->”Процент”,  дальше я попрошу  ввести название компании(правильность ввода компании, можно посмотреть в разделе /menu ->”Портфель”->” Все акции“). Затем введите нужную дату в формате “ГГГГ-ММ-ДД”


*Примечание:* Чтобы добавить в свой портфель акции или удалить их из него, нажмите в **Главном меню** “Портфель”->”Все акции” 

Если у вас возникли какие-то вопросы, на которые вы не наши ответы – пишите моему **Администратору**:
"""
    text = hlink('Мосбиржа','https://www.moex.com/')
    await call.message.answer(text = text2,reply_markup=Info,parse_mode="Markdown")


@dp.callback_query_handler(text="api")
async def click_api(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer("Выберите, что хотите получить\n",
                              reply_markup=API)
    await Test.Q3.set()

@dp.callback_query_handler(text="delete",state=Test.Q8)
async def click_delete(call: CallbackQuery,state: FSMContext):
    await state.reset_state(with_data=False)
    data = await state.get_data()
    current_stock = data.get("answer6")
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer(f"Вы удалили из своего портфеля акции {current_stock} \n",
                              reply_markup=briefcase)
    BotDB.delete_stock(call.from_user.id,current_stock)

@dp.callback_query_handler(text = "back_menu",state=Test.Q3)
async def back_menu(call: CallbackQuery,state: FSMContext):
    await state.reset_state(with_data=False)
    await call.message.delete()
    await call.message.answer("Главное меню\n",reply_markup=choice)


@dp.callback_query_handler(state=Test.Q3,text_contains="api")
async def clic_percent(call: CallbackQuery,state: FSMContext):
    await call.message.delete()
    await call.answer(cache_time=5)
    text = call.data[4:]
    print("text ",text)
    await state.update_data(PercOrGraf=text)
    await call.message.answer("Введите название компании, о которой хотите получить данные\n")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def state3(message: Message, state: FSMContext):
    text = message.text
    print(text)
    await state.update_data(name_comp=text)
    await message.answer("Введите первую дату в формате “ГГГГ-ММ-ДД”\n")
    await Test.next()

@dp.message_handler(state=Test.Q5)
async def state3(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(date1=text)
    await message.answer("Введите вторую дату “ГГГГ-ММ-ДД”\n")
    await Test.next()

@dp.message_handler(state=Test.Q6)
async def state66(message: Message,state: FSMContext):
    # await state.reset_state(with_data=False)
    text = message.text
    await state.update_data(date2=text)
    data = await state.get_data()
    PercOrGraf = data.get("PercOrGraf")
    name_comp = data.get("name_comp")
    date1 = data.get("date1")
    date2 = data.get("date2")
    if(PercOrGraf == "perc"):
        await message.answer("Секундочку, происходит магия...\n")
        a = apii(name_comp, date1, date2)
        if (a == 'TypeError'):
            await state.finish()
            await message.answer("Введите корректно дату\nСкорее всего, в какой-то из дней не было торгов\n"
                                      "Введите название компании о которой хотите получить данные\n",reply_markup=choice)
        elif (a == "KeyError"):
            await state.finish()
            await message.answer("Вы ввели некоректно название компании\n"
                                      "Введите название компании, о которой хотите получить данные\n",reply_markup=choice)
        elif (a == "ErrorDate"):
            await state.finish()
            await message.answer("Первая дата больше второй, введите данные коректно\n"
                                      "Введите название компании, о которой хотите получить данные\n",reply_markup=choice)
        elif (a == "nan"):
            await state.finish()
            await message.answer("Введите корректно дату\nСкорее всего, в какой-то из дней не было торгов\n"
                                      "Введите название компании о которой хотите получить данные\n",reply_markup=choice)
        else:
            await message.answer(f"Результат: {a}")
    else:
        await message.answer("Секундочку, происходит магия...\n")
        a = grapf(name_comp, date1, date2)
        if a == "ErrorDate":
            await state.finish()
            await message.answer("Первая дата больше второй, введите данные коректно\n"
                                 "Введите название компании, о которой хотите получить данные\n", reply_markup=choice)
        elif a == 'TypeError':
            await state.finish()
            await message.answer("Введите корректно дату\nСкорее всего, в какой-то из дней не было торгов\n"
                                      "Введите название компании о которой хотите получить данные\n",reply_markup=choice)
        elif a == "KeyError":
            await state.finish()
            await message.answer("Вы ввели некоректно название компании\n"
                                      "Введите название компании, о которой хотите получить данные\n",reply_markup=choice)
        else:
            patch = Path("PycharmProjectsBot", "page", "myfig.png")
            Photo = InputFile(f'.\page\{name_comp}_{date1}_{date2}.png')
            # photo = open(patch)
            await bot.send_photo(chat_id=message.from_user.id, photo=Photo)
            os.remove(f'.\page\{name_comp}_{date1}_{date2}.png')
            text = """*Выберите из Главного Меню, интересующий Вас, раздел*"""
            await message.answer(text=text, reply_markup=choice, parse_mode="Markdown")
    await state.finish()

@dp.callback_query_handler(text_contains="portf")
async def click_portf(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Вы перешли в раздел \"Портфель\"",
                              reply_markup=briefcase)


@dp.callback_query_handler(text="my_Stock")
async def click_my_Stock(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    text = BotDB.get_stock_user(call.from_user.id)
    await call.message.answer(tabulate(text.items(), headers=['Название компании', 'Кол-во акций'], tablefmt="rst"),
                              reply_markup=back_to_promotion_menu)


@dp.callback_query_handler(text="all_stock")
async def ALL_stock(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer("Здесь Вы можете выбрать, интересующие Вас акции\n",
                              reply_markup=all_stock1)

@dp.callback_query_handler(text="str2")
async def str2(call:CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer(text="Здесь Вы можете выбрать, интересующие Вас акции\n",reply_markup=all_stock2)

@dp.callback_query_handler(text="str3")
async def str2(call:CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer(text="Здесь Вы можете выбрать, интересующие Вас акции\n",reply_markup=all_stock3)

@dp.callback_query_handler(text="str1")
async def str2(call:CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer(text="Здесь Вы можете выбрать, интересующие Вас акции\n",reply_markup=all_stock1)


@dp.callback_query_handler(text_contains = "stock")
async def click_stock(call: CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.answer(cache_time=5)
    await Test.Q7.set()
    current_stock = call.data[6:]
    await state.update_data(answer6 = current_stock)
    await call.message.answer("Введите количество акций, которое Вы хотите добавить в свой портфель\n"
                              "или нажмите кнопку \"Удалить\"",reply_markup=amount_stock)
    await Test.next()


@dp.message_handler(state=Test.Q8)
async def get_amount_stock(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(answer7 = text)
    data = await state.get_data()
    amount = data.get("answer7")
    current_stock = data.get("answer6")
    await message.answer(f"Вы добавили в свой портфель {amount} акций компании {current_stock}",
                         reply_markup=all_stock1)
    if(BotDB.stock_exists(message.from_user.id,current_stock) == False):
        BotDB.add_stock(message.from_user.id,current_stock,amount)
    else:
        BotDB.update_stock(message.from_user.id,current_stock,amount)
    await state.reset_state(with_data=False)

@dp.callback_query_handler(text = "back_all",state=Test.Q8)
async def click_back_all(call: CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer("Здесь Вы можете выбрать, интересующие Вас акции\n",
                              reply_markup=all_stock1)

@dp.callback_query_handler(text="delete",state=Test.Q8)
async def click_delete(call: CallbackQuery,state: FSMContext):
    await state.reset_state(with_data=False)
    data = await state.get_data()
    current_stock = data.get("answer6")
    await call.message.delete()
    await call.answer(cache_time=5)
    await call.message.answer(f"Вы удалили из своего портфеля акции {current_stock} \n",
                              reply_markup=briefcase)
    BotDB.delete_stock(call.from_user.id,current_stock)





@dp.callback_query_handler(text_contains="add")
async def click_add(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Здесь можно будет добавить в свой портфель акции\n",
                              reply_markup=back_portfile)



@dp.callback_query_handler(text_contains="delete")
async def click_delete(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Здесь можно будет удалить акции из своего портфеля\n",
                              reply_markup=back_portfile)

@dp.callback_query_handler(text="back")
async def click_back(call: CallbackQuery):
    # await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=choice)

@dp.callback_query_handler(text="back_portfile")
async def click_back_portfile(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=update)