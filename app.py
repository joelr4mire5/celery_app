# /*  This file initializes the Celery app with:
# Broker: redis://localhost:6379/0 – The message queue system, Redis, is used here to hold tasks before they are executed.
# Backend: redis://localhost:6379/0 – This is used to store task results.
# Include: Specifies where to find the task definitions (in tasks.py).
# The Celery app acts as the central hub for managing and distributing tasks to worker processes. 
# */

from celery import Celery

app = Celery(
    'image_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

app.conf.update(
    include=['tasks'],
    broker_connection_retry_on_startup=True  # Ensures retries on startup
)

