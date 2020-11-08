from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الخدمة')
    price = models.FloatField(verbose_name='سعر الخدمة')
    number_of_visits = models.IntegerField(verbose_name='عدد الزيارات')

    def __str__(self):
        return self.name

