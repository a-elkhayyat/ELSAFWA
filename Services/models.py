from django.db import models
from Core.models import *


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الخدمة')
    price = models.FloatField(verbose_name='سعر الخدمة')
    number_of_visits = models.IntegerField(verbose_name='عدد الزيارات')
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

