from django.contrib import admin
from django.urls import path
from home_maintenance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name="home"),
    path('about', views.aboutUs,name="about"),
    path('contact', views.contact,name="contact"),
    path('services', views.services,name="services"),
]
