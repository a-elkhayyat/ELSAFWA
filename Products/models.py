from django.db import models
from Core.models import Instance


# Create your models here.
class Product(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=128, verbose_name='الاسم')
    cost_price = models.FloatField(verbose_name='سعر التكلفة')
    sell_price = models.FloatField(verbose_name='سعر البيع')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name
