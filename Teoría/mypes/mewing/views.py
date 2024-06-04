from django.shortcuts import render, redirect
from .models import Producto, Categoria, Venta
from .forms import ProductoForm, CategoriaForms, VentaForm

def index(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'mewing/index.html', {'productos': productos, 'categorias': categorias})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'mewing/agregar_producto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForms()
    return render(request, 'mewing/agregar_categoria.html', {'form': form})

def vender_producto(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            producto = venta.producto
            if producto.stock >= venta.cantidad_vendida:
                producto.stock -= venta.cantidad_vendida
                producto.save()
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'mewing/vender_producto.html', {'form': form})

def eliminar(request, id):
    producto = Venta.objects.get(id=id)
    producto.delete()
    return redirect('index')

def editar(request, id):  
    producto = Producto.objects.get(id=id)  
    form = ProductoForm(request.POST, instance = producto)  
    if form.is_valid():  
        form.save()  
        return redirect("index")
    else:
        form = ProductoForm()
    return render(request, 'mewing/editar.html', {'form': form})  

