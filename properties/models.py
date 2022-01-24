from typing_extensions import Required
from django.db import models

# Create your models here.


class Building(models.Model):
    name = models.CharField(max_length=50, unique=True, Required=True)
