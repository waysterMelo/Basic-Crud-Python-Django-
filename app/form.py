from django.forms import *
from app.models import *


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'cpf', 'estado', 'cidade', 'cep', 'endereco', 'numero', 'email', 'contato']


class MotoForm(ModelForm):
    class Meta:
        model = Motocicletas
        fields = ['modelo', 'marca', 'placa', 'preco', 'estado']


class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = ['cliente', 'motocicleta', 'dataVenda']