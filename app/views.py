from app.form import *
from django.shortcuts import render, redirect
from app.models import *


def home(request):
    return render(request, 'index.html')


def ver_clientes(request):
    data = {}
    data['db'] = Clientes.objects.all()
    return render(request, 'verClientes.html', data)


def add_clientes(request):
    data = {}
    data['form'] = ClientesForm()
    return render(request, 'add_clientes.html', data)


def create(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ver_clientes')


def ver_motocicletas(request):
    data = {}
    data['motos'] = Motocicletas.objects.all()
    return render(request, 'verMotos.html', data)


def add_motors(request):
    data = {}
    data['form'] = MotoForm
    return render(request, 'add_motos_form.html', data)


def save_motors(request):
    form = MotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_motos')


def delete_clientes(request, id):
    db = Clientes.objects.get(id=id)
    db.delete()
    return redirect('ver_clientes')


def delete_motos(request, id):
    db = Motocicletas.objects.get(id=id)
    db.delete()
    return redirect('home_motos')


def verVendas(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['vendas'] = Vendas.objects.filter(cliente__icontains=search)
    else:
        data['vendas'] = Vendas.objects.all()

    return render(request, 'verVendas.html', data)


def add_vendas(request):
    data = {}
    data['form'] = VendasForm()
    return render(request, 'add_vendas.html', data)


def save_sales(request):
    form = VendasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('verVendas')
