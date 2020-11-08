from .models import *
from django.forms import *


class LabTestForm(ModelForm):
    class Meta:
        model = LabTest
        exclude = ['deleted']


class LabTestDeleteForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ['deleted']


class LabTestAttributeForm(ModelForm):
    class Meta:
        model = LabTestAttribute
        exclude = ['lab_test']

