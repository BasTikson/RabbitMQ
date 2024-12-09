from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env_file = os.path.join(os.path.join(BASE_DIR, '.env'))
environ.Env.read_env(env_file)

# Настройки RabbitMQ
RABBITMQ_DEFAULT_USER = env('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = env('RABBITMQ_DEFAULT_PASS')
RABBITMQ_HOST = env('RABBITMQ_HOST')
RABBITMQ_PORT = env('RABBITMQ_PORT')