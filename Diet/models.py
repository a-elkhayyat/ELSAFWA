from django.db import models
from Core.models import Instance


# Create your models here.
class Diet(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم النظام')
    description = models.TextField(verbose_name='وصف النظام')
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    instance = models.ForeignKey(Instance, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
