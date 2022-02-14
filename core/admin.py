from django.contrib import admin
from .models import Produto


@admin.register(Produto) #Decorator
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco","estoque","ativo")