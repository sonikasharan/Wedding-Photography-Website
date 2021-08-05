from django.urls import path
from . import views



urlpatterns=[
   
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('aboutus',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('FAQ',views.FAQ,name='FAQ'),
    
]