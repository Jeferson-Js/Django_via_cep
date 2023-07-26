from django.shortcuts import render
import requests 
from django.http import JsonResponse


# Create your views here.
def get_cep(request):
    if request.method =='GET' and 'cep' in request.GET:
        cep = request.GET['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        data = response.json()
        show_result = not data.get('erro')
        return JsonResponse(data)
    return render(request, 'home/index.html')