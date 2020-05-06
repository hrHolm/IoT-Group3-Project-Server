import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub
import os
from urllib.parse import urlparse

url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://whd:Q0@hairdresser-01.cloudmqtt.com:15690')
url = urlparse(url_str)
auth_info = { 'username' : url.username, 'password' : url.password}

def pub_data_to_mqtt(topic, message):
    pub.single(topic, payload=message, hostname=url.hostname, port=url.port, auth=auth_info)