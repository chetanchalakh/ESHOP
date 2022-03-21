from django import views
from django.urls import path
from store import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('info/<int:id>',views.info,name='info'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('address/',views.address,name='address'),
    path('address_delete/<int:id>',views.address_delete,name='address_delete'),
    
    path('logout/',views.user_logout,name='logout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact),
    path('addshow/',views.add_show,name='addshow'),
    path('update/<int:id>',views.updatebook,name='updatebook'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('showcart/',views.showcart,name='showcart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('order/',views.order,name='order'),
    path('cancel_item/<int:id>/',views.cancel_item,name='cancel_item'),

]