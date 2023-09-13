from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib import messages

def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')



def customerregistration(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email= request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        #print(email,pass1)
        if pass1!=pass2:
            msg = "confirm password and Password not matched !"
            return render(request,'app/customerregistration.html',{'msg':msg})
            #messages.success(request,"Both passwords are not matched !")
        elif User.objects.filter(username=uname):
            msg1 = "Username is already registered !"
            return render(request,'app/customerregistration.html',{'msg':msg1})
        elif User.objects.filter(email=uname):
            msg2 = "Email is already registered !"
            return render(request,'app/customerregistration.html',{'msg':msg2})
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            messages.success(request,"your account is created")
            return redirect('login')
        
    return render(request, 'app/customerregistration.html')

def Login(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        user = authenticate(request,username=uname,password=pass1)
        #print(user)
        if user is not None:
            login(request,user)
            #return redirect('home')
            fname = user.first_name
            return render(request,'app/home.html',{'fname':fname})
        else:
            #return HttpResponse("username or password id incorrect")
            #messages.success(request,"username or password id incorrect")
            msg = "Incorrect username or password !"
            return render(request,'app/login.html',{'msg':msg})
        
    return render(request, 'app/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

def checkout(request):
 return render(request,'app/checkout.html')
