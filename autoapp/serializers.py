from rest_framework import serializers
from .models import Cities,Countries,States


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
