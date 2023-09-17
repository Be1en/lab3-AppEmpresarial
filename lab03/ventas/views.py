from django.shortcuts import redirect, render
from .models import Cliente, Proveedor, Venta, Producto, TelefonoCliente
from .forms import ClienteForm, ProveedorForm, TelefonoClienteForm

def index(request):
    return render(request, 'ventas/index.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    telefonos = TelefonoCliente.objects.all()
    context = {
        'clientes': clientes,
        'telefonos': telefonos
    }
    return render(request, 'ventas/clientes.html', context)

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores': proveedores
    }
    return render(request, 'ventas/proveedores.html', context)
def ventas_view(request):
    ventas = Venta.objects.all()
    context = {
        'ventas': ventas
    }
    return render(request, 'ventas/ventas.html', context)
def productos_view(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'ventas/productos.html', context)

def ingresar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Guardar el cliente
            cliente = form.save()
            # Crear un teléfono para el cliente y relacionarlo
            telefono_form = TelefonoClienteForm(request.POST)
            if telefono_form.is_valid():
                telefono = telefono_form.save(commit=False)
                telefono.cliente = cliente  # Relacionar el teléfono con el cliente
                telefono.save()

            return redirect('clientes.html')  # Redirigir a la vista de clientes

    else:
        form = ClienteForm()
        telefono_form = TelefonoClienteForm()  # Agregar un formulario para el teléfono
    
    context = {
        'form': form,
        'telefono_form': telefono_form  # Pasar el formulario de teléfono al contexto
    }
    return render(request, 'ventas/ingresar_cliente.html', context)

def ingresar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores.html')
    else:
        form = ProveedorForm()
    
    context = {
        'form': form
    }
    return render(request, 'ventas/ingresar_proveedor.html', context)