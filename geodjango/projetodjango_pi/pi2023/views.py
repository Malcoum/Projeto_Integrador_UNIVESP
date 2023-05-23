from django.shortcuts import render

#Início do exemplo

def index_exemplo(request):
    return render(request, 'pi2023/templates/index_exemplo.html')

# Fim exemplo
