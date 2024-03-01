from django.urls import path
from .views import CarsView, CarsDetailView,CustomersView,CustomersDetailView,CarCustomerView,CarCustomerDetailView

urlpatterns = [
    path('cars/', CarsView.as_view(), name='cars'),
    path('car/<int:pk>/', CarsDetailView.as_view(), name='cars-detail'),
    path('customers/', CustomersView.as_view(), name='customers'),
    path('customer/<int:pk>/', CustomersDetailView.as_view(), name='customers-detail'),
    path('car-customer/', CarCustomerView.as_view(), name='car-customer'),
    path('car-customer/<int:pk>/', CarCustomerDetailView.as_view(), name='car-customer-detail'),
]
