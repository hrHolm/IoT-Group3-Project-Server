import paho.mqtt.publish as pub
import paho.mqtt.subscribe as sub
import os
import json
from datetime import datetime

from urllib.parse import urlparse

url_str = os.environ.get('CLOUDMQTT_URL')
url = urlparse(url_str)
auth_info = { 'username' : url.username, 'password' : url.password}

def pub_data_to_mqtt(topic, message):
    pub.single(topic, payload=message, hostname=url.hostname, port=url.port, auth=auth_info)
'''
def on_message_save(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    topic = message.topic
    data_object = json.loads(message.payload)
    t = data_object.timestamp
    t_convert = datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    data = LightData(device_id=1, timestamp=t_convert.timestamp(), value=data_object.light_level)


    


sub.callback(on_message_save, "device/+", hostname=url.hostname, port=url.port, auth=auth_info)
'''