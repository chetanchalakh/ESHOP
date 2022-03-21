from cProfile import label
import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from store.models.product import Product

# Create your models here.
# class Book(models.Model):
#     name=models.CharField(max_length=50,label='Book Name')
#     password=models.CharField(max_length=50)
#     description=models.CharField(max_length=500)
    
# class Cart(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)
    
#     def __str__(self):
#         return str(self.id)
    