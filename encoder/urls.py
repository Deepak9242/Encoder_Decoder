from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload/', views.upload, name='upload'),
    path('decode/', views.decode, name='decode'),
    path('email/' , views.email,  name='email'),
    re_path(r'[a-bA-Z0-9]*',views.error)
]
