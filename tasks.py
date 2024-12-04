
# 2. tasks.py: Task Definitions
# Purpose: Defines a reusable task (resize_image) that can be called asynchronously.
# The task:
# Takes an image path (image_path), an output path (output_path), and a desired size (size).
# Uses the Pillow library to resize the image and save the result.
# Returns a success message or an error if something goes wrong.
# The @shared_task decorator tells Celery that this function can be executed asynchronously as a task.

# tasks.py

from celery import shared_task
from PIL import Image
import os
from time import sleep
@shared_task
def resize_image(image_path, output_path, size):
    """
    Resize an image to the specified size.
    :param image_path: Path to the original image.
    :param output_path: Path to save the resized image.
    :param size: Tuple (width, height) for the new size.
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            sleep(60)
            img.save(output_path)
        return f"Resized image saved to {output_path}"
    except Exception as e:
        return str(e)
