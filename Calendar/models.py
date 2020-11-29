from django.db import models
from Services.models import *
from Patients.models import *
from django.db.models import Sum


# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField(verbose_name='الموعد')
    end = models.DateTimeField(verbose_name='نهاية الجلسة', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, verbose_name='المريض')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name='الخدمة')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Queue(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, verbose_name='الموعد')
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, verbose_name='المريض')
    date = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name='الخدمة')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default='-1')
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def sessions_left(self):
        patient = self.patient
        queues = patient.queue_set.filter(service=self.service)
        if queues:
            count = queues.aggregate(count=Sum('count'))
            return count['count']
        else:
            return 0
