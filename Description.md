├── config/
│   ├── db.Dockerfile
│   ├── docker-compose.yml
│   └── Dockerfile
├── init/
│   └── init.sql
├── tests/
│   ├── test_firstapp.py
│   └── test_main.py
├── firstapp/
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── __init__.py
│   ├── middleware.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── task.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media/
├── pyproject.toml
├── pytest.ini
├── rabbitmqtest/
│   ├── asgi.py
│   ├── celery_conf.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── static/
├── tasks/
│   ├── __init__.py
│   ├── rabbit_mq_tasks.py
│   └── tasks.py
└── templates/
    └── main/
        ├── about.html
        ├── about_some_url.html
        └── request_logs.html