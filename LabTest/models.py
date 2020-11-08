from django.db import models


# Create your models here.
class LabTest(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم التحليل')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name


class LabTestAttribute(models.Model):
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128, verbose_name='اسم الخاصية')
    normal_min = models.FloatField(verbose_name='طبيعي من', null=True, blank=True)
    normal_max = models.FloatField(verbose_name='طبيعي حتي', null=True, blank=True)
    unit = models.CharField(verbose_name='وحدة القياس', null=True, blank=True, max_length=128)

    def __str__(self):
        return self.name

