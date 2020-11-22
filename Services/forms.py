from django.forms import ModelForm
from .models import *


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


