from os import remove
from django_q.tasks import async_task
import time


def delete_image(image_path):
    time.sleep(5)
    if image_path.startswith('/media/temporal/'):
        remove(image_path)
    