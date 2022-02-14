from datetime import datetime
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify, default
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True,  blank=True)
    modificado = models.DateField('Data de atualização',auto_now_add= True, blank=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True ##Mostra que a classe é abstrata(Não será salva do BD)



class Produto(Base):
    nome = models.CharField("nome", max_length=100)
    preco = models.DecimalField("preço", decimal_places=2, max_digits=10)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField('Imagem', upload_to='produtos', variations= {'thumb':(124, 124)})
    slug = models.SlugField('Slug',max_length=100, blank=True, editable=False)


    def __str__(self):
        return self.nome

def produto_save(signal, instance, sender,  **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_save, sender=Produto) #Indica o que fazer quando receber um sinal do 'Produto'