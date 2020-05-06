from django.db import models

# Create your models here.
class Device(models.Model):
    device_id = models.IntegerField(primary_key=True)
    
class LightData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    value = models.FloatField()

class SetpointData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    value = models.FloatField()

class IntensityData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    value = models.FloatField()
