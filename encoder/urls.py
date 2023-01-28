from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.encode, name='encode'),
    path('upload/', views.upload, name='upload')
]
