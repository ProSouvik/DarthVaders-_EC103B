from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    print(request.user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            msg = request.POST.get('msg')
            print(msg)
            s = comment(user=request.user.first_name, comment=msg)  # assuming user is a field in Comment model
            s.save()
        else:
            return redirect('login')
    return render(request, 'index.html', {'msg': comment.objects.all()})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def membership(request):
    return render(request,'membership.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = User.objects.get(email=email,password=password)
#         if user:
#             login(request,user)
#             print('loged')

#     return render(request,'auth/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(email=email).exists():
            return render(request, 'auth/signup.html')

        user = User.objects.create_user(username=email, email=email, password=password,first_name=name)
        user.save()
        login(request,user)
        
        return redirect('index') 

    return render(request, 'auth/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)


        if user is not None:
            login(request, user)
            return redirect('index')  
            
        
    return render(request, 'auth/login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index')  


def payment_getway(request):
    return render(request, 'paymentGateway.html')