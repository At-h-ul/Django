from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('service', views.service, name="service"),
    path('newproduct', views.newproduct, name="newproduct"),
    path('oldproduct', views.oldproduct, name="oldproduct"),
    path('demandlaptop', views.demandlaptop, name="demandlaptop"),
    path('demandpc', views.demandpc, name="demandpc"),
    path('demandothers', views.demandothers, name="demandothers"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)