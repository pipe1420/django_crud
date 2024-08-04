from django.urls import path
from usuarios import views

urlpatterns = [
    #path('', views.listarUsuarios, name='listar_usuarios'),
    path('listado', views.listarUsuarios, name='listar_usuarios'),
    path('form_registrar', views.mostrarFormRegistrarUsuario, name='registrar_usuario'),
    path('form_actualizar/<int:id>', views.mostrarFormActualizarUsuario, name='actualizar_usuario'),
    path('actualizar/<int:id>', views.actualizarUsuario),
    path('eliminar/<int:id>', views.eliminarUsuario, name='eliminar_usuario'),
    path('insertar', views.insertarUsuario),
    path('index', views.mostrarIndexUsuarios, name='index_usuarios'),  # Añadido para la página de inicio de usuarios
]