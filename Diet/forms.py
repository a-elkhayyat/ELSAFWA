from .models import *
from django import forms


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        exclude = ['deleted']
        widgets = {
            'instance': forms.HiddenInput()
        }


class DietDeleteForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['deleted']
