from django.db import models
from account.models import Account
# Create your models here.

class Contact(models.Model):

    full_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name


class Trial(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=50)
    iptv_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    mac_address = models.CharField(max_length=30)
    option = models.BooleanField(default=False)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name

    

