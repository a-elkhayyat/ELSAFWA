from .models import *
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['deleted']
        widgets = {
            'instance': forms.HiddenInput(),
        }


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['deleted']
