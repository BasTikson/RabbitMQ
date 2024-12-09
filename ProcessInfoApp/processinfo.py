from faker import Faker
import random
import json
from ProcessInfoApp.producer import RabbitMQProducer


# Функция, которая будет что-то делать с изначальным сообщением
def add_user_comment(message_rmq: str):
    # Генерируем какое-то предложение
    fake = Faker()
    num_words = random.randint(5, 6)
    sentence = fake.sentence(nb_words=num_words)
    sentence = sentence.rstrip('.')

    # Должны распарить сообщение, включить в него случайное предложение и отправить в другую очередь
    message_dict = json.loads(message_rmq)
    if isinstance(message_dict, dict):
        message_dict.update({'random_message': sentence})
        RabbitMQProducer().send_message(queue_name='second_queue', message=message_dict)

    else:
        print('Сообщение не превратили в словарь!')
