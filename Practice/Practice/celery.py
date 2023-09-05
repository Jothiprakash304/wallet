from celery import Celery
from django.conf import settings
import os
app=Celery('Practice')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Practice.settings')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()