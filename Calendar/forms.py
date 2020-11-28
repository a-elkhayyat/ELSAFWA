from django import forms
from .models import *


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=DateInput(format='%Y-%m-%dT%H:%M'),
        label='الموعد'
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.none()

        if 'patient' in self.data:
            self.fields['patient'].queryset = Patient.objects.filter(deleted=False)

        elif self.instance.patient:
            self.fields['patient'].queryset = Patient.objects.filter(deleted=False, id=self.instance.patient.pk)
