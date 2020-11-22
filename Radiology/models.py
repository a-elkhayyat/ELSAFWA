from django.db import models


# Create your models here.
class Radiology(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الاشعة')
    deleted = models.BooleanField(default=False, verbose_name="حذف")

    def __str__(self):
        return self.name

