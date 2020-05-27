import os
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from urllib.parse import urlparse
import logging

from dashboard.models import Device, DeviceData

logger = logging.getLogger("mylogger")

url_str = os.environ.get('CLOUDMQTT_URL')
url = urlparse(url_str)

def on_connect(client, userdata, rc):
    client.subscribe("$SYS/#")

def on_message(client, userdata, message):
    topic = message.topic.split('/')
    logger.info(topic)
    device_id = topic[5]
    data_object = json.loads(message.payload)
    t = data_object['time_stamp']
    
    t_convert = datetime(year=t[0], month=t[1], day=t[2], hour=t[3], minute=t[4], second=t[5], microsecond=t[6])
    logger.info(t_convert)
    data = DeviceData(
        device_id=int(device_id), 
        timestamp=t_convert.timestamp(), 
        light_value=data_object['light_level'], 
        setpoint_value=data_object['setpoint'],
        intensity_value=data_object['light_intensity']
        )
    data.save()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set(url.username, url.password)
client.connect(url.hostname, url.port)

# Only the device and room should be wildcarded, since doing it on building would leave little control over throughput
client.subscribe(topic="building/1/room/+/device/+/light")