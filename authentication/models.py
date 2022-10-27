from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
