from django.db import models
from django.utils import timezone
from server.models.core import TimeStampedModel


class Users(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)


class AccessExpire(TimeStampedModel):
    user = models.ForeignKey(Users)
    expire_date = models.DateTimeField(default=timezone.now)


class NetworkClass(TimeStampedModel):
    name = models.CharField(max_length=50)


class MacAddress(TimeStampedModel):
    mac_address = models.CharField(max_length=50, null=False)
    date = models.DateField(auto_now=True)
    network = models.OneToOneField(NetworkClass)
    computer = models.ForeignKey(Computer)
    expire_date = models.OneToOneField(AccessExpire)


class Computer(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    mac_address = models.ForeignKey(MacAddress)


class ComputerCustodian(TimeStampedModel):
    computer = models.ForeignKey(Computer)
    user = models.OneToOneField(Users)
