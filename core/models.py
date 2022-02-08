from django.db import models


class Produto(models.Model):
    nome = models.CharField("nome", max_length=100)
    preco = models.DecimalField("preço", decimal_places=2, max_digits=10)
    estoque = models.IntegerField("Estoque")

    def __str__(self):
        return self.nome
