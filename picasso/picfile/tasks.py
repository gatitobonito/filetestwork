from celery import shared_task
from .s3client import upload_video


@shared_task
def upload(local_path, path):
    upload_video(local_path, path)
    return 'success'
