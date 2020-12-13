from django import forms
from .models import *


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
