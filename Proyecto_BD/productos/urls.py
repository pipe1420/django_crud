from django.urls import path
from productos import views

urlpatterns = [
    #path('', views.mostrarIndex),
    path('form_registrar', views.mostrarFormRegistrar),
    path('form_actualizar/<int:id>', views.mostrarFormActualizar),
    path('listado', views.mostrarListado),
    path('insertar', views.insertarProducto),
    path('actualizar/<int:id>', views.actualizarProducto),
    path('eliminar/<int:id>', views.eliminarProducto),
]