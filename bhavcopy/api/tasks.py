from celery import shared_task
import requests

@shared_task    
def add():
    requests.get('http://localhost:8000/api/key/ABBLTD')
    return 'here'
