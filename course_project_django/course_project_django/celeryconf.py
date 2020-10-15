import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_project_django.settings')

app = Celery('course_project_django')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
