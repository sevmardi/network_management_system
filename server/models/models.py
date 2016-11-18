from django.db import models
from django.utils import timezone
#from server.models.core import TimeStampedModel


class Users(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=False)


class AccessExpire(models.Model):
    user = models.ForeignKey(Users)
    expire_date = models.DateTimeField(default=timezone.now, null=False)


class NetworkClass(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    description = models.CharField(max_length=255, null=True)


class Computer(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255, null=True)


class MacAddress(models.Model):
    mac_address = models.CharField(max_length=50, null=False)
    date = models.DateField(auto_now=True)
    network = models.OneToOneField(NetworkClass)
    computer = models.ForeignKey(Computer)
    expire_date = models.OneToOneField(AccessExpire)
    user = models.ManyToManyField(Users)

class ComputerCustodian(models.Model):
    computer = models.ForeignKey(Computer)
    user = models.OneToOneField(Users)
