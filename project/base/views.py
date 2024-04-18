from django.shortcuts import render
from django.shortcuts import render
from .models import WebsiteDetails


def home(request):
    webdetails = WebsiteDetails.objects.all()
    return render(request, 'index.html', {'webdetails': webdetails})


def aboutus(request):
    webdetails = WebsiteDetails.objects.all()
    return render(request, 'about.html', {'webdetails': webdetails})


def contactus(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')
