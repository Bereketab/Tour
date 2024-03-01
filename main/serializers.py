# app_name/serializers.py

from rest_framework import serializers
from .models import Destinations, Services

class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'