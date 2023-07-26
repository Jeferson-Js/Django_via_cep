# cep_api/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse

def get_cep(request):
    if request.method == 'GET' and 'cep' in request.GET:
        cep = request.GET['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)
    return render(request, 'home/index.html')
