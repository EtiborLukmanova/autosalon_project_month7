from rest_framework import serializers
from .models import CarsModel,CustomersModel,CarCustomerModel

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomersModel
        fields = '__all__'

class CarCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCustomerModel
        fields = '__all__'
        