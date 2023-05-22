from django.shortcuts import render

#Início do exemplo

from .models import Localizacao  

def exibir_localizacao(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'exibir_localizacao.html', {'localizacoes': localizacoes})

def index_example(request):
    return render(request, 'index_example.html')

# Fim exemplo
