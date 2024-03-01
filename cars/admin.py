from django.contrib import admin
from .models import CarCustomerModel,CarsModel,CustomersModel
# Register your models here.

admin.site.register(CarsModel)

admin.site.register(CarCustomerModel)

admin.site.register(CustomersModel)