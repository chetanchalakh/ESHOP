from django import forms
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm,UserChangeForm
from store.models import Customer

from store.models.product import Product
from store.models.Customer import Customer
# user creatioin form
class Signupform(UserCreationForm):
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        labels={'emai':'Email'}
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                }
        
        
    def __init__(self,*args,**kwargs):
        super(Signupform,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    
    
# profile update 
class Edituserprofile(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels={'emai':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                # 'description':forms.TextInput(attrs={'class':'form-control'}),
                # 'image':forms. ClearableFileInput(attrs={'class':'form-control'}),
                }
        
#Books Entry   
class Bookentry(forms.ModelForm):
    class Meta:
        model = Product
        fields=('name','auth_name','price','catagory','description','image')
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'auth_name':forms.TextInput(attrs={'class':'form-control'}),
                'price':forms.NumberInput(attrs={'class':'form-control'}),
                'catagory':forms.Select(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'image':forms. ClearableFileInput(attrs={'class':'form-control'}),
                }
                
#login form
class AuthenticationForm():
    class Meta:
        model = User
        
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        
#Custmer  form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=('name','locality','city','zipcode','state')
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'locality':forms.TextInput(attrs={'class':'form-control'}),
                'city':forms.TextInput(attrs={'class':'form-control'}),
                'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                'state':forms.Select(attrs={'class':'form-control'}),
                }
        