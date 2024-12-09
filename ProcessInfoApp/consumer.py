import pika
from ProcessInfoApp.processinfo import add_user_comment
from ProcessInfoApp.config import (
    RABBITMQ_DEFAULT_USER,
    RABBITMQ_DEFAULT_PASS,
    RABBITMQ_HOST,
)


class RabbitMQConsumer:
    def __init__(self,
                 host=RABBITMQ_HOST,
                 user=RABBITMQ_DEFAULT_USER,
                 password=RABBITMQ_DEFAULT_PASS):
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
            add_user_comment(message_rmq=message)

        channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)
        print(f' [*] Waiting for messages in queue "{queue_name}". To exit press CTRL+C')
        channel.start_consuming()


if __name__ == "__main__":
    queue_name_start = 'first_queue'
    consumer = RabbitMQConsumer()
    consumer.receive_messages(queue_name_start)
