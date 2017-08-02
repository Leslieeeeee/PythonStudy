#import Mysqldb
from django.db import models

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    psd = models.CharField(max_length=32)
    qq = models.IntegerField(max_length=32)
    email = models.CharField(max_length=32)


class OrderInfo(models.Model):
    user = models.CharField(max_length=32)
    psd = models.CharField(max_length=32)
    qq = models.IntegerField(max_length=32)
    email = models.CharField(max_length=32)





