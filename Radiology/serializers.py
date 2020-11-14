from .models import *
from rest_framework.serializers import ModelSerializer


class RadiologySerializer(ModelSerializer):
    class Meta:
        model = Radiology
        exclude = ['deleted']