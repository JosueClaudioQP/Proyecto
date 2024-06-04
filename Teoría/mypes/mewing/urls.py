from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('agregar_categoria', views.agregar_categoria, name='agregar_categoria'),
    path('vender_producto', views.vender_producto, name='vender_producto'),
    path('delete/<int:id>', views.eliminar, name='eliminar'), 
]