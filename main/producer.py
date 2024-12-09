import pika
from django.conf import settings
import json
import jsonpickle


# Отправитель сообщений

class RabbitMQProducer:
    def __init__(self,
                 host=settings.RABBITMQ_HOST,
                 user=settings.RABBITMQ_DEFAULT_USER,
                 password=settings.RABBITMQ_DEFAULT_PASS):

        self.host = host
        self.user = user
        self.password = password

    def send_message(self, queue_name, message):
        credentials = pika.PlainCredentials(self.user, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        # Преобразование к правильному виду. RabbitMQ принимает форматы, которые могут быть представлены в виде строки
        if isinstance(message, dict):
            message = json.dumps(message)
        elif isinstance(message, object):
            message = jsonpickle.encode(message)

        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f" [x] Sent '{message}' to queue '{queue_name}'")
        connection.close()
