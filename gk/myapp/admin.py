from django.contrib import admin
from .models import  Bills, BillDetails, Category, Product, CustomUser

# Register your models here.
admin.site.register(Bills)
admin.site.register(BillDetails)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CustomUser)