from django import forms

from .models import *


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['deleted']

        widgets = {
            'instance': forms.HiddenInput()
        }


class ServiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['deleted']
