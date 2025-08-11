# backend/app/workers/celery_app.py
from __future__ import annotations

import os
from celery import Celery
from celery.schedules import crontab

from app.core.config import get_settings


# Celery factory that reads dynamic settings at import time
_settings = get_settings()

celery_app = Celery(
    "media_server",
    broker=_settings.jobs.broker_url,
    backend=os.environ.get("CELERY_RESULT_BACKEND", _settings.jobs.broker_url),
    include=[
        # "app.workers.tasks",  # add when tasks.py exists
    ],
)

# Basic queues aligned to our job types
celery_app.conf.task_queues = (
    {
        "name": "default",
    },
    {
        "name": "ai",
    },
    {
        "name": "thumbs",
    },
)

# Route heavy jobs to specific queues (paths here are placeholders until tasks exist)
celery_app.conf.task_routes = {
    # "app.workers.tasks.generate_thumbnails": {"queue": "thumbs"},
    # "app.workers.tasks.ai_tag_media": {"queue": "ai", "rate_limit": f"{_settings.ai.max_concurrent_jobs}/s"},
}

# Respect quiet hours by *scheduling* heavy jobs outside 01:00–06:00 when possible.
# (Actual enforcement also belongs in task code via _settings.in_quiet_hours()).
celery_app.conf.beat_schedule = {
    # Daily 3:00 backup of DB + sidecars (task to be implemented in tasks.py)
    "daily-backup": {
        "task": "app.workers.tasks.run_backup",
        "schedule": crontab(minute=0, hour=3),
        "options": {"queue": "default"},
    },
    # Cache trim suggestion (e.g., enforce 50GB thumb cap) — implement later
    # "cache-trim": {
    #     "task": "app.workers.tasks.trim_cache",
    #     "schedule": crontab(minute=0, hour="*/6"),
    #     "options": {"queue": "thumbs"},
    # },
}

celery_app.conf.update(
    worker_max_tasks_per_child=100,
    worker_prefetch_multiplier=1,
    task_time_limit=60 * 30,  # 30 minutes per task max
    broker_heartbeat=30,
    timezone=os.environ.get("TZ", "localtime"),
)

# Convenience for `celery -A app.workers.celery_app.celery_app worker -l info -Q default,ai,thumbs`