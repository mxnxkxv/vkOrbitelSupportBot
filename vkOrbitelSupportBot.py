import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def write_message(sender, message):
    auth.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'attachment': ','.join(attachments)})

token = "vk1.a.ToejyP7iQm45rcZS19zq5NsPYIsEvcGAxbKywNB0kDhC1SwNDJkBAWq0nSRxIwteJcRci9qm8KHGR9ugVTTjL0QgpvZ4CWdhYp7etkNGpGiy_6h-R71HsGxImys4iSqbPXYSH1Y11GxMBmdg27vR64QrElPnsyZch9PlIJ1knqmC3h24rmWcbzXX_CZt2viJzFcqhyG8BzEgCLbVlD-gWw"
image = "C:/Users/mxnxkxv/Desktop/logo.jpg"
auth = vk_api.VkApi(token=token)
longpoll = VkLongPoll(auth)
upload = VkUpload(auth)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        attachments = []
        upload_image = upload.photo_messages(photos=image)[0]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
        if received_message == "Привет":
            write_message(sender, "Добрый день!")
        elif received_message == "Пока":
            write_message(sender, "До встречи!")
        else:
            write_message(sender, "Извините, я Вас не понимаю :(")