from rest_framework.serializers import ModelSerializer
from .models import *


class LabTestSerializer(ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'
