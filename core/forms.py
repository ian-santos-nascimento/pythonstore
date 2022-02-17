from django import forms
from .models import Produto
from django.core.mail.message import EmailMessage


class ContatoFormulario(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label="email", max_length=100)
    assunto = forms.CharField(label="assunto")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

    def send(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome = {nome}; \n Email = {email}; \n Assunto = {assunto}; \n Mensagem = {mensagem}; \n '

        mail = EmailMessage(subject='Email Enviado pelo sistema backend',
                            body=conteudo,
                            from_email='contato@algo.com.br',
                            to=['contato@algo.com.br', ], headers={'Reply-to': email})
        mail.send()
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields= ["nome", "preco", "estoque", "imagem"]