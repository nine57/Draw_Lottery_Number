from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Number


class NumberSerializer(ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'
