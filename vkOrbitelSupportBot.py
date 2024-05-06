import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import json

token = "vk1.a.zUyng5AuQ9M64nHC2HgLXNqghmB4qTMoVvCk2A0pj5ERtsdKJKBgELbx0aBekuXXpnVIznTT2xYa8kEc5UY8olZkf2yQi1ErlAIc_68ELu5v2lAEKJcuynAAyi-Y07bNhLnRGlzCnQPcbQfG1aSqULj2oxW-ttfoXnQ2OELYsrZ0WHZTk09vU8CTMvmqnDfNHKdZuDuO-pDCVDWDL-fNAg"
auth = vk_api.VkApi(token=token)
longpoll = VkLongPoll(auth)

def generate_keyboard(buttons):
    keyboard = {
        "one_time": False,
        "buttons": buttons
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    return str(keyboard.decode('utf-8'))

buttons1 = [
    [{
        "action": {
            "type": "open_link",
            "link": "https://www.speedtest.net",
            "label": "Проверить скорость"
        },
    },
    {
        "action": {
            "type": "open_link",
            "link": "https://orbitel.ru",
            "label": "Открыть сайт"
        },
    }],
    [{
        "action": {
            "type": "open_link",
            "link": "https://orbitel.ru/smotr",
            "label": "Посмотреть тарифы"
        },
    },
    {
        "action": {
            "type": "open_link",
            "link": "https://orbitel.ru/business",
            "label": "Для бизнеса"
        },
    }],
    [{
        "action": {
            "type": "text",
            "label": "Соцсети"
        },
        "color": "primary"
    },
    {
        "action": {
            "type": "text",
            "label": "Адрес"
        },
        "color": "primary"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Поддержка"
        },
        "color": "positive"
    }]
]

buttons2 = [
    [{
        "action": {
            "type": "text",
            "label": "Задать вопрос здесь"
        },
        "color": "positive"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Телефон горячей линии"
        },
        "color": "positive"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Вернуться в главное меню"
        },
        "color": "negative"
    }]
]

buttons3 = [
    [{
        "action": {
            "type": "text",
            "label": "Тип подключения"
        },
        "color": "primary"
    },
    {
        "action": {
            "type": "text",
            "label": "Абонентская плата"
        },
        "color": "primary"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Пропал ТВ-канал"
        },
        "color": "primary"
    },
    {
        "action": {
            "type": "text",
            "label": "Я переезжаю"
        },
        "color": "primary"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Блокировка услуги"
        },
        "color": "primary"
    },
    {
        "action": {
            "type": "text",
            "label": "Отрицательный баланс"
        },
        "color": "primary"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Настроил, а интернета нет"
        },
        "color": "primary"
    },
    {
        "action": {
            "type": "text",
            "label": "Телефон горячей линии"
        },
        "color": "primary"
    }],
    [{
        "action": {
            "type": "text",
            "label": "Вернуться в главное меню"
        },
        "color": "negative"
    }]
]

keyboard1 = generate_keyboard(buttons1)
keyboard2 = generate_keyboard(buttons2)
keyboard3 = generate_keyboard(buttons3)

def send_message(user_id, message, keyboard=None):
    params = {
        'user_id': user_id,
        'message': message,
        'random_id': get_random_id()
    }
    if keyboard is not None:
        params['keyboard'] = keyboard
    auth.method('messages.send', params)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text.lower()
        sender = event.user_id
        if received_message in ["старт", "привет", "меню"]:
            send_message(sender, "Привет! Чем могу помочь?", keyboard=keyboard1)
        elif received_message == "поддержка":
            send_message(sender, "Вы можете спросить у меня или позвонить на горячую линию", keyboard=keyboard2)
        elif received_message == "задать вопрос здесь":
            send_message(sender, "Выберите вопрос из списка или позвоните на горячую линию", keyboard=keyboard3)
        elif received_message == "телефон горячей линии":
            send_message(sender, "Телефон горячей линии: +7 (3522) 65-00-00", keyboard=keyboard1)
        elif received_message == "соцсети":
            send_message(sender, "Наш сайт: orbitel.ru\nМы в ВКонтакте: vk.com/orbitel", keyboard=keyboard1)
        elif received_message == "вернуться в главное меню":
            send_message(sender, "Вы вернулись в главное меню", keyboard=keyboard1)
        elif received_message == "тип подключения":
            send_message(sender, "В сети Орбител используется статический IP.", keyboard=keyboard3)
        elif received_message == "абонентская плата":
            send_message(sender, "Абонентская плата списывается в начале каждого месяца независимо от даты вашего подключения. Списание производится за весь месяц целиком. Если вы были подключены в середине месяца, первый раз вам начисляется абонентская плата на остаток месяца, затем будет начисляться за полный.", keyboard=keyboard3)
        elif received_message == "пропал тв-канал":
            send_message(sender, "Если пропал ТВ-канал попробуйте выполнить автонастройку каналов по инструкции: orbitel.ru/tv-manual", keyboard=keyboard3)
        elif received_message == "я переезжаю":
            send_message(sender, "В этом случае вам необходимо обратиться в офис или по тел. +7 (3522) 65-00-00 и уточнить возможность переоформления договора по новому адресу.", keyboard=keyboard3)
        elif received_message == "блокировка услуги":
            send_message(sender, "Если вы уезжаете в отпуск и не планируете пользоваться услугой, вы можете подойти в офис или подать заявку на блокировку по тел. +7 (3522) 65-00-00.", keyboard=keyboard3)
        elif received_message == "отрицательный баланс":
            send_message(sender, "По условию договора абонент обязуется оплачивать абонентскую плату ежемесячно. Если вы не планируете пользоваться интернетом какое то время, вам нужно подать заявку на блокировку. Но если задолженность все-таки образовалась, а интернетом в течении месяца вы не пользовались, вам могут сделать перерасчет за данный период, удержав с вас по 100 рублей за поддержание линии.", keyboard=keyboard3)
        elif received_message == "настроил, а интернета нет":
            send_message(sender, "Если вы прописали настройки на другом компьютере или установили роутер, вам необходимо позвонить в техническую поддержку по тел. +7 (3522) 65-00-00, чтобы ваше устройство зафиксировали в сети Орбител.", keyboard=keyboard3)
        elif received_message == "адрес":
            send_message(sender, "Мы находимся по адресу: Курган ул. Пичугина 16/IV\n\nЧасы работы:\n\nПн 9:00 - 19:00\nВт 9:00 - 19:00\nСр 9:00 - 19:00\nЧт 9:00 - 19:00\nПт Сб 10:00 - 16:00\nВс 10:00 - 16:00", keyboard=keyboard1)
        else:
            send_message(sender, "Извините, я Вас не понимаю :(\n\nНапишите мне Привет, Старт или Меню")