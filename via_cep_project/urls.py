from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.get_cep, name='get_cep')
]