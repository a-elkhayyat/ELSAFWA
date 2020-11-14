from django.db import models


# Create your models here.
class Radiology(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الاشعة')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

