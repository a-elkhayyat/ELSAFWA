from .models import *
from django.forms import ModelForm


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        exclude = ['deleted']


class MedicineDeleteForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['deleted']
