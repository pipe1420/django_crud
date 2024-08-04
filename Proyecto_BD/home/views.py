from django.shortcuts import render

def mostrarIndexHome(request):
    return render(request, 'home/index.html')

