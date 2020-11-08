from django.db import models
from Services.models import *
from Patients.models import *


# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField(verbose_name='الموعد')
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, verbose_name='المريض')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name='الخدمة')

    def __str__(self):
        return str(self.id)


class Queue(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, verbose_name='الموعد')
    date = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name='الخدمة')

    def __str__(self):
        return str(self.id)
