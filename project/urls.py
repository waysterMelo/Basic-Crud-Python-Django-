from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ver_clients/', ver_clientes, name='ver_clientes'),
    path('ver_clients/add_clientes', add_clientes, name='form'),
    path('ver_clients/save_client', create, name='createCliente'),
    path('ver_motocicletas/', ver_motocicletas, name="home_motos"),
    path('ver_motocicletas/add_motors', add_motors, name='motors'),
    path('ver_motocicletas/save_motors', save_motors),
    path('delete/<int:id>', delete_clientes, name='delete_clientes'),
    path('ver_motocicletas/delete_motors/<int:id>', delete_motos, name='delete_motos'),
    path('ver_vendas', verVendas, name='verVendas'),
    path('add_vendas', add_vendas),
    path('save_venda', save_sales)
]
