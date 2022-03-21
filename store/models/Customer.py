from cProfile import label
import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from store.models.product import Product

STATE_CHOICES=(
    ('Maharashtra','Maharshta'),
    ('	Andhra Pradesh','	Andhra Pradesh'),
    ('	Bihar','	Bihar'),
    ('Chandigarh (UT)','Chandigarh (UT)'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    
    ('	Meghalaya','Meghalaya'),
     ('	Punjab','	Punjab'), ('Rajasthan','Rajasthan'), ('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),('	Uttar Pradesh','	Uttar Pradesh'),('Uttarakhand','Uttarakhand'),('West Bengal','West Bengal'),
    
)


class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField(default=0)
    state=models.CharField(choices=STATE_CHOICES,max_length=60)
    
    def __str__(self):
        return str(self.id)