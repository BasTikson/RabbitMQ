import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitmqtest.settings')
app = Celery('rabbitmqtest')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['tasks'])