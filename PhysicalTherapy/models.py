from django.db import models
from Core.models import User, Instance


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الجهاز')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم التمرين')

    def __str__(self):
        return self.name


