# cep_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get_cep/', views.get_cep, name='get_cep'),
]
