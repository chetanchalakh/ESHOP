from email.headerregistry import Address
from itertools import product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# importing form here
from store.forms import CustomerProfileForm, Signupform
from django.contrib import messages
from django.shortcuts import render , HttpResponseRedirect
from store.forms import Signupform ,Edituserprofile
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm ,SetPasswordForm ,UserChangeForm
from django.contrib.auth import authenticate , login , logout ,update_session_auth_hash 
from django.contrib import messages
from django.contrib.auth.models import User
from store.forms import Bookentry
from django.views import View

# importing model here
from store.models.product import Product
from store.models.catagory import Catagory
from store.models.Cart import Cart 
from store.models.Customer import Customer
from store.models.orderplaced import OrderPlaced


# Create your views here.


def index(request):
    if request.user.is_staff == False:
        products=None
        # products = get_all_product()
        catagory = Catagory.get_all_catagory()
        catagoryID=request.GET.get('catagory')
        
        if catagoryID:
            products=Product.get_all_products_by_catagory_id(catagoryID)
        else:
            products =Product.get_all_product()
        # data={}
        # data['product']=products 
        # data['catagory']=catagorys 
        return render(request,'store/index.html',{'product':products,'catagory':catagory})
    else:
        return HttpResponseRedirect('/addshow')
      
    
# about function
def about(request):
    if request.user.is_staff == False:
     return render(request,'store/about.html')
    else:
        return HttpResponseRedirect('/addshow')



# @login_required(login_url='login')
def contact(request):
    if request.user.is_staff == False:
     user=request.user
     return render(request,'store/contact.html',{'user':user})
    else:
        return HttpResponseRedirect('/addshow')

# user info 
def info(request,id):
    if request.user.is_staff == False:
        pi=Product.objects.get(pk=id)
        products =Product.get_all_product()
        # fm=StudentRegistartion(instance=pi) 
        return render(request,'store/info.html',{'pi':pi,'product':products})
    else:
        return HttpResponseRedirect('/addshow')
    
# signup form  
def Signup(request):
    if request.user.is_staff == False:
        if request.method == 'POST':
            fm=Signupform(request.POST)
            if fm.is_valid():
                messages.success(request,'Account has been created')
                fm.save()
                fm=Signupform()
        else:
            fm=Signupform()
        return render(request,'store/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/addshow/')
        



#login view function 
def user_login(request):
        if not request.user.is_authenticated: 
                if request.method == 'POST':
                    fm=AuthenticationForm(request=request,data=request.POST)
                    if fm.is_valid():
                        uname=fm.cleaned_data['username']
                        upass=fm.cleaned_data['password']
                        user = authenticate(username=uname,password=upass)
                        if user is not None:
                            login(request,user)
                            messages.success(request,'Logged in sucessfully')
                            if request.user.is_staff == True:
                             return HttpResponseRedirect('/addshow/')
                            else:
                              return HttpResponseRedirect('/profile')
                else:
                    fm=AuthenticationForm()
                return render(request,'store/login.html',{'form':fm})
         
        
        else:
            if request.user.is_staff == True: 
                return  HttpResponseRedirect('/addshow')
            else:
                return HttpResponseRedirect('/profile')              




#user Logout function 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/') 


     
# user profile function 
def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":   
            fm=Edituserprofile(request.POST,instance=request.user)

            if fm.is_valid():
             messages.success(request,'Profile has been Updated')
             fm.save()
        else: 
            fm=Edituserprofile(instance=request.user)
    
        
            user=None    
        return render(request,'store/profile.html',{'name':request.user,'form':fm })
    else:
        return HttpResponseRedirect('/login/')             




