from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Patient)
admin.site.register(Complain)
admin.site.register(Disease)
admin.site.register(CancerType)
admin.site.register(PatientInvestigation)