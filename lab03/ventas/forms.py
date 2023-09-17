# forms.py
from django import forms
from .models import Cliente, Proveedor, TelefonoCliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre', 'direccion_calle', 'direccion_numero', 'direccion_comuna', 'direccion_ciudad']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre', 'direccion_calle', 'direccion_numero', 'direccion_comuna', 'direccion_ciudad', 'telefono', 'pagina_web']

class TelefonoClienteForm(forms.ModelForm):
    class Meta:
        model = TelefonoCliente
        fields = ['telefono'] 