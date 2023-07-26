# cep_api/views.py
import requests
from django.shortcuts import render

def get_cep(request):
    if request.method == 'GET' and 'cep' in request.GET:
        cep = request.GET['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        data = response.json()

        if 'erro' in data:
            return render(request, 'home/index.html', {'erro': True})
        return render(request, 'home/index.html', {'data': data})

    return render(request, 'home/index.html')
