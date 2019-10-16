import os
from django.db import models


class Module(models.Model):
    rf_address = models.CharField(max_length=30)
    token = models.CharField(max_length=30, default=os.getenv('CENTRAL_TOKEN'))
