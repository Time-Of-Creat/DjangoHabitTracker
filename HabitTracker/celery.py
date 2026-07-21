import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HabitTracker.settings')

app = Celery('HabitTracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()