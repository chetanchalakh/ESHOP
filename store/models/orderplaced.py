from cProfile import label
import email
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from store.models.Customer import Customer
from store.models.product import Product

ORDER_CHOICES=(
    ('order placed','Order Placed'),
    ('	Order confirm','	Order confirm'),
   
    ('Order Packed','Order Packed'),
    ('Order Dispatch','Order Dispatch'),
    ('Order Dilivered','Order Dilivered'),
     ('	Rejected','	Rejected'),


)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=ORDER_CHOICES,default='Order Placed')