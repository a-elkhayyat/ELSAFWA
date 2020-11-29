from django.db import models
from Core.models import User, Instance
from Services.models import Service
from Patients.models import Patient


# Create your models here.
class Invoice(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الموظف')
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المريض')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الخدمة')
    visits_added = models.IntegerField(default=1, verbose_name='عدد الزيارات المضافة')
    price = models.FloatField(default=0, verbose_name='سعر الخدمة')
    discount = models.FloatField(default=0, verbose_name='خصم')
    after_discount = models.FloatField(default=0, verbose_name='بعد الخصم')
    visits_used = models.IntegerField(default=1, verbose_name='عدد الزيارات المستخدمة')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



