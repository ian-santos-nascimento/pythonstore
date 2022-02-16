from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.contrib import messages

from .models import Produto

from .forms import ContatoFormulario, ProdutoModelForm


def index(request):
    produtos = Produto.objects.all()
    contexto = {
        'curso': "Curso da Udemy",
        'produtos': produtos
    }
    return render(request, "index.html", contexto)


def produtos(request):

    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Salvo com sucesso")
            form = ProdutoModelForm
        else:
            print("Não é valido")
    else:
        form = ProdutoModelForm
        context = {
            'form': form
        }
    return render(request, 'produto.html', context)


def contato_novo(request):
    formulario = ContatoFormulario(request.POST or None)

    if (request.method == 'POST'):
        if formulario.is_valid():
            formulario.send()
            formulario = ContatoFormulario()
            messages.success(request, "Enviado com sucesso")
        else:
            messages.error(request, "Não foi enviado com sucesso")
    context = {
        'form': formulario,
        'mensagem': "Prolema no formulário"
    }
    return render(request, 'contato.html', context=context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template, content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template, content_type='text/html; charset=utf8', status=500)
