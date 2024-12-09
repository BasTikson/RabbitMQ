from django.utils.deprecation import MiddlewareMixin
# from tasks.rabbit_mq_tasks import log_request
from main.producer import  RabbitMQProducer


class RequestLogMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        print('__call__ вызвали')

        # Формируем сообщение
        message = {
            'url': request.path,
            'method': request.method,
            'ip_address': self.get_client_ip(request),
            'user_agent': request.META.get('HTTP_USER_AGENT', '')
        }

        # Пытаемся отправить
        RabbitMQProducer().send_message(queue_name='first_queue', message=message)

        # Передаем далее запрос, который нам пришел
        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
