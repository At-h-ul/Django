from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from services.models import ServiceEnquiry


def dashboard(request):
    service_enquiries = ServiceEnquiry.objects.all()
    return render(request, 'dashboard.html', {'service_enquiries': service_enquiries})


def signin(request):

    if request.method=="POST":
       username=request.POST['username']
       password = request.POST['password']
       user=auth.authenticate(username=username, password=password)
       if user is not None:
          auth.login(request,user)
          return redirect('dashboard')
       else:
          return redirect('signin')
    
    return render(request, 'signin.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save();
        return redirect('signin')
    
    else:
     return render(request,'signup.html') 
    

def signout(request):
   auth.logout(request)
   return redirect('signin')