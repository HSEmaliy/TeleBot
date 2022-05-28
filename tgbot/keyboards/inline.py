from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import emoji

portfolio = emoji.emojize(":briefcase:")
profil = emoji.emojize(":bust_in_silhouette:")
laprop = emoji.emojize(":laptop:")
b = emoji.emojize(":footprints:")
back = emoji.emojize(":BACK_arrow:")
end = emoji.emojize(":END_arrow:")
all_stock = emoji.emojize(":receipt:")
dolar = emoji.emojize(":dollar_banknote:")
graf = emoji.emojize(":chart_increasing:")
proc = emoji.emojize(":right_arrow_curving_left:")
plus = emoji.emojize(":check_mark:")
minus = emoji.emojize(":cross_mark:")
info = emoji.emojize(":speech_balloon:")
one = emoji.emojize(":keycap_1:")
two = emoji.emojize(":keycap_2:")
three = emoji.emojize(":keycap_3:")
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{profil}Профиль",callback_data="prof"),
            InlineKeyboardButton(text=f"{laprop}Работа с сайтом", callback_data="api"),

        ],
        [
            InlineKeyboardButton(text=f"{portfolio}Портфель", callback_data="portf"),
            InlineKeyboardButton(text=f"{info}Инструкция", callback_data="info"),
        ],
    ]
)
API = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{proc}Процент", callback_data="api_perc"),
            InlineKeyboardButton(text=f"{graf}График", callback_data="api_graf"),
        ],
        [
            InlineKeyboardButton(text=f"{back}Назад", callback_data="back_menu")
        ]
    ]
)
briefcase = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{all_stock}Все акции",callback_data="all_stock"),
            InlineKeyboardButton(text=f"{dolar}Мои акции", callback_data="my_Stock"),
        ]
    ]
)
back_portfile = InlineKeyboardButton(text=f"{back}Назад", callback_data="back_portfile")
back_to_promotion_menu = InlineKeyboardMarkup()
back_to_promotion_menu.insert(back_portfile)
update = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{plus}Добавить", callback_data="add"),
            InlineKeyboardButton(text=f"{minus}Удалить", callback_data="delete"),
        ]
    ]
)

amount_stock = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{minus}Удалить",callback_data="delete"),
        ],
        [
            InlineKeyboardButton(text=f"{back}Назад", callback_data="back_all"),
        ]
    ]
)

my_stock = InlineKeyboardMarkup()
Prof = InlineKeyboardMarkup()
Info = InlineKeyboardMarkup()

Back = InlineKeyboardButton(text=f"{back}Назад", callback_data="back")
update.insert(Back)
Prof.insert(Back)
Info.insert(Back)
briefcase.insert(Back)
all_stock1 = InlineKeyboardMarkup(row_width=1,
    inline_keyboard =
    [
        [
            InlineKeyboardButton(text="Yandex clA",callback_data="stock:Yandex clA"),
        ],
        [
            InlineKeyboardButton(text="ГАЗПРОМ ао", callback_data="stock:ГАЗПРОМ ао"),
        ],
        [
            InlineKeyboardButton(text="Сбербанк", callback_data="stock:Сбербанк"),
        ],
        [
            InlineKeyboardButton(text="ФосАгро ао", callback_data="stock:ФосАгро ао"),
        ],
        [
            InlineKeyboardButton(text="ЛУКОЙЛ", callback_data="stock:ЛУКОЙЛ"),
        ],
        [
            InlineKeyboardButton(text="Роснефть", callback_data="stock:Роснефть"),
        ],
        [
            InlineKeyboardButton(text="ГМКНорНик", callback_data="stock:ГМКНорНик"),
        ],
        [
            InlineKeyboardButton(text="Магнит ао", callback_data="stock:Магнит ао"),
        ],
        [
            InlineKeyboardButton(text="TCS-гдр", callback_data="stock:TCS-гдр"),
        ],
        [
            InlineKeyboardButton(text="Новатэк ао", callback_data="stock:Новатэк ао"),
        ],
        [
            InlineKeyboardButton(text="ВТБ ао", callback_data="stock:ВТБ ао"),
        ],
        [
            InlineKeyboardButton(text="МТС-ао", callback_data="stock:МТС-ао"),
        ],
        [
            InlineKeyboardButton(text="МКБ ао", callback_data="stock:МКБ ао"),
        ],
        [
            InlineKeyboardButton(text="Полюс", callback_data="stock:Полюс"),
        ],
        [
            InlineKeyboardButton(text="ПИК ао", callback_data="stock:ПИК ао"),
        ],
        [
            InlineKeyboardButton(text=f"{two} стр.", callback_data="str2"),
            InlineKeyboardButton(text=f"{three} стр.", callback_data="str3"),
        ],
        [
            InlineKeyboardButton(text=f"{end}Назад", callback_data="back_portfile"),
        ]
    ]
)

