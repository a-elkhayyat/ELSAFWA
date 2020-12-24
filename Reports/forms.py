from django import forms
from Invoices.models import *
from django.utils.timezone import now


class FromToForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='من',
                                initial=now().date().replace(day=1))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='إلي', initial=now().date())
