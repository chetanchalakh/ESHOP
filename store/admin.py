from django.contrib import admin

from store.models.orderplaced import OrderPlaced
from .models.product import Product
from .models.catagory import Catagory
from .models.Cart import Cart


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','catagory','image')
    
@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('user','product','quantity')
    
@admin.register(OrderPlaced)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','product','quantity','order_date','status')