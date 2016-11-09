from django.db import models

# models/computer.py

from django.db import models
from models.core import TimeStampedModel


class Computer(TimeStampedModel):
    name = models.CharField(max_length=50)
