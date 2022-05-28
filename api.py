import apimoex
import pandas as pd
import requests
import seaborn as sns
import matplotlib as plt
def apii(name_kom,date1,date2,check = None):
    if(date1 > date2):
        return "ErrorDate"
    else:
        pass
    try:
        name = {'АбрауДюрсо': 'ABRD', 'АСКО ао': 'ACKO', 'Система ао':
            'AFKS', 'Аэрофлот': 'AFLT', 'AGRO-гдр': 'AGRO', 'ETF AKCH': 'AKCH', 'AKEB ETF': 'AKEB', 'AKEU ETF': 'AKEU',
                'AKGD ETF': 'AKGD', 'ETF AKMB': 'AKMB', 'ETF AKMD': 'AKMD', 'ETF AKME': 'AKME', 'AKNX ETF': 'AKNX', 'AKQU ETF': 'AKQU', 'Акрон': 'AKRN',
                'ETF AKSC': 'AKSC', 'AKSF ETF': 'AKSF', 'AKSP ETF': 'AKSP', 'AKVG ETF': 'AKVG', 'АЛРОСА ао': 'ALRS', 'AMCC ETF': 'AMCC', 'AMDG ETF': 'AMDG',
                'AMEM ETF': 'AMEM', 'АшинскийМЗ': 'AMEZ', 'AMGF ETF': 'AMGF', 'AMGM ETF': 'AMGM', 'AMGR ETF': 'AMGR', 'AMHC ETF': 'AMHC', 'AMHY ETF': 'AMHY', 'AMIG ETF': 'AMIG', 'AMIN ETF': 'AMIN', 'AMLV ETF': 'AMLV', 'AMMF ETF': 'AMMF', 'AMRB ETF': 'AMRB', 'AMRE ETF': 'AMRE', 'AMRH ETF': 'AMRH', 'AMSC ETF': 'AMSC', 'AMSL ETF': 'AMSL', 'AMVF ETF': 'AMVF', 'Аптеки36и6': 'APTK', 'РусАква ао': 'AQUA', 'Арсагера': 'ARSA', 'АстрЭнСб': 'ASSB', 'Авангрд-ао': 'AVAN', 'Башнефт ао': 'BANE', 'Башнефт ап': 'BANEP', 'BCSB ETF': 'BCSB', 'BCSH ETF': 'BCSH', 'BCSY ETF': 'BCSY', 'Белуга ао': 'BELU', 'БашИнСв ао': 'BISV', 'БашИнСв ап': 'BISVP', 'Белон ао': 'BLNG', 'БурЗолото': 'BRZL', 'БСП ао': 'BSPB', 'БСП ап': 'BSPBP', 'МКБ ао': 'CBOM', 'РН-ЗапСиб': 'CHGZ', 'ЧКПЗ ао': 'CHKZ', 'СевСт-ао': 'CHMF', 'ЧМК ао': 'CHMK', 'CIAN-адр': 'CIAN', 'Телеграф': 'CNTL', 'Телеграф-п': 'CNTLP', 'ДагСб ао': 'DASB', 'Держава ап': 'DERZP', 'ЗаводДИОД': 'DIOD', 'ETF DIVD': 'DIVD', 'ДетскийМир': 'DSKY', 'ДЭК ао': 'DVEC', 'ДонскЗР': 'DZRD', 'ДонскЗР п': 'DZRDP', 'ЕвроЭлтех': 'EELT', 'Электрцинк': 'ELTZ', 'EM44-гдр': 'EM44', 'ЭН+ГРУП ао': 'ENPG', 'ЭнелРос ао': 'ENRU', 'ESGR ETF': 'ESGR', 'ETLN-гдр': 'ETLN', 'ФСК ЕЭС ао': 'FEES', 'ДВМП ао': 'FESH', 'FIVE-гдр': 'FIVE', 'FIXP-гдр': 'FIXP', 'Совкомфлот': 'FLOT', 'FMRU ETF': 'FMRU', 'FMUS ETF': 'FMUS', 'FXBC ETF': 'FXBC', 'FXCN ETF': 'FXCN', 'FXDE ETF': 'FXDE', 'FXDM ETF': 'FXDM', 'FXEM ETF': 'FXEM', 'FXES ETF': 'FXES', 'FXFA ETF': 'FXFA', 'FXGD ETF': 'FXGD', 'FXIM ETF': 'FXIM', 'FXIP ETF': 'FXIP', 'iFXIT ETF': 'FXIT', 'FXKZ ETF': 'FXKZ', 'FXMM ETF': 'FXMM', 'FXRB ETF': 'FXRB', 'FXRD ETF': 'FXRD', 'FXRE ETF': 'FXRE', 'FXRL ETF': 'FXRL', 'FXRU ETF': 'FXRU', 'FXRW ETF': 'FXRW', 'FXTB ETF': 'FXTB', 'FXTP ETF': 'FXTP', 'FXUS ETF': 'FXUS', 'FXWO ETF': 'FXWO', 'ГАЗ ао': 'GAZA', 'ГАЗ ап': 'GAZAP', 'ГАЗКОН-ао': 'GAZC', 'ГАЗПРОМ ао': 'GAZP', 'ГАЗ-сервис': 'GAZS', 'ГАЗ-Тек ао': 'GAZT', 'ЧеркизГ-ао': 'GCHE', 'iММЦБ ао': 'GEMA', 'GEMC-гдр': 'GEMC', 'GLTR-гдр': 'GLTR', 'ETF GLVD': 'GLVD', 'ГМКНорНик': 'GMKN', 'GPBC ETF': 'GPBC', 'GPBM ETF': 'GPBM', 'GPBR ETF': 'GPBR', 'GPBS ETF': 'GPBS', 'GPBW ETF': 'GPBW', 'ETF GQGD': 'GQGD', 'ГИТ ао': 'GRNT', 'ETF GROD': 'GROD', 'ETF GSCD': 'GSCD', 'ГТМ ао': 'GTRK', 'ГЕОТЕК ао': 'GTSS', 'iHHRU-адр': 'HHRU', 'Химпром ао': 'HIMC', 'Химпром ап': 'HIMCP', 'HMSG-гдр': 'HMSG', 'РусГидро': 'HYDR', 'Инв-Девел': 'IDVP', 'Ижсталь2ао': 'IGST', 'Ижсталь ап': 'IGSTP', 'INEM ETF': 'INEM', 'INFL ETF': 'INFL', 'INGO ETF': 'INGO', 'ИНГРАД ао': 'INGR', 'ИнтерРАОао': 'IRAO', 'ИркЭнерго': 'IRGZ', 'ИРКУТ-3': 'IRKT', 'iИСКЧ ао': 'ISKJ', 'Славн-ЯНОС': 'JNOS', 'Слав-ЯНОСп': 'JNOSP', 'Куйбазот': 'KAZT', 'Куйбазот-п': 'KAZTP', 'ТНСэКубань': 'KBSB', 'КамчатЭ ао': 'KCHE', 'КамчатЭ ап': 'KCHEP', 'КурганГКао': 'KGKC', 'КурганГКап': 'KGKCP', 'КалужскСК': 'KLSB', 'КАМАЗ': 'KMAZ', 'КМЗ': 'KMEZ', 'КосогМЗ ао': 'KMTZ', 'КоршГОК ао': 'KOGK', 'СаратНПЗ': 'KRKN', 'СаратНПЗ-п': 'KRKNP', 'ТКЗКК ао': 'KRKO', 'ТКЗКК ап': 'KRKOP', 'КрасОкт-ао': 'KROT', 'КрасОкт-1п': 'KROTP', 'Красэсб ао': 'KRSB', 'Красэсб ап': 'KRSBP', 'Кокс ао': 'KSGR', 'КСБ ао': 'KTSB', 'КСБ ап': 'KTSBP', 'РСетКубань': 'KUBE', 'КузнецкийБ': 'KUZB', 'КЗМС ао': 'KZMS', 'ОргСинт ао': 'KZOS', 'ОргСинт ап': 'KZOSP', 'Лента ао': 'LENT', 'iФармсинтз': 'LIFE', 'ЛУКОЙЛ': 'LKOH', 'Лензолото': 'LNZL', 'Лензол. ап': 'LNZLP', 'ЛЭСК ао': 'LPSB', 'РСетиЛЭ': 'LSNG', 'РСетиЛЭ-п': 'LSNGP', 'ЛСР ао': 'LSRG', 'Левенгук': 'LVHK', 'МагадЭн ао': 'MAGE', 'МагадЭн ап': 'MAGEP', 'ММК': 'MAGN', 'MBEQ ETF': 'MBEQ', 'MBGB ETF': 'MBGB', 'MDMG-гдр': 'MDMG', 'МЕРИДИАН': 'MERF', 'Мегион-ао': 'MFGS', 'Мегион-ап': 'MFGSP', 'МегаФон ао': 'MFON', 'Магнит ао': 'MGNT', 'СМЗ-ао': 'MGNZ', 'МГТС-5ао': 'MGTS', 'МГТС-4ап': 'MGTSP', 'ТНСэнМарЭл': 'MISB', 'ТНСэМаЭл-п': 'MISBP', 'MKBD ETF': 'MKBD', 'МосБиржа': 'MOEX', 'Морион ао': 'MORI', 'РоссЦентр': 'MRKC', 'Россети СК': 'MRKK', 'РСетиЦП ао': 'MRKP', 'РсетСиб ао': 'MRKS', 'МРСК Ур': 'MRKU', 'РсетВол ао': 'MRKV', 'РоссЮг ао': 'MRKY', 'РСетиСЗ ао': 'MRKZ', 'МордЭнСб': 'MRSB', '+МосЭнерго': 'MSNG', 'РСетиМР ао': 'MSRS', 'Мостотрест': 'MSTT', 'MTEK ETF': 'MTEK', 'Мечел ао': 'MTLR', 'Мечел ап': 'MTLRP', 'МТС-ао': 'MTSS', 'М.видео': 'MVID', 'iНПОНаука': 'NAUK', 'НЕФАЗ': 'NFAZ', 'НКХП ао': 'NKHP', 'НКНХ ао': 'NKNC', 'НКНХ ап': 'NKNCP', 'Нижкамшина': 'NKSH', 'НЛМК ао': 'NLMK', 'НМТП ао': 'NMTP', 'ТНСэнНН ао': 'NNSB', 'ТНСэнНН ап': 'NNSBP', 'Физика ао': 'NPOF', 'iНаукаСвяз': 'NSVZ', 'Новатэк ао': 'NVTK', 'Медиахолд': 'ODVA', 'ОГК-2 ао': 'OGKB', 'OKEY-гдр': 'OKEY', 'ОМЗ-ап': 'OMZZP', 'OPNA ETF': 'OPNA', 'OPNB ETF': 'OPNB', 'OPNE ETF': 'OPNE', 'OPNR ETF': 'OPNR', 'OPNS ETF': 'OPNS', 'OPNU ETF': 'OPNU', 'ETF OPNW': 'OPNW', 'ОРГ ао': 'ORUP', 'OZON-адр': 'OZON', 'ПавлАвт ао': 'PAZA', 'ФосАгро ао': 'PHOR', 'ПИК ао': 'PIKK', 'Полюс': 'PLZL', 'ПермьЭнСб': 'PMSB', 'ПермьЭнС-п': 'PMSBP', 'Petropavl': 'POGR', 'Polymetal': 'POLY', 'iПозитив': 'POSI', 'ЧЗПСН ао': 'PRFN', 'PRIE ETF': 'PRIE', 'Приморье': 'PRMB', 'iQIWI': 'QIWI', 'Распадская': 'RASP', 'Raven': 'RAVN', 'РБК ао': 'RBCM', 'RCHY ETF': 'RCHY', 'RCMB ETF': 'RCMB', 'RCMM ETF': 'RCMM', 'RCMX ETF': 'RCMX', 'RCUS ETF': 'RCUS', 'РДБанк ао': 'RDRB', 'Ренессанс': 'RENI', 'РГС СК ао': 'RGSS', 'ЭнергияРКК': 'RKKE', 'РуссНфт ао': 'RNFT', 'Русолово': 'ROLO', 'Росбанк ао': 'ROSB', 'Роснефть': 'ROSN', 'РОСИНТЕРао': 'ROST', 'RQIE ETF': 'RQIE', 'RQIU ETF': 'RQIU', 'Россети ао': 'RSTI', 'Россети ап': 'RSTIP', 'ГазпРнД ао': 'RTGZ', 'Ростел -ао': 'RTKM', 'Ростел -ап': 'RTKMP', 'ТНСэнРст': 'RTSB', 'ТНСэнРст-п': 'RTSBP', 'ФондПервый': 'RU0005418747', 'ФондКонс': 'RU0006922010', 'ФондПроф': 'RU0006922044', 'АкцииРоста': 'RU0006922051', 'ПИФСбер-КН': 'RU000A0ERGA7', 'БКСПерспек': 'RU000A0HF0L2', 'АрсагераФА': 'RU000A0HGNG6', 'ПервыйИПИФ': 'RU000A0JNK00', 'УниверИПИФ': 'RU000A0JNK34', 'ЗПИФ КапВл': 'RU000A0JNUM1', 'ТФГ Анг-ип': 'RU000A0JNUW0', 'ПИФКапИнвб': 'RU000A0JP4U1', 'БКСXXIIвек': 'RU000A0JP708', 'БКС РосАкц': 'RU000A0JP773', 'БКС Основа': 'RU000A0JP799', 'ПИФРВМ-Лог': 'RU000A0JPCF8', 'СтражУрСод': 'RU000A0JPGC6', 'ПИФТФГ ДН': 'RU000A0JPJ35', 'ПИФ РВМ': 'RU000A0JPLG7', 'ПИФРусТрнз': 'RU000A0JPM71', 'Технологич': 'RU000A0JPPP9', 'ГлобалИн': 'RU000A0JPRL4', 'ОПИФПрРес': 'RU000A0JPRP5', 'ОРЕОЛПроек': 'RU000A0JPWL4', 'АкБрс-Инв': 'RU000A0JPZL7', 'АкБрс-Прсп': 'RU000A0JPZP8', 'ТрнфИП ТрЭ': 'RU000A0JQ4Q8', 'ПИФКредит1': 'RU000A0JQP77', 'ПИФКапит.2': 'RU000A0JQP93', 'ЗПИФ Рент2': 'RU000A0JQPA9', 'ПИФЮгра': 'RU000A0JQSM8', 'Югра-кред': 'RU000A0JQT81', 'ПИФКап21в': 'RU000A0JQUQ5', 'РВММегаплс': 'RU000A0JQYE3', 'ВИМФондАкц': 'RU000A0JR282', 'ВИМИнМсБир': 'RU000A0JR290', 'ВИМФондСб': 'RU000A0JR2A5', 'ВИМФондКаз': 'RU000A0JR2C1', 'ПИФТФГСпек': 'RU000A0JR3X5', 'ПИФАпрелев': 'RU000A0JR7V0', 'ПИФГорки-2': 'RU000A0JR7W8', 'ПИФМскПром': 'RU000A0JR7X6', 'ПИФИвПром': 'RU000A0JR7Y4', 'ПИФДомПром': 'RU000A0JR7Z1', 'ПИФОдинцПр': 'RU000A0JR811', 'ПИФ АТРИУМ': 'RU000A0JRHC0', 'ПИФГФКПрКр': 'RU000A0JRRN6', 'ТринфПерсп': 'RU000A0JRTR3', 'ПИФКоммИнв': 'RU000A0JS991', 'ТФГСтНедв1': 'RU000A0JS9A9', 'ЗПИФКрасн': 'RU000A0JSGF3', 'ТФГ-руб.об': 'RU000A0JT7G9', 'ПИФУрлНед1': 'RU000A0JT8U8', 'ПИФОбГород': 'RU000A0JTQH6', 'ПИФНевский': 'RU000A0JTVY1', 'ПИФПерПрК': 'RU000A0JU0G1', 'ПИФРВМКап': 'RU000A0JUKK1', 'ПИФ КОНСЕР': 'RU000A0JUR61', 'ПИФВариант': 'RU000A0JUTH8', 'ЗПИФЛофтин': 'RU000A0JUYB1', 'РынокДМет': 'RU000A0JVDG2', 'ИСУ ГК-3': 'RU000A0JVEZ0', 'ЗПИФПромИн': 'RU000A0JVGP6', 'БКСИмперия': 'RU000A0JVHY6', 'БКСДрагМет': 'RU000A0JVJ29', 'Прайм Недв': 'RU000A0JVJA2', 'БАЙКАЛ ПИФ': 'RU000A0JVKZ7', 'СФНАрБизн': 'RU000A0JWAW3', 'ПИФ РубОбл': 'RU000A0JX1H4', 'ЗПИФДОМ.РФ': 'RU000A0JXP78', 'СберАрБиз2': 'RU000A0ZYC64', 'ИПГПБУАЕО+': 'RU000A0ZYPM4', 'ЛобняЗПИФ': 'RU000A0ZZ422', 'СберАрБиз3': 'RU000A0ZZ5R2', 'ЗПИФ АКЦ 1': 'RU000A0ZZAU6', 'ИПИФМирИнв': 'RU000A0ZZCD8', 'ГПБУАЕОбИП': 'RU000A0ZZVH9', 'ГПБУАМОбИП': 'RU000A0ZZVL1', 'СолидРент2': 'RU000A0ZZX84', 'пре-АйПиО1': 'RU000A1000Y0', 'ПерНакопОП': 'RU000A1002D0', 'БКСФундВыб': 'RU000A1007R9', 'БКСМежОбл': 'RU000A100EP4', 'БКС РосЕвр': 'RU000A100EQ2', 'ИПИФИндБуд': 'RU000A100S25', 'ЗПИФ ПНК': 'RU000A1013V9', 'ОПИФПервый': 'RU000A101F29', 'ПИФАльфаАП': 'RU000A101HY7', 'ЗПИФ ФПР': 'RU000A101NK4', 'ОРЕОЛСтрой': 'RU000A101UK9', 'ОПИФ ОФЗ': 'RU000A101UY0', 'ПИФАльфАП2': 'RU000A101YY2', 'ПАРУС-ОЗН': 'RU000A1022Z1', 'ЗПИФ ВДО': 'RU000A1027E5', 'Арендбизн6': 'RU000A102AH5', 'ЗарРентБиз': 'RU000A102N44', 'ЗПИФРД': 'RU000A102N77', 'ИПИФРайфМО': 'RU000A102P67', 'ИПИФсубUSD': 'RU000A102PE0', 'ПИФсубEURO': 'RU000A102PF7', 'ПИФАльфаФФ': 'RU000A102PN1', 'ПИФСубРуб': 'RU000A102PQ4', 'БКС Миррес': 'RU000A102Q33', 'СФНАрБиз7': 'RU000A1034U7', 'РенДохПРО': 'RU000A103B62', 'БКСВостЗап': 'RU000A103EX2', 'РД 2': 'RU000A103HD7', 'БКСЦифрГал': 'RU000A103JE1', 'БКСИнновац': 'RU000A1040F5', 'ПАРУС-СБЛ': 'RU000A104172', 'РУСАЛ ао': 'RUAL', 'Русгрэйн': 'RUGR', 'RUSB ETF': 'RUSB', 'RUSE ETF': 'RUSE', 'ИКРУСС-ИНВ': 'RUSI', 'Русполимет': 'RUSP', 'РязЭнСб': 'RZSB', 'СамарЭн-ао': 'SAGO', 'СамарЭн-ап': 'SAGOP', 'СаратЭн-ао': 'SARE', 'СаратЭн-ап': 'SAREP', 'SBBE ETF': 'SBBE', 'SBCB ETF': 'SBCB', 'SBCS ETF': 'SBCS', 'SBDS ETF': 'SBDS', 'Сбербанк': 'SBER', 'Сбербанк-п': 'SBERP', 'SBGB ETF': 'SBGB', 'SBHI ETF': 'SBHI', 'SBMM ETF': 'SBMM', 'SBMX ETF': 'SBMX', 'SBOG ETF': 'SBOG', 'SBPS ETF': 'SBPS', 'SBRB ETF': 'SBRB', 'SBRI ETF': 'SBRI', 'SBRS ETF': 'SBRS', 'SBSP ETF': 'SBSP', 'SBWS ETF': 'SBWS', 'SCFT ETF': 'SCFT', 'SCIP ETF': 'SCIP', 'Селигдар': 'SELG', 'ЭсЭфАй ао': 'SFIN', 'iSFTL-гдр': 'SFTL', 'Сегежа': 'SGZH', 'АйсCтим ао': 'SIBG', 'Газпрнефть': 'SIBN', 'Сахэнер ао': 'SLEN', 'Самолет ао': 'SMLT', 'Сургнфгз': 'SNGS', 'Сургнфгз-п': 'SNGSP', 'ETF SPBC': 'SPBC', 'СПБ Биржа': 'SPBE', 'ETF SPBF': 'SPBF', 'СтаврЭнСб': 'STSB', 'СтаврЭнСбп': 'STSBP', 'SUGB ETF': 'SUGB', 'СОЛЛЕРС': 'SVAV', 'Светофор': 'SVET', 'ТамбЭнСб': 'TASB', 'ТамбЭнСб-п': 'TASBP', 'Татнфт 3ао': 'TATN', 'Татнфт 3ап': 'TATNP', 'TBEU ETF': 'TBEU', 'TBIO ETF': 'TBIO', 'TBRU ETF': 'TBRU', 'TBUY ETF': 'TBUY', 'TCBR ETF': 'TCBR', 'TCS-гдр': 'TCSG', 'TECH ETF': 'TECH', 'TEMS ETF': 'TEMS', 'TEUR ETF': 'TEUR', 'TEUS ETF': 'TEUS', 'TFNX ETF': 'TFNX', 'ТГК-1': 'TGKA', 'ТГК-2': 'TGKB', 'ТГК-2 ап': 'TGKBP', 'Квадра': 'TGKD', 'Квадра-п': 'TGKDP', 'ТГК-14': 'TGKN', 'TGLD ETF': 'TGLD', 'TGRN ETF': 'TGRN', 'TIPO ETF': 'TIPO', 'TMOS ETF': 'TMOS', 'ТНСэнрг ао': 'TNSE', 'ТРК ао': 'TORS', 'ТРК ап': 'TORSP', 'TPAS ETF': 'TPAS', 'TRAI ETF': 'TRAI', 'ТрансК ао': 'TRCN', 'ТрансФ ао': 'TRFM', 'ТМК ао': 'TRMK', 'Транснф ап': 'TRNFP', 'TRUR ETF': 'TRUR', 'TSOX ETF': 'TSOX', 'TSPV ETF': 'TSPV', 'TSPX ETF': 'TSPX', 'TSST ETF': 'TSST', 'Таттел. ао': 'TTLK', 'TUSD ETF': 'TUSD', 'ТЗА ао': 'TUZA', 'ОКС ао': 'UCSS', 'ЮжКузб. ао': 'UKUZ', 'iАвиастКао': 'UNAC', 'ЮУНК ао': 'UNKL', 'Юнипро ао': 'UPRO', 'Уркалий-ао': 'URKA', 'УрКузница': 'URKZ', 'УралСиб ао': 'USBN', 'ЮТэйр ао': 'UTAR', 'ОВК ао': 'UWGN', 'VEON': 'VEON-RX', 'ВолгЭнСб': 'VGSB', 'ВолгЭнСб-п': 'VGSBP', 'Варьеган': 'VJGZ', 'Варьеган-п': 'VJGZP', 'VK-гдр': 'VKCO', 'ВХЗ-ао': 'VLHZ', 'ТНСэнВорон': 'VRSB', 'ТНСэнВор-п': 'VRSBP', 'ВСМПО-АВСМ': 'VSMO', 'ВыбСудЗ ао': 'VSYD', 'ВыбСудЗ ап': 'VSYDP', 'VTBA ETF': 'VTBA', 'WIMB ETF': 'VTBB', 'VTBE ETF': 'VTBE', 'WIMF ETF': 'VTBF', 'WIMG ETF': 'VTBG', 'VTBH ETF': 'VTBH', 'VTBI ETF': 'VTBI', 'VTBL ETF': 'VTBL', 'WIMM ETF': 'VTBM', 'ВТБ ао': 'VTBR', 'VTBU ETF': 'VTBU', 'WIMX ETF': 'VTBX', 'VTBY ETF': 'VTBY', 'ЦМТ ао': 'WTCM', 'ЦМТ ап': 'WTCMP', 'ЯТЭК ао': 'YAKG', 'Якутскэнрг': 'YKEN', 'Якутскэн-п': 'YKENP', 'Yandex clA': 'YNDX', 'ТНСэнЯр': 'YRSB', 'ТНСэнЯр-п': 'YRSBP', 'ЗИЛ ао': 'ZILL', 'ЗВЕЗДА ао': 'ZVEZ'}
        secid = name[name_kom]

        df1 = pd.DataFrame(apimoex.get_market_history(session=requests.Session(),
                                                  security=secid,columns=['SECID','SHORTNAME','TRADEDATE','OPEN', 'LOW', 'HIGH','CLOSE']))

        df1 = df1.query(f"TRADEDATE >= '{date1}' and TRADEDATE <= '{date2}'",)
        df1 = df1.drop_duplicates(subset=['SECID'])

        df2 = pd.DataFrame(apimoex.get_market_history(session=requests.Session(),
                                                  security=secid,columns=['SECID','SHORTNAME','TRADEDATE','OPEN', 'LOW', 'HIGH','CLOSE']))

        df2 = df2.query(f"TRADEDATE == '{date2}'",)
        df2 = df2.drop_duplicates(subset=['SECID'])
        dt = float(((float(df1.CLOSE) - float(df2.OPEN)) / float(df1.CLOSE)) * 100)
        dz = "%.6f" % dt
        if(check == None):
            return dz
        else:
            return dz,float(df1.OPEN),float(df1.CLOSE)
    except TypeError:
        return 'TypeError'
    except KeyError:
        return "KeyError"

