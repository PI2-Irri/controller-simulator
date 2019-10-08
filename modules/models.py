from django.db import models


class Module(models.Model):
    rf_address = models.CharField(max_lenght=30)
    battery_level = models.IntegerField(default=0)
