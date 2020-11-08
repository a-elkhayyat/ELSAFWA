from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.timezone import now


# Create your models here.
class Country(models.Model):
    name = models.CharField(verbose_name='اسم الدولة', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        ordering = ['id']


class State(models.Model):
    country = models.ForeignKey(Country, verbose_name='الدولة', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='اسم الدولة', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        ordering = ['id']


class City(models.Model):
    state = models.ForeignKey(State, verbose_name='المحافظة', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='اسم المدينة', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        ordering = ['id']


class Area(models.Model):
    city = models.ForeignKey(City, verbose_name='المدينة', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='اسم المنطقة', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        ordering = ['id']


class Job(models.Model):
    name = models.CharField(max_length=128, verbose_name='اسم الوظيفة')

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        ordering = ['id']


class Instance(models.Model):
    name = models.CharField(verbose_name='اسم المركز/الطبيب', max_length=128)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    expiry_date = models.DateField(verbose_name='تاريخ الإنتهاء')

    def __str__(self):
        return self.name

    def is_expired(self):
        if self.expiry_date > now().date():
            return True
        else:
            return False

    class Meta:
        default_permissions = ()
        ordering = ['id']


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='رقم الهاتف', null=True)
    email = models.EmailField(null=True, blank=True, verbose_name='البريد الإلكتروني')
    avatar = models.ImageField(verbose_name='صورة البروفايل', null=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    is_superadmin = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        default_permissions = ()
        ordering = ['id']

