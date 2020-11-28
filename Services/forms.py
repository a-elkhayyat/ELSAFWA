from django.forms import ModelForm
from .models import *


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['deleted']


class ServiceDeleteForm(ModelForm):
    class Meta:
        model = Service
        fields = ['deleted']
