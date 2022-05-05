from rest_framework.serializers import ModelSerializer

from .models import Number, Count


class NumberSerializer(ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'


class CountSerializer(ModelSerializer):
    class Meta:
        model = Count
        fields = '__all__'
