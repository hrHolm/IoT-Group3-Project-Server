import paho.mqtt.publish as pub
import paho.mqtt.subscribe as sub
import os
import json
from datetime import datetime

from urllib.parse import urlparse

url_str = os.environ.get('CLOUDMQTT_URL')
url = urlparse(url_str)
auth_info = { 'username' : url.username, 'password' : url.password}

def adjust_device(device_id, message):
    pub.single(topic="building/1/room/1/device/{id}/adjust".format(id=device_id), payload=message, hostname=url.hostname, port=url.port, auth=auth_info)