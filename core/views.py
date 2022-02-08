from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Produto

def Index(request):
    produtos = Produto.objects.all()
    contexto = {
        'curso': "Curso da Udemy",
        'produtos': produtos
    }
    return render(request, "index.html", contexto)

def Produtos(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id = pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template, content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template, content_type='text/html; charset=utf8', status=500)
