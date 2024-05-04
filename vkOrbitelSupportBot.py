import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def write_message(sender, message):
    auth.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

token = "vk1.a.xDPEyahppKoJfsXgcvQqYnfc80R0wC_TQvFrRhUijDjqgOwqK5N1uiiHkQKRm4zLmtducQNJEZNwLeEQ53uDCLYl-JMMJ6oN1Xtl16cWJJQVETapxv7ngWd0Ek14IF027XZP5-eIKbxQZ4VmiKUgUnisj0BMS9gbuyKDai-1ZJzsEWPbUiUG45jBMRqBj3Yf8ykuBDnJ3_NJZYwN_7qsww"
auth = vk_api.VkApi(token=token)
longpoll = VkLongPoll(auth)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        if received_message == "Привет":
            write_message(sender, "Добрый день!")
        elif received_message == "Пока":
            write_message(sender, "До встречи!")
        else:
            write_message(sender, "Извините, я Вас не понимаю :(")