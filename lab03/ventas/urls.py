from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.index,name='index'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('proveedores/', views.proveedores_view, name='proveedores'),
    path('ventas/', views.ventas_view, name='ventas'),
    path('productos/', views.productos_view, name='productos'),
    path('ingresar_cliente/', views.ingresar_cliente, name='ingresar_cliente'),
    path('ingresar_cliente/clientes.html', views.clientes_view, name='ingresar_cliente/clientes.html'),
    path('ingresar_proveedor/', views.ingresar_proveedor, name='ingresar_proveedor'),
    path('ingresar_proveedor/proveedores.html', views.proveedores_view, name='ingresar_proveedor/proveedores.html'),

]
