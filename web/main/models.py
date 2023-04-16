from django.db import models
from django.utils import timezone

# Create your models here.
class Log(models.Model):
    login = models.CharField('Login', max_length=255)
    password = models.CharField('Password', max_length=255)
    date = models.DateField('Date', default=timezone.now)

    