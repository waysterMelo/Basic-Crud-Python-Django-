from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.IntegerField()
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    cep = models.IntegerField()
    endereco = models.CharField(max_length=30)
    numero = models.IntegerField()
    email = models.CharField(max_length=150)
    contato = models.CharField(max_length=100)


class Motocicletas(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=100)
    preco = models.FloatField()
    estado = models.CharField(max_length=50)


class Vendas(models.Model):
    cliente = models.CharField(max_length=50)
    motocicleta = models.CharField(max_length=100)
    dataVenda = models.CharField(max_length=200)