#this is an addresss function 
def address(request):
    if request.user.is_staff == False:
        if request.user.is_authenticated:
            if request.method=="POST": 
                address= CustomerProfileForm(request.POST)
                user=request.user
                if address.is_valid():
                    name=address.cleaned_data['name']
                    locality=address.cleaned_data['locality']
                    city=address.cleaned_data['city']
                    zipcode=address.cleaned_data['zipcode']
                    state=address.cleaned_data['state']
                    reg=Customer(user=user,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
                    reg.save()
                    address=CustomerProfileForm()
                    #this shoud be same while you print blank form else part
                
                
            else:
                address=CustomerProfileForm()
            user=request.user
            user_address=Customer.objects.filter(user=user)
            return render(request,'store/address.html',{'addressform':address,'user_address':user_address})
                
        else:
            return HttpResponseRedirect('/login/')       
    else:
        return HttpResponseRedirect('/addshow')
        
##  delete adrdress for customer function 
def address_delete(request,id):
    if request.user.is_staff == False:
        if request.method == 'POST':
            pi=Customer.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/address')   
    else:
        return HttpResponseRedirect('/addshow')


# add to cart function
def addtocart(request):
    if request.user.is_staff == False:
        if request.user.is_authenticated:
            user=request.user
            product=request.GET.get('product')
            product=Product.objects.get(id=product)
                
            Cart(user=user,product=product).save()
        
            return HttpResponseRedirect('/showcart/') 
        else:
            return HttpResponseRedirect('/login/')  
    else:
        return HttpResponseRedirect('/addshow')
# show to cart function
def showcart(request):
    if request.user.is_staff == False:
        if request.user.is_authenticated:
            user=request.user
            cart=Cart.objects.filter(user=user)
            amount=0.0
            shipping_amount=40.0
            total_amount=0.0
            cart_product=[ p for p in Cart.objects.all() if p.user ==user]
            if cart_product:
                for p in cart_product:    
                    tempamount=(p.quantity * p.product.price)
                    amount += tempamount
                    totalamount=amount+shipping_amount
                return render(request,'store/addtocart.html',{'cart':cart,'totalamount':totalamount,'amount':amount}) 
            else:
                empty='Your Cart is Empty'
                return render(request,'store/addtocart.html',{'empty':empty})
           
           
       
        else:
            return HttpResponseRedirect('/login/')     
    else:
        return HttpResponseRedirect('/addshow') 
        


#this function is for adding new book an show item
@login_required(login_url='login')
def add_show(request):
    if request.user.is_staff == True:
    
     if request.method == 'POST':
        fm = Bookentry(request.POST,request.FILES)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            an=fm.cleaned_data['auth_name']
            pr=fm.cleaned_data['price']
            cg=fm.cleaned_data['catagory']
            im=fm.cleaned_data['image']
            ds=fm.cleaned_data['description']
            reg=Product(name=nm,auth_name=an,price=pr,catagory=cg,description=ds,image=im)
            reg.save()  
            fm = Bookentry() 
            return HttpResponseRedirect('/') 
            
        # we can use this method also fm.save()
     else:    
        fm = Bookentry()
     stud = Product.objects.all()
        # stud ko else ke baher lagana chahiye
     return render(request,'store/addshow.html',{'form':fm,'stu':stud}) 
    else:
        return HttpResponseRedirect('/')  


#  staff delete function for book 
@login_required(login_url='login')
def delete(request,id):
    if request.user.is_staff == True:
        if request.user.is_authenticated:
          if request.method == 'POST':
            
             pi=Product.objects.get(pk=id)
             pi.delete()
             return HttpResponseRedirect('/addshow')
        else:
            return HttpResponseRedirect('/login/')      
         
    else:
        return HttpResponseRedirect('/')     

#update book
# def updatebook(request,id):
#         pi=Product.objects.get(pk=id)
#         # fm=StudentRegistartion(instance=pi) 
#         return render(request,'store/updatebook.html',{'pi':pi})
#update book for staff
@login_required(login_url='login')
def updatebook(request,id):
    if request.user.is_staff == True:
        if request.method =="POST":
            pi=Product.objects.get(pk=id)
            fm=Bookentry(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi=Product.objects.get(pk=id)
        fm=Bookentry(instance=pi) 
        return render(request,'store/updatebook.html',{'form':fm})
    else:
        return HttpResponse('soory you are not Authorize') 
        
    # request.method =="POST":

# User Removing  book from cart
def remove(request,id):
    if request.method == 'POST':
        pi=Cart.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/showcart')
    
# User Placed order checkout function
@login_required(login_url='login')
def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_item=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=40.0
    totalamount=0.0
    cart_product=[ p for p in Cart.objects.all() if p.user ==request.user]
    if cart_product:
     for p in cart_product:    
        tempamount=(p.quantity * p.product.price)
        amount+= tempamount
        totalamount=amount+shipping_amount
    return render(request,'store/checkout.html',{'add':add,'cart':cart_item,'totalamount':totalamount})

# User Placed order checkout function
@login_required(login_url='login')
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
        messages.success(request,'Order Placed sucessfully')
      
    return redirect('order')
@login_required(login_url='login')
def order(request):
    if request.user.is_staff == False:
        op=OrderPlaced.objects.filter(user=request.user)
        if op:
         return render(request,'store/order.html',{'order_placed':op})
        else:
            empty='No order placed '
            return render(request,'store/order.html',{'empty':empty})
    else:
        return HttpResponseRedirect('/addshow') 
    
          
      
      
      
# User Cancel Item from cart
def cancel_item(request,id):
    if request.method == 'POST':
        pi=OrderPlaced.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/order')
      
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def index(request):
#     products=None
#     # products = get_all_product()
#     catagory = Catagory.get_all_catagory()
#     catagoryID=request.GET.get('catagory')
    
#     if catagoryID:
#         products=Product.get_all_products_by_catagory_id(catagoryID)
#     else:
#         products =Product.get_all_product()
#     # data={}
#     # data['product']=products 
#     # data['catagory']=catagorys 
#     return render(request,'store/index.html',{'product':products,'catagory':catagory})