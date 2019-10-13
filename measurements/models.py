import os
from django.db import models
from modules.models import Module


class ActuatorMeasurement(models.Model):
    token = models.CharField(max_length=30, default=os.getenv('CENTRAL_TOKEN'))
    water_consumption = models.FloatField(default=0.0)
    reservoir_level = models.IntegerField(default=0)


class ModuleMeasurement(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0.0)
    ground_humidity = models.IntegerField(default=0)
    battery_level = models.IntegerField(default=0)
