from django.db import models 
from django.contrib.auth.models import AbstractUser

class Bills(models.Model):  
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()

class BillDetails(models.Model):
    id_product = models.IntegerField()
    quantity = models.IntegerField()
    bill_id = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=500)
    note = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    vote = models.IntegerField()
    image = models.CharField(max_length=100)
    type = models.IntegerField()

class CustomUser(AbstractUser): 
    
    email = models.EmailField(unique=True)

    def get_username(self) -> str:
        return str(self.username)

    def get_email(self) -> str:
        return self.email