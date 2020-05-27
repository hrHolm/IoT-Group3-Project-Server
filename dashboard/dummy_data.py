import time
from dashboard.models import DeviceData

timestamp = time.time()

def insert_dummy_data_for_test(amount):
    '''Used for evaluation'''
    data = []
    for i in range(amount):
        datum = DeviceData(
        device_id=1, 
        timestamp=(timestamp + i), 
        light_value=100, 
        setpoint_value=80,
        intensity_value=50
        )
        data.append(datum)
    DeviceData.objects.bulk_create(data)