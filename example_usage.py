# example_usage.py

from app import app
from tasks import resize_image

from celery.result import AsyncResult

# Check backend and broker configurations
print(f"Result backend: {app.conf.result_backend}")
print(f"Broker: {app.conf.broker_url}")

# Submit a task


task = resize_image.delay("input_images/input_image.jpg", "output_images/output_images.jpg", (300, 300))
print(f"Task ID: {task.id}")

# Check task status
try:
    result = AsyncResult(task.id)
    print(f"Task {task.id} status: {result.status}")
    if result.ready():
        print(f"Task Result: {result.get(timeout=20)}")
except Exception as e:
    print(f"Error checking task status: {e}")