all_stock2 = InlineKeyboardMarkup(
    inline_keyboard =
    [
        [
            InlineKeyboardButton(text="Polymetal",callback_data="stock:Polymetal"),
        ],
        [
            InlineKeyboardButton(text="ГАЗПРОМ ао", callback_data="stock:ГАЗПРОМ ао"),
        ],
        [
            InlineKeyboardButton(text="ИнтерРАОао", callback_data="stock:ИнтерРАОао"),
        ],
        [
            InlineKeyboardButton(text="Сургнфгз-п", callback_data="stock:Сургнфгз-п"),
        ],
        [
            InlineKeyboardButton(text="VK-гдр", callback_data="stock:VK-гдр"),
        ],
        [
            InlineKeyboardButton(text="ММК", callback_data="stock:ММК"),
        ],
        [
            InlineKeyboardButton(text="НЛМК ао", callback_data="stock:НЛМК ао"),
        ],
        [
            InlineKeyboardButton(text="Сургнфгз", callback_data="stock:Сургнфгз"),
        ],
        [
            InlineKeyboardButton(text="Юнипро ао", callback_data="stock:Юнипро ао"),
        ],
        [
            InlineKeyboardButton(text="Petropavl", callback_data="stock:Petropavl"),
        ],
        [
            InlineKeyboardButton(text="МосБиржа", callback_data="stock:МосБиржа"),
        ],
        [
            InlineKeyboardButton(text="РУСАЛ ао", callback_data="stock:РУСАЛ ао"),
        ],
        [
            InlineKeyboardButton(text="Система ао", callback_data="stock:Система ао"),
        ],
        [
            InlineKeyboardButton(text="Квадра", callback_data="stock:Квадра"),
        ],
        [
            InlineKeyboardButton(text="Белуга ао", callback_data="stock:Белуга ао"),
        ],
        [
            InlineKeyboardButton(text=f"{one} стр.", callback_data="str1"),
            InlineKeyboardButton(text=f"{three} стр.", callback_data="str3"),
        ],
        [
            InlineKeyboardButton(text=f"{end}Назад", callback_data="back_portfile"),
        ]
    ]
)

all_stock3 = InlineKeyboardMarkup(
    inline_keyboard =
    [
        [
            InlineKeyboardButton(text="iПозитив",callback_data="stock:iПозитив"),
        ],
        [
            InlineKeyboardButton(text="Татнфт 3ап", callback_data="stock:Татнфт 3ап"),
        ],
        [
            InlineKeyboardButton(text="OZON-адр", callback_data="stock:OZON-адр"),
        ],
        [
            InlineKeyboardButton(text="Аэрофлот", callback_data="stock:Аэрофлот"),
        ],
        [
            InlineKeyboardButton(text="Мечел ап", callback_data="stock:Мечел ап"),
        ],
        [
            InlineKeyboardButton(text="Распадская", callback_data="stock:Распадская"),
        ],
        [
            InlineKeyboardButton(text="FIVE-гдр", callback_data="stock:FIVE-гдр"),
        ],
        [
            InlineKeyboardButton(text="НКНХ ап", callback_data="stock:НКНХ ап"),
        ],
        [
            InlineKeyboardButton(text="Сегежа", callback_data="stock:Сегежа"),
        ],
        [
            InlineKeyboardButton(text="Транснф ап", callback_data="stock:Транснф ап"),
        ],
        [
            InlineKeyboardButton(text="ВСМПО-АВСМ", callback_data="stock:КоршГОК ао"),
        ],
        [
            InlineKeyboardButton(text="Приморье", callback_data="stock:Приморье"),
        ],
        [
            InlineKeyboardButton(text="ГазпРнД ао", callback_data="stock:ГазпРнД ао"),
        ],
        [
            InlineKeyboardButton(text="УрКузница", callback_data="stock:УрКузница"),
        ],
        [
            InlineKeyboardButton(text="Лензолото", callback_data="stock:Лензолото"),
        ],
        [
            InlineKeyboardButton(text=f"{one} стр.", callback_data="str1"),
            InlineKeyboardButton(text=f"{three} стр.", callback_data="str2"),
        ],
        [
            InlineKeyboardButton(text=f"{end}Назад", callback_data="back_portfile"),
        ]
    ]
)