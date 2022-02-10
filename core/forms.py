from django import forms


class ContatoFormulario(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label="email", max_length=100)
    assunto = forms.CharField(label="assunto")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())


