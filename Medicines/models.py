from django.db import models


# Create your models here.
class Medicine(models.Model):
    trade_name = models.CharField(max_length=128, verbose_name='الاسم التجاري')
    generic_name = models.CharField(max_length=128, verbose_name='الاسم العلمي', null=True, blank=True)
    company = models.CharField(max_length=128, verbose_name='الشركة المنتجة', null=True, blank=True)
    pharmacology = models.CharField(verbose_name='فارماكولوجي', null=True, blank=True, max_length=128)
    price = models.FloatField(default=0.0, verbose_name='السعر', null=True, blank=True)
    ingredient = models.IntegerField(verbose_name='التركيز', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.trade_name
