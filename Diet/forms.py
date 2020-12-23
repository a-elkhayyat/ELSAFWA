from .models import *
from django import forms


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        exclude = ['deleted']


class DietDeleteForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['deleted']
