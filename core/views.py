from django.shortcuts import render

def Index(request):
    contexto = {
        'curso': "Curso da Udemy"
    }
    return render(request, "index.html", contexto)