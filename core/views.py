from django.shortcuts import render
from .models import Produto

def Index(request):
    produtos = Produto.objects.all()
    contexto = {
        'curso': "Curso da Udemy",
        'produtos': produtos
    }
    return render(request, "index.html", contexto)

def Produtos(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)