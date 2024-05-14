from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services.models import ServiceEnquiry

@login_required
def dashboard(request):
    if request.session.get('user_logged_in'):
      service_enquiries = ServiceEnquiry.objects.filter(user=request.user)
      return render(request, 'dashboard.html', {'service_enquiries': service_enquiries})
    else:
       return redirect('signin')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # Check if the user is already logged in
            if not request.session.get('user_logged_in'):
                auth.login(request, user)
                # Set a session variable to mark the user as logged in
                request.session['user_logged_in'] = True
                return redirect('dashboard')
            else:
                messages.error(request, 'User is already logged in.')
                return redirect('signin')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        email=request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if not username or not email  or not first_name or not password:
            messages.error(request, 'Please fill in all the fields.')
            return redirect('signup')

        if password != password1:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')

        user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
        user.save();
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('signin')
    
    else:
     return render(request,'signup.html') 
    

def signout(request):
    if request.session.get('user_logged_in'):
        auth.logout(request)
        # Clear the session variable indicating user login status
        del request.session['user_logged_in']
    return redirect('signin')