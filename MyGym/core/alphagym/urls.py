from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('membership/',membership,name='membership'),
    path('login/',login_view,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_view,name='logout'),
    path('paymentGateway/',payment_getway,name='payment_getway')
]