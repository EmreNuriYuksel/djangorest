from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=40)
