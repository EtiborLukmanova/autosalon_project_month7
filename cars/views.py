from django.shortcuts import render
from .serializers import CarsSerializer,CustomersSerializer,CarCustomerSerializer
from rest_framework.views import APIView
from .models import CarsModel,CarCustomerModel,CustomersModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

# Create your views here.


class CarsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cars = CarsModel.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarsDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        cars = CarsModel.objects.get(pk=pk)
        serializer = CarsSerializer(cars)
        return Response(serializer.data)
    
    def put(self, request, pk):
        cars = CarsModel.objects.get(pk=pk)
        serializer = CarsSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cars = CarsModel.objects.get(pk=pk)
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomersView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customers = CustomersModel.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomersDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        customers = CustomersModel.objects.get(pk=pk)
        serializer = CustomersSerializer(customers)
        return Response(serializer.data)
    
    def put(self, request, pk):
        customers = CustomersModel.objects.get(pk=pk)
        serializer = CustomersSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        customers = CustomersModel.objects.get(pk=pk)
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CarCustomerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        car_customers = CarCustomerModel.objects.all()
        serializer = CarCustomerSerializer(car_customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CarCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarCustomerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        car_customers = CarCustomerModel.objects.get(pk=pk)
        serializer = CarCustomerSerializer(car_customers)
        return Response(serializer.data)
    
    def put(self, request, pk):
        car_customers = CarCustomerModel.objects.get(pk=pk)
        serializer = CarCustomerSerializer(car_customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        car_customers = CarCustomerModel.objects.get(pk=pk)
        car_customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    