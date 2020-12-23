from .models import *
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['deleted']


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['deleted']