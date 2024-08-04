from django.shortcuts import render
from productos.models import Producto

def mostrarListado(request):
    pro = Producto.objects.all().values()
    print(pro)
    datos = { 'pro' : pro}
    return render(request, 'productos/listado.html', datos)

def mostrarFormRegistrar(request):
    return render(request, 'productos/form_registrar.html')

def mostrarFormActualizar(request, id):
    try:
        pro = Producto.objects.get(id = id)
        print(pro)
        datos = { 'pro' : pro}
        return render(request, 'productos/form_actualizar.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = {
            'pro' : pro,
            'r2' : 'El ID ('+str(id)+') No existe... imposible actualizar!!!',
        }
        return render(request, 'productos/listado.html', datos)

def insertarProducto(request):
    if request.method == 'POST':
        try:
            nom = request.POST.get('txtnom')
            mar = request.POST.get('cbomar')
            pre = request.POST.get('txtpre')
            
            if not nom or not mar or not pre:
                raise ValueError("Todos los campos son obligatorios")
            
            pro = Producto(nombre=nom, marca=mar, precio=pre)
            pro.save()
            datos = {'r': 'Registro realizado correctamente!'}
        except ValueError as e:
            datos = {'r2': str(e)}
        except Exception as e:
            datos = {'r2': f"Error al guardar el producto: {e}"}
        return render(request, 'productos/form_registrar.html', datos)
    else:
        datos = {'r2': 'No se puede procesar solicitud!!!'}
        return render(request, 'productos/form_registrar.html', datos)
    
    
def actualizarProducto(request, id):
    if request.method == 'POST':
        try:
            nom = request.POST.get('txtnom')
            mar = request.POST.get('cbomar')
            pre = request.POST.get('txtpre')
            
            if not nom or not mar or not pre:
                raise ValueError("Todos los campos son obligatorios")
            
            pro = Producto.objects.get(id = id)
            pro.nombre = nom
            pro.marca = mar
            pro.precio = pre
            pro.save()
            pro = Producto.objects.all().values()
            datos = {
                'r': 'Datos modificados correctamente!',
                'pro': pro,
            }
            return render(request, 'productos/listado.html', datos)
        except ValueError as e:
            datos = {'r2': str(e)}
        except Exception as e:
            datos = {'r2': f"Error al guardar el producto: {e}"}
        return render(request, 'productos/listado.html', datos)
    else:
        datos = {'r2': 'No se puede procesar solicitud!!!'}
        return render(request, 'productos/listado.html', datos)

def eliminarProducto(request, id):
    try:
        pro = Producto.objects.get(id = id)
        pro.delete()
        
        pro = Producto.objects.all().values()
        datos = {
            'r': 'Registro eliminado correctamente',
            'pro': pro,
        }
        return render(request, 'productos/listado.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = {
            'r2': 'El ID (' +str(id)+ ') no existe. Imposible eliminar!!!',
            'pro': pro,
        }
        return render(request, 'productos/listado.html', datos)
