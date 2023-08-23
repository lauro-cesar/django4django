from celery import Celery
from celery.schedules import crontab
from django.conf import settings
import os
import logging
debug_logger = logging.getLogger("django_debug")


REDIS_QUEUE_HOST = os.environ.get("REDIS_QUEUE_HOST", default="127.0.0.1")
REDIS_QUEUE_PORT = os.environ.get("REDIS_QUEUE_PORT", default=6379)
REDIS_QUEUE_DB = os.environ.get("REDIS_QUEUE_DB", default=0)
REDIS_QUEUE_QUEUE_NAME = os.environ.get(
    "REDIS_QUEUE_QUEUE_NAME", default="default_django_queue"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "___.settings")
from django.conf import settings


app = Celery(
    "___",
    broker_url=f"redis://{REDIS_QUEUE_HOST}:{REDIS_QUEUE_PORT}/{REDIS_QUEUE_DB}",
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(result_expires=3600, enable_utc=True, timezone="America/Sao_Paulo")
app.autodiscover_tasks()
