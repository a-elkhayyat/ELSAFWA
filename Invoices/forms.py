from django import forms
from .models import *


class InvoiceForm(forms.ModelForm):
    old_balance = forms.FloatField(label='الرصيد السابق', required=False)
    remaining = forms.FloatField(label='المتبقي', required=False)

    class Meta:
        model = Invoice
        exclude = [
            'patient',
            'service',
            'visits_added',
            'visits_used',
            'added_by',
            'outcome',
            'category',
            'invoice_type'
        ]
        widgets = {
            'instance': forms.HiddenInput(),
            'price': forms.NumberInput(attrs={'readonly': 'true'}),
            'after_discount': forms.NumberInput(attrs={'readonly': 'true'}),
            'old_balance': forms.NumberInput(attrs={'readonly': 'true'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = OutcomeCategory
        exclude = ['deleted']
        widgets = {
            'instance': forms.HiddenInput(),
        }


class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = OutcomeCategory
        fields = ['deleted']


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'instance',
            'category',
            'outcome',
        ]
        widgets = {
            'instance': forms.HiddenInput(),
        }

