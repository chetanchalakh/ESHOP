from email.policy import default
from tkinter import CASCADE
from django.db import models
from setuptools import Require

from .catagory import Catagory

class Product(models.Model):
    name=models.CharField(max_length=50)
    auth_name=models.CharField(max_length=50)
    price=models.IntegerField(default=250)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=800,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')
    

    
    @staticmethod
    def get_all_product():
      return Product.objects.all



    @staticmethod
    def get_all_products_by_catagory_id(catagary_id):
     if catagary_id:
       return Product.objects.filter(catagory=catagary_id)
     else:
       return Product.objects.all