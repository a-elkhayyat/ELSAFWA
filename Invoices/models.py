from django.db import models
from Core.models import User, Instance
from Services.models import Service
from Patients.models import Patient


# Create your models here.
class OutcomeCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم التصنيف')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_types = (
        (1, 'سند قبض نقدية'),
        (2, 'سند صرف نقدية'),
    )
    invoice_type = models.IntegerField(choices=invoice_types, verbose_name='النوع', default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الموظف')
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المريض')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الخدمة')
    visits_added = models.IntegerField(default=1, verbose_name='عدد الزيارات المضافة')
    price = models.FloatField(default=0, verbose_name='سعر الخدمة')
    discount = models.FloatField(default=0, verbose_name='خصم')
    after_discount = models.FloatField(default=0, verbose_name='بعد الخصم')
    paid = models.FloatField(verbose_name='المدفوع', default=0)
    outcome = models.FloatField(verbose_name='منصرف', default=0, null=True, blank=True)
    visits_used = models.IntegerField(default=1, verbose_name='عدد الزيارات المستخدمة')
    category = models.ForeignKey(OutcomeCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='التصنيف')
    comment = models.TextField(null=True, blank=True, verbose_name='ملاحظات')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    is_invoice = models.BooleanField(default=False, verbose_name='فاتورة')

    def __str__(self):
        return str(self.id)

    def visits_left(self):
        return self.visits_added - self.visits_used



