from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from jjacademy import settings
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('error_404/', views.error_404, name='error_404'),
    
    #path('home/', views.home, name='home'),
    path('', include('lms.urls')),
]

