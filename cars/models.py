from django.db import models

# Create your models here.

class CarsModel(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_year = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.car_name
    
class CustomersModel(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name

class CarCustomerModel(models.Model):
    comment = models.CharField(max_length=100)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomersModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:20]



    