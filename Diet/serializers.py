from rest_framework.serializers import ModelSerializer
from .models import Diet


class DietSerializer(ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'