def grapf(name_comp,date1,date2):
    if (date1 > date2):
        return "ErrorDate"
    else:
        pass
    try:
        name = {'АбрауДюрсо': 'ABRD', 'АСКО ао': 'ACKO', 'Система ао':
            'AFKS', 'Аэрофлот': 'AFLT', 'AGRO-гдр': 'AGRO', 'ETF AKCH': 'AKCH', 'AKEB ETF': 'AKEB', 'AKEU ETF': 'AKEU',
                'AKGD ETF': 'AKGD', 'ETF AKMB': 'AKMB', 'ETF AKMD': 'AKMD', 'ETF AKME': 'AKME', 'AKNX ETF': 'AKNX',
                'AKQU ETF': 'AKQU', 'Акрон': 'AKRN',
                'ETF AKSC': 'AKSC', 'AKSF ETF': 'AKSF', 'AKSP ETF': 'AKSP', 'AKVG ETF': 'AKVG', 'АЛРОСА ао': 'ALRS',
                'AMCC ETF': 'AMCC', 'AMDG ETF': 'AMDG',
                'AMEM ETF': 'AMEM', 'АшинскийМЗ': 'AMEZ', 'AMGF ETF': 'AMGF', 'AMGM ETF': 'AMGM', 'AMGR ETF': 'AMGR',
                'AMHC ETF': 'AMHC', 'AMHY ETF': 'AMHY', 'AMIG ETF': 'AMIG', 'AMIN ETF': 'AMIN', 'AMLV ETF': 'AMLV',
                'AMMF ETF': 'AMMF', 'AMRB ETF': 'AMRB', 'AMRE ETF': 'AMRE', 'AMRH ETF': 'AMRH', 'AMSC ETF': 'AMSC',
                'AMSL ETF': 'AMSL', 'AMVF ETF': 'AMVF', 'Аптеки36и6': 'APTK', 'РусАква ао': 'AQUA', 'Арсагера': 'ARSA',
                'АстрЭнСб': 'ASSB', 'Авангрд-ао': 'AVAN', 'Башнефт ао': 'BANE', 'Башнефт ап': 'BANEP',
                'BCSB ETF': 'BCSB', 'BCSH ETF': 'BCSH', 'BCSY ETF': 'BCSY', 'Белуга ао': 'BELU', 'БашИнСв ао': 'BISV',
                'БашИнСв ап': 'BISVP', 'Белон ао': 'BLNG', 'БурЗолото': 'BRZL', 'БСП ао': 'BSPB', 'БСП ап': 'BSPBP',
                'МКБ ао': 'CBOM', 'РН-ЗапСиб': 'CHGZ', 'ЧКПЗ ао': 'CHKZ', 'СевСт-ао': 'CHMF', 'ЧМК ао': 'CHMK',
                'CIAN-адр': 'CIAN', 'Телеграф': 'CNTL', 'Телеграф-п': 'CNTLP', 'ДагСб ао': 'DASB',
                'Держава ап': 'DERZP', 'ЗаводДИОД': 'DIOD', 'ETF DIVD': 'DIVD', 'ДетскийМир': 'DSKY', 'ДЭК ао': 'DVEC',
                'ДонскЗР': 'DZRD', 'ДонскЗР п': 'DZRDP', 'ЕвроЭлтех': 'EELT', 'Электрцинк': 'ELTZ', 'EM44-гдр': 'EM44',
                'ЭН+ГРУП ао': 'ENPG', 'ЭнелРос ао': 'ENRU', 'ESGR ETF': 'ESGR', 'ETLN-гдр': 'ETLN',
                'ФСК ЕЭС ао': 'FEES', 'ДВМП ао': 'FESH', 'FIVE-гдр': 'FIVE', 'FIXP-гдр': 'FIXP', 'Совкомфлот': 'FLOT',
                'FMRU ETF': 'FMRU', 'FMUS ETF': 'FMUS', 'FXBC ETF': 'FXBC', 'FXCN ETF': 'FXCN', 'FXDE ETF': 'FXDE',
                'FXDM ETF': 'FXDM', 'FXEM ETF': 'FXEM', 'FXES ETF': 'FXES', 'FXFA ETF': 'FXFA', 'FXGD ETF': 'FXGD',
                'FXIM ETF': 'FXIM', 'FXIP ETF': 'FXIP', 'iFXIT ETF': 'FXIT', 'FXKZ ETF': 'FXKZ', 'FXMM ETF': 'FXMM',
                'FXRB ETF': 'FXRB', 'FXRD ETF': 'FXRD', 'FXRE ETF': 'FXRE', 'FXRL ETF': 'FXRL', 'FXRU ETF': 'FXRU',
                'FXRW ETF': 'FXRW', 'FXTB ETF': 'FXTB', 'FXTP ETF': 'FXTP', 'FXUS ETF': 'FXUS', 'FXWO ETF': 'FXWO',
                'ГАЗ ао': 'GAZA', 'ГАЗ ап': 'GAZAP', 'ГАЗКОН-ао': 'GAZC', 'ГАЗПРОМ ао': 'GAZP', 'ГАЗ-сервис': 'GAZS',
                'ГАЗ-Тек ао': 'GAZT', 'ЧеркизГ-ао': 'GCHE', 'iММЦБ ао': 'GEMA', 'GEMC-гдр': 'GEMC', 'GLTR-гдр': 'GLTR',
                'ETF GLVD': 'GLVD', 'ГМКНорНик': 'GMKN', 'GPBC ETF': 'GPBC', 'GPBM ETF': 'GPBM', 'GPBR ETF': 'GPBR',
                'GPBS ETF': 'GPBS', 'GPBW ETF': 'GPBW', 'ETF GQGD': 'GQGD', 'ГИТ ао': 'GRNT', 'ETF GROD': 'GROD',
                'ETF GSCD': 'GSCD', 'ГТМ ао': 'GTRK', 'ГЕОТЕК ао': 'GTSS', 'iHHRU-адр': 'HHRU', 'Химпром ао': 'HIMC',
                'Химпром ап': 'HIMCP', 'HMSG-гдр': 'HMSG', 'РусГидро': 'HYDR', 'Инв-Девел': 'IDVP',
                'Ижсталь2ао': 'IGST', 'Ижсталь ап': 'IGSTP', 'INEM ETF': 'INEM', 'INFL ETF': 'INFL', 'INGO ETF': 'INGO',
                'ИНГРАД ао': 'INGR', 'ИнтерРАОао': 'IRAO', 'ИркЭнерго': 'IRGZ', 'ИРКУТ-3': 'IRKT', 'iИСКЧ ао': 'ISKJ',
                'Славн-ЯНОС': 'JNOS', 'Слав-ЯНОСп': 'JNOSP', 'Куйбазот': 'KAZT', 'Куйбазот-п': 'KAZTP',
                'ТНСэКубань': 'KBSB', 'КамчатЭ ао': 'KCHE', 'КамчатЭ ап': 'KCHEP', 'КурганГКао': 'KGKC',
                'КурганГКап': 'KGKCP', 'КалужскСК': 'KLSB', 'КАМАЗ': 'KMAZ', 'КМЗ': 'KMEZ', 'КосогМЗ ао': 'KMTZ',
                'КоршГОК ао': 'KOGK', 'СаратНПЗ': 'KRKN', 'СаратНПЗ-п': 'KRKNP', 'ТКЗКК ао': 'KRKO',
                'ТКЗКК ап': 'KRKOP', 'КрасОкт-ао': 'KROT', 'КрасОкт-1п': 'KROTP', 'Красэсб ао': 'KRSB',
                'Красэсб ап': 'KRSBP', 'Кокс ао': 'KSGR', 'КСБ ао': 'KTSB', 'КСБ ап': 'KTSBP', 'РСетКубань': 'KUBE',
                'КузнецкийБ': 'KUZB', 'КЗМС ао': 'KZMS', 'ОргСинт ао': 'KZOS', 'ОргСинт ап': 'KZOSP',
                'Лента ао': 'LENT', 'iФармсинтз': 'LIFE', 'ЛУКОЙЛ': 'LKOH', 'Лензолото': 'LNZL', 'Лензол. ап': 'LNZLP',
                'ЛЭСК ао': 'LPSB', 'РСетиЛЭ': 'LSNG', 'РСетиЛЭ-п': 'LSNGP', 'ЛСР ао': 'LSRG', 'Левенгук': 'LVHK',
                'МагадЭн ао': 'MAGE', 'МагадЭн ап': 'MAGEP', 'ММК': 'MAGN', 'MBEQ ETF': 'MBEQ', 'MBGB ETF': 'MBGB',
                'MDMG-гдр': 'MDMG', 'МЕРИДИАН': 'MERF', 'Мегион-ао': 'MFGS', 'Мегион-ап': 'MFGSP', 'МегаФон ао': 'MFON',
                'Магнит ао': 'MGNT', 'СМЗ-ао': 'MGNZ', 'МГТС-5ао': 'MGTS', 'МГТС-4ап': 'MGTSP', 'ТНСэнМарЭл': 'MISB',
                'ТНСэМаЭл-п': 'MISBP', 'MKBD ETF': 'MKBD', 'МосБиржа': 'MOEX', 'Морион ао': 'MORI', 'РоссЦентр': 'MRKC',
                'Россети СК': 'MRKK', 'РСетиЦП ао': 'MRKP', 'РсетСиб ао': 'MRKS', 'МРСК Ур': 'MRKU',
                'РсетВол ао': 'MRKV', 'РоссЮг ао': 'MRKY', 'РСетиСЗ ао': 'MRKZ', 'МордЭнСб': 'MRSB',
                '+МосЭнерго': 'MSNG', 'РСетиМР ао': 'MSRS', 'Мостотрест': 'MSTT', 'MTEK ETF': 'MTEK',
                'Мечел ао': 'MTLR', 'Мечел ап': 'MTLRP', 'МТС-ао': 'MTSS', 'М.видео': 'MVID', 'iНПОНаука': 'NAUK',
                'НЕФАЗ': 'NFAZ', 'НКХП ао': 'NKHP', 'НКНХ ао': 'NKNC', 'НКНХ ап': 'NKNCP', 'Нижкамшина': 'NKSH',
                'НЛМК ао': 'NLMK', 'НМТП ао': 'NMTP', 'ТНСэнНН ао': 'NNSB', 'ТНСэнНН ап': 'NNSBP', 'Физика ао': 'NPOF',
                'iНаукаСвяз': 'NSVZ', 'Новатэк ао': 'NVTK', 'Медиахолд': 'ODVA', 'ОГК-2 ао': 'OGKB', 'OKEY-гдр': 'OKEY',
                'ОМЗ-ап': 'OMZZP', 'OPNA ETF': 'OPNA', 'OPNB ETF': 'OPNB', 'OPNE ETF': 'OPNE', 'OPNR ETF': 'OPNR',
                'OPNS ETF': 'OPNS', 'OPNU ETF': 'OPNU', 'ETF OPNW': 'OPNW', 'ОРГ ао': 'ORUP', 'OZON-адр': 'OZON',
                'ПавлАвт ао': 'PAZA', 'ФосАгро ао': 'PHOR', 'ПИК ао': 'PIKK', 'Полюс': 'PLZL', 'ПермьЭнСб': 'PMSB',
                'ПермьЭнС-п': 'PMSBP', 'Petropavl': 'POGR', 'Polymetal': 'POLY', 'iПозитив': 'POSI', 'ЧЗПСН ао': 'PRFN',
                'PRIE ETF': 'PRIE', 'Приморье': 'PRMB', 'iQIWI': 'QIWI', 'Распадская': 'RASP', 'Raven': 'RAVN',
                'РБК ао': 'RBCM', 'RCHY ETF': 'RCHY', 'RCMB ETF': 'RCMB', 'RCMM ETF': 'RCMM', 'RCMX ETF': 'RCMX',
                'RCUS ETF': 'RCUS', 'РДБанк ао': 'RDRB', 'Ренессанс': 'RENI', 'РГС СК ао': 'RGSS', 'ЭнергияРКК': 'RKKE',
                'РуссНфт ао': 'RNFT', 'Русолово': 'ROLO', 'Росбанк ао': 'ROSB', 'Роснефть': 'ROSN',
                'РОСИНТЕРао': 'ROST', 'RQIE ETF': 'RQIE', 'RQIU ETF': 'RQIU', 'Россети ао': 'RSTI',
                'Россети ап': 'RSTIP', 'ГазпРнД ао': 'RTGZ', 'Ростел -ао': 'RTKM', 'Ростел -ап': 'RTKMP',
                'ТНСэнРст': 'RTSB', 'ТНСэнРст-п': 'RTSBP', 'ФондПервый': 'RU0005418747', 'ФондКонс': 'RU0006922010',
                'ФондПроф': 'RU0006922044', 'АкцииРоста': 'RU0006922051', 'ПИФСбер-КН': 'RU000A0ERGA7',
                'БКСПерспек': 'RU000A0HF0L2', 'АрсагераФА': 'RU000A0HGNG6', 'ПервыйИПИФ': 'RU000A0JNK00',
                'УниверИПИФ': 'RU000A0JNK34', 'ЗПИФ КапВл': 'RU000A0JNUM1', 'ТФГ Анг-ип': 'RU000A0JNUW0',
                'ПИФКапИнвб': 'RU000A0JP4U1', 'БКСXXIIвек': 'RU000A0JP708', 'БКС РосАкц': 'RU000A0JP773',
                'БКС Основа': 'RU000A0JP799', 'ПИФРВМ-Лог': 'RU000A0JPCF8', 'СтражУрСод': 'RU000A0JPGC6',
                'ПИФТФГ ДН': 'RU000A0JPJ35', 'ПИФ РВМ': 'RU000A0JPLG7', 'ПИФРусТрнз': 'RU000A0JPM71',
                'Технологич': 'RU000A0JPPP9', 'ГлобалИн': 'RU000A0JPRL4', 'ОПИФПрРес': 'RU000A0JPRP5',
                'ОРЕОЛПроек': 'RU000A0JPWL4', 'АкБрс-Инв': 'RU000A0JPZL7', 'АкБрс-Прсп': 'RU000A0JPZP8',
                'ТрнфИП ТрЭ': 'RU000A0JQ4Q8', 'ПИФКредит1': 'RU000A0JQP77', 'ПИФКапит.2': 'RU000A0JQP93',
                'ЗПИФ Рент2': 'RU000A0JQPA9', 'ПИФЮгра': 'RU000A0JQSM8', 'Югра-кред': 'RU000A0JQT81',
                'ПИФКап21в': 'RU000A0JQUQ5', 'РВММегаплс': 'RU000A0JQYE3', 'ВИМФондАкц': 'RU000A0JR282',
                'ВИМИнМсБир': 'RU000A0JR290', 'ВИМФондСб': 'RU000A0JR2A5', 'ВИМФондКаз': 'RU000A0JR2C1',
                'ПИФТФГСпек': 'RU000A0JR3X5', 'ПИФАпрелев': 'RU000A0JR7V0', 'ПИФГорки-2': 'RU000A0JR7W8',
                'ПИФМскПром': 'RU000A0JR7X6', 'ПИФИвПром': 'RU000A0JR7Y4', 'ПИФДомПром': 'RU000A0JR7Z1',
                'ПИФОдинцПр': 'RU000A0JR811', 'ПИФ АТРИУМ': 'RU000A0JRHC0', 'ПИФГФКПрКр': 'RU000A0JRRN6',
                'ТринфПерсп': 'RU000A0JRTR3', 'ПИФКоммИнв': 'RU000A0JS991', 'ТФГСтНедв1': 'RU000A0JS9A9',
                'ЗПИФКрасн': 'RU000A0JSGF3', 'ТФГ-руб.об': 'RU000A0JT7G9', 'ПИФУрлНед1': 'RU000A0JT8U8',
                'ПИФОбГород': 'RU000A0JTQH6', 'ПИФНевский': 'RU000A0JTVY1', 'ПИФПерПрК': 'RU000A0JU0G1',
                'ПИФРВМКап': 'RU000A0JUKK1', 'ПИФ КОНСЕР': 'RU000A0JUR61', 'ПИФВариант': 'RU000A0JUTH8',
                'ЗПИФЛофтин': 'RU000A0JUYB1', 'РынокДМет': 'RU000A0JVDG2', 'ИСУ ГК-3': 'RU000A0JVEZ0',
                'ЗПИФПромИн': 'RU000A0JVGP6', 'БКСИмперия': 'RU000A0JVHY6', 'БКСДрагМет': 'RU000A0JVJ29',
                'Прайм Недв': 'RU000A0JVJA2', 'БАЙКАЛ ПИФ': 'RU000A0JVKZ7', 'СФНАрБизн': 'RU000A0JWAW3',
                'ПИФ РубОбл': 'RU000A0JX1H4', 'ЗПИФДОМ.РФ': 'RU000A0JXP78', 'СберАрБиз2': 'RU000A0ZYC64',
                'ИПГПБУАЕО+': 'RU000A0ZYPM4', 'ЛобняЗПИФ': 'RU000A0ZZ422', 'СберАрБиз3': 'RU000A0ZZ5R2',
                'ЗПИФ АКЦ 1': 'RU000A0ZZAU6', 'ИПИФМирИнв': 'RU000A0ZZCD8', 'ГПБУАЕОбИП': 'RU000A0ZZVH9',
                'ГПБУАМОбИП': 'RU000A0ZZVL1', 'СолидРент2': 'RU000A0ZZX84', 'пре-АйПиО1': 'RU000A1000Y0',
                'ПерНакопОП': 'RU000A1002D0', 'БКСФундВыб': 'RU000A1007R9', 'БКСМежОбл': 'RU000A100EP4',
                'БКС РосЕвр': 'RU000A100EQ2', 'ИПИФИндБуд': 'RU000A100S25', 'ЗПИФ ПНК': 'RU000A1013V9',
                'ОПИФПервый': 'RU000A101F29', 'ПИФАльфаАП': 'RU000A101HY7', 'ЗПИФ ФПР': 'RU000A101NK4',
                'ОРЕОЛСтрой': 'RU000A101UK9', 'ОПИФ ОФЗ': 'RU000A101UY0', 'ПИФАльфАП2': 'RU000A101YY2',
                'ПАРУС-ОЗН': 'RU000A1022Z1', 'ЗПИФ ВДО': 'RU000A1027E5', 'Арендбизн6': 'RU000A102AH5',
                'ЗарРентБиз': 'RU000A102N44', 'ЗПИФРД': 'RU000A102N77', 'ИПИФРайфМО': 'RU000A102P67',
                'ИПИФсубUSD': 'RU000A102PE0', 'ПИФсубEURO': 'RU000A102PF7', 'ПИФАльфаФФ': 'RU000A102PN1',
                'ПИФСубРуб': 'RU000A102PQ4', 'БКС Миррес': 'RU000A102Q33', 'СФНАрБиз7': 'RU000A1034U7',
                'РенДохПРО': 'RU000A103B62', 'БКСВостЗап': 'RU000A103EX2', 'РД 2': 'RU000A103HD7',
                'БКСЦифрГал': 'RU000A103JE1', 'БКСИнновац': 'RU000A1040F5', 'ПАРУС-СБЛ': 'RU000A104172',
                'РУСАЛ ао': 'RUAL', 'Русгрэйн': 'RUGR', 'RUSB ETF': 'RUSB', 'RUSE ETF': 'RUSE', 'ИКРУСС-ИНВ': 'RUSI',
                'Русполимет': 'RUSP', 'РязЭнСб': 'RZSB', 'СамарЭн-ао': 'SAGO', 'СамарЭн-ап': 'SAGOP',
                'СаратЭн-ао': 'SARE', 'СаратЭн-ап': 'SAREP', 'SBBE ETF': 'SBBE', 'SBCB ETF': 'SBCB', 'SBCS ETF': 'SBCS',
                'SBDS ETF': 'SBDS', 'Сбербанк': 'SBER', 'Сбербанк-п': 'SBERP', 'SBGB ETF': 'SBGB', 'SBHI ETF': 'SBHI',
                'SBMM ETF': 'SBMM', 'SBMX ETF': 'SBMX', 'SBOG ETF': 'SBOG', 'SBPS ETF': 'SBPS', 'SBRB ETF': 'SBRB',
                'SBRI ETF': 'SBRI', 'SBRS ETF': 'SBRS', 'SBSP ETF': 'SBSP', 'SBWS ETF': 'SBWS', 'SCFT ETF': 'SCFT',
                'SCIP ETF': 'SCIP', 'Селигдар': 'SELG', 'ЭсЭфАй ао': 'SFIN', 'iSFTL-гдр': 'SFTL', 'Сегежа': 'SGZH',
                'АйсCтим ао': 'SIBG', 'Газпрнефть': 'SIBN', 'Сахэнер ао': 'SLEN', 'Самолет ао': 'SMLT',
                'Сургнфгз': 'SNGS', 'Сургнфгз-п': 'SNGSP', 'ETF SPBC': 'SPBC', 'СПБ Биржа': 'SPBE', 'ETF SPBF': 'SPBF',
                'СтаврЭнСб': 'STSB', 'СтаврЭнСбп': 'STSBP', 'SUGB ETF': 'SUGB', 'СОЛЛЕРС': 'SVAV', 'Светофор': 'SVET',
                'ТамбЭнСб': 'TASB', 'ТамбЭнСб-п': 'TASBP', 'Татнфт 3ао': 'TATN', 'Татнфт 3ап': 'TATNP',
                'TBEU ETF': 'TBEU', 'TBIO ETF': 'TBIO', 'TBRU ETF': 'TBRU', 'TBUY ETF': 'TBUY', 'TCBR ETF': 'TCBR',
                'TCS-гдр': 'TCSG', 'TECH ETF': 'TECH', 'TEMS ETF': 'TEMS', 'TEUR ETF': 'TEUR', 'TEUS ETF': 'TEUS',
                'TFNX ETF': 'TFNX', 'ТГК-1': 'TGKA', 'ТГК-2': 'TGKB', 'ТГК-2 ап': 'TGKBP', 'Квадра': 'TGKD',
                'Квадра-п': 'TGKDP', 'ТГК-14': 'TGKN', 'TGLD ETF': 'TGLD', 'TGRN ETF': 'TGRN', 'TIPO ETF': 'TIPO',
                'TMOS ETF': 'TMOS', 'ТНСэнрг ао': 'TNSE', 'ТРК ао': 'TORS', 'ТРК ап': 'TORSP', 'TPAS ETF': 'TPAS',
                'TRAI ETF': 'TRAI', 'ТрансК ао': 'TRCN', 'ТрансФ ао': 'TRFM', 'ТМК ао': 'TRMK', 'Транснф ап': 'TRNFP',
                'TRUR ETF': 'TRUR', 'TSOX ETF': 'TSOX', 'TSPV ETF': 'TSPV', 'TSPX ETF': 'TSPX', 'TSST ETF': 'TSST',
                'Таттел. ао': 'TTLK', 'TUSD ETF': 'TUSD', 'ТЗА ао': 'TUZA', 'ОКС ао': 'UCSS', 'ЮжКузб. ао': 'UKUZ',
                'iАвиастКао': 'UNAC', 'ЮУНК ао': 'UNKL', 'Юнипро ао': 'UPRO', 'Уркалий-ао': 'URKA', 'УрКузница': 'URKZ',
                'УралСиб ао': 'USBN', 'ЮТэйр ао': 'UTAR', 'ОВК ао': 'UWGN', 'VEON': 'VEON-RX', 'ВолгЭнСб': 'VGSB',
                'ВолгЭнСб-п': 'VGSBP', 'Варьеган': 'VJGZ', 'Варьеган-п': 'VJGZP', 'VK-гдр': 'VKCO', 'ВХЗ-ао': 'VLHZ',
                'ТНСэнВорон': 'VRSB', 'ТНСэнВор-п': 'VRSBP', 'ВСМПО-АВСМ': 'VSMO', 'ВыбСудЗ ао': 'VSYD',
                'ВыбСудЗ ап': 'VSYDP', 'VTBA ETF': 'VTBA', 'WIMB ETF': 'VTBB', 'VTBE ETF': 'VTBE', 'WIMF ETF': 'VTBF',
                'WIMG ETF': 'VTBG', 'VTBH ETF': 'VTBH', 'VTBI ETF': 'VTBI', 'VTBL ETF': 'VTBL', 'WIMM ETF': 'VTBM',
                'ВТБ ао': 'VTBR', 'VTBU ETF': 'VTBU', 'WIMX ETF': 'VTBX', 'VTBY ETF': 'VTBY', 'ЦМТ ао': 'WTCM',
                'ЦМТ ап': 'WTCMP', 'ЯТЭК ао': 'YAKG', 'Якутскэнрг': 'YKEN', 'Якутскэн-п': 'YKENP', 'Yandex clA': 'YNDX',
                'ТНСэнЯр': 'YRSB', 'ТНСэнЯр-п': 'YRSBP', 'ЗИЛ ао': 'ZILL', 'ЗВЕЗДА ао': 'ZVEZ'}
        secid = name[name_comp]

        df1 = pd.DataFrame(apimoex.get_market_history(session=requests.Session(),
                                                      security=secid,
                                                      columns=['SECID', 'SHORTNAME', 'TRADEDATE', 'OPEN', 'LOW', 'HIGH',
                                                               'CLOSE']))
        df1 = df1.query(f"TRADEDATE >= '{date1}' and TRADEDATE <= '{date2}'", )
        normalisedate1 = int(date1.replace("-", ""))
        normalisedate2 = int(date2.replace("-", ""))
        if (normalisedate2 - normalisedate1 > 10000):

            df1.TRADEDATE = df1.TRADEDATE.apply(lambda x: x[:4])
        elif normalisedate2 - normalisedate1 > 400:
            df1.TRADEDATE = df1.TRADEDATE.apply(lambda x: x[:7])
        else:
            df1.TRADEDATE = df1.TRADEDATE.apply(lambda x: x[:10])

        ax = sns.lineplot(x='TRADEDATE', y='CLOSE', data=df1,legend=True)
        ax.tick_params(axis='x', rotation=30)
        fig = ax.get_figure()
        # plt.pyplot.show()
        fig.savefig(f'.\page\{name_comp}_{date1}_{date2}.png')
        plt.pyplot.close()
        return 0
    except KeyError:
        return "KeyError"
    except TypeError:
        return 'TypeError'

