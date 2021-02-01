from .models import *
from django.forms import ModelForm


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        exclude = ['deleted']


class MedicineDeleteForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['deleted']


class DoseForm(ModelForm):
    class Meta:
        model = Dose
        fields = '__all__'


class TimingForm(ModelForm):
    class Meta:
        model = Timing
        fields = '__all__'
