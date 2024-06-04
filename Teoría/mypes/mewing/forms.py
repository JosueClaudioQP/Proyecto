from django import forms
from .models import Producto, Categoria, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'categoria']

        def analizar(self):
            nombre = self.cleaned_data.get('nombre')
            if Producto.objects.filter(nombre=nombre).exists():
                raise forms.ValidationError("Ya hay un producto con este nombre, ingrese otro")
            return nombre
        
        def agregar(self, commit = True):
            producto = super().save(commit=False)
            producto.nombre = self.cleaned_data['nombre']
            if commit:
                producto.save()
            return producto

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'descripcion']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad_vendida']