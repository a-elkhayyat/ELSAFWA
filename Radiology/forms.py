from django.forms import ModelForm
from .models import *


class RadiologyForm(ModelForm):
    class Meta:
        model = Radiology
        exclude = ['deleted']


class RadiologyDeleteForm(ModelForm):
    class Meta:
        model = Radiology
        fields = ['deleted']
