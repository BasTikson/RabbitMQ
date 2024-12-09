from main.models import RequestLog
import pika
import os
import django
from django.conf import settings
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()


def process_message(queue_name, message):
    # Здесь вы можете добавить логику обработки сообщения
    print(f" [x] Received message from queue '{queue_name}': {message}")

    if queue_name == 'second_queue':
        message_dict = json.loads(message)
        RequestLog.objects.create(
            url=message_dict['url'],
            method=message_dict['method'],
            ip_address=message_dict['ip_address'],
            user_agent=message_dict['user_agent'],
            random_message=message_dict['random_message']
        )


class RabbitMQConsumer:
    def __init__(self,
                 host=settings.RABBITMQ_HOST,
                 user=settings.RABBITMQ_DEFAULT_USER,
                 password=settings.RABBITMQ_DEFAULT_PASS):
        self.host = host
        self.user = user
        self.password = password

    def receive_messages(self, queue_name):
        credentials = pika.PlainCredentials(self.user, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        def callback(ch, method, properties, body):
            message = body.decode('utf-8')
            process_message(queue_name, message)

        channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)
        print(f' [*] Waiting for messages in queue "{queue_name}". To exit press CTRL+C')
        channel.start_consuming()
