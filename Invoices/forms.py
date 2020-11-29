from django import forms
from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        exclude = [
            'patient',
            'service',
            'visits_added',
            'visits_used',
            'added_by',
        ]
        widgets = {
            'instance': forms.HiddenInput(),
        }
