from celery import shared_task
from main.models import RequestLog


# @shared_task
@shared_task(name='main.tasks.log_request')
def log_request(url, method, ip_address, user_agent):
    RequestLog.objects.create(
        url=url,
        method=method,
        ip_address=ip_address,
        user_agent=user_agent
    )
