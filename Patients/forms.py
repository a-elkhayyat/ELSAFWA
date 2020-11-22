from django.forms import *
from .models import *


class DateInput(DateInput):
    input_type = 'date'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ['patient_history', 'deleted', 'visits']
        widgets = {
            'instance': HiddenInput(),
            'birthday': DateInput(),
        }


class PatientHistoryForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_history']


class PatientDeleteForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['deleted']


class VitalRecordForm(ModelForm):
    class Meta:
        model = PatientViralProcess
        exclude = ['patient']


class HeightAndWeightForm(ModelForm):
    class Meta:
        model = HeightAndWeight
        fields = ['height', 'weight']


class InvestigationForm(ModelForm):
    class Meta:
        model = PatientInvestigation
        exclude = ['patient']


class LabTestRequestForm(ModelForm):
    class Meta:
        model = LabTestRequest
        exclude = ['patient']


class RadiologyRequestForm(ModelForm):
    class Meta:
        model = RadiologyRequest
        exclude = ['patient']


class RadiologyResultForm(ModelForm):
    class Meta:
        model = RadiologyResult
        exclude = ['radiology']
