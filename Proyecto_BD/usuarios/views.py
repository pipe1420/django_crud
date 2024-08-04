# usuarios/views.py

from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import Usuario
from .forms import UsuarioForm

def mostrarIndexUsuarios(request):
    return render(request, 'usuarios/index.html')

def listarUsuarios(request):
    usu = Usuario.objects.all().values()
    print(usu)
    datos = { 'usu' : usu}
    return render(request, 'usuarios/listado.html', datos)
    
def mostrarFormRegistrarUsuario(request):
    return render(request, 'usuarios/form_registrar.html')

def mostrarFormActualizarUsuario(request, id):
    try:
        usu = Usuario.objects.get(id = id)
        print(usu)
        datos = { 'usu' : usu}
        return render(request, 'usuarios/form_actualizar.html', datos)
    except:
        usu = Usuario.objects.all().values()
        datos = {
            'usu' : usu,
            'r2' : 'El ID ('+str(id)+') No existe... imposible actualizar!!!',
        }
        return render(request, 'usuarios/listado.html', datos)

def insertarUsuario(request):
    if request.method == 'POST':
        try:
            nom = request.POST.get('txtnom')
            mail = request.POST.get('txtemail')
            cont = request.POST.get('txtpass')
            
            if not nom or not mail or not cont:
                raise ValueError("Todos los campos son obligatorios")
            
            usu = Usuario(nombre=nom, email=mail, contraseña=cont)
            usu.save()
            
            usu = Usuario.objects.all().values() 
            datos = {
                'r': 'Usuario registrado correctamente!',
                'usu': usu,
            }
            return render(request, 'usuarios/form_registrar.html', datos)
        except ValueError as e:
            datos = {'r2': str(e)}
        except Exception as e:
            datos = {'r2': f"Error al guardar el usuario: {e}"}
        return render(request, 'usuarios/form_registrar.html', datos)
    else:
        datos = {'r2': 'No se puede procesar solicitud!!!'}
        return render(request, 'usuarios/form_registrar.html', datos)
    
def eliminarUsuario(request, id):
    try:
        usu = Usuario.objects.get(id = id)
        usu.delete()
        
        usu = Usuario.objects.all().values()
        datos = {
            'r': 'Usuario eliminado correctamente',
            'usu': usu,
        }
        return render(request, 'usuarios/listado.html', datos)
    except:
        usu = Usuario.objects.all().values()
        datos = {
            'r2': 'El ID (' +str(id)+ ') no existe. Imposible eliminar!!!',
            'usu': usu,
        }
        return render(request, 'usuarios/listado.html', datos)

def actualizarUsuario(request, id):
    if request.method == 'POST':
        try:
            nom = request.POST.get('txtnom')
            mail = request.POST.get('txtemail')
            cont = request.POST.get('txtpass')
            
            if not nom or not mail or not cont:
                raise ValueError("Todos los campos son obligatorios")
            
            usu = Usuario.objects.get(id = id)
            usu.nombre = nom
            usu.email = mail
            usu.contraseña = cont
            usu.save()
            usu = Usuario.objects.all().values()
            datos = {
                'r': 'Usuario modificado correctamente!',
                'usu': usu,
            }
            return render(request, 'usuarios/listado.html', datos)
        except:
            usu = Usuario.objects.all().values()
            datos = {
                'r2': f'Error al guard el usuario ({id})!',
                'usu': usu,
            }
            return render(request, 'usuarios/listado.html', datos)
    else:
        datos = {'r2': 'No se puede procesar solicitud!!!'}
        return render(request, 'usuarios/listado.html', datos)