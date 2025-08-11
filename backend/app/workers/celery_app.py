# backend/app/workers/celery_app.py
from celery import Celery
from kombu import Queue

celery_app = Celery("video_server")

celery_app.conf.task_queues = [
    Queue("default"),
    Queue("ai"),
    Queue("thumbs"),
]
celery_app.conf.task_default_queue = "default"
