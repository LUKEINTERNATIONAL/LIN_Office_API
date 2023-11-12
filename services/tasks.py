# Create your tasks here
import yaml
import os
import json
from pathlib import Path
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
config_data = json.load(open(os.path.join(BASE_DIR,'config.json')))
from celery import shared_task


@shared_task(queue='send_message')   
def send_sms_email(_url,data,message_type):
    try:
        requests.post(url = str(_url), json = data)
        print(f"Send {message_type} successful")
    
    except Exception as e:
        print(f"Failed to send {message_type}")
        print(f"Error: {e}")


