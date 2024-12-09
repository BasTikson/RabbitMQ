import os
import sys
import django

# Устанавливаем переменную окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitmqtest.settings')
django.setup()

from rabbit_mq_tasks import RabbitMQConsumer


def start_consumer(queue_name):
    consumer = RabbitMQConsumer()
    consumer.receive_messages(queue_name)


if __name__ == '__main__':
    start_consumer('second_queue')
