# app_cartas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carta # ¡Importa el nuevo modelo!

# Listar cartas
def index(request):
    cartas = Carta.objects.all()
    # Pasa la lista de 'cartas' al template renombrado 'listar_cartas.html'
    return render(request, 'listar_cartas.html', {'cartas': cartas})

# Ver carta (Opcional, si quieres ver detalle)
def ver_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    # NOTA: No creaste el template 'ver_carta.html', si no lo vas a usar, puedes borrar esta función
    return render(request, 'ver_carta.html', {'carta': carta})

# Agregar carta
def agregar_carta(request):
    if request.method == 'POST':
        # Captura los nuevos campos
        nombre_carta = request.POST['nombre_carta']
        rareza = request.POST['rareza']
        condicion = request.POST['condicion']
        precio_compra = request.POST['precio_compra']
        id_expansion = request.POST['id_expansion']
        
        # Crea y guarda el nuevo objeto Carta
        Carta.objects.create(
            nombre_carta=nombre_carta, 
            rareza=rareza, 
            condicion=condicion,
            precio_compra=precio_compra,
            id_expansion=id_expansion
        )
        return redirect('inicio')
    return render(request, 'agregar_carta.html')

# Editar carta
def editar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    if request.method == 'POST':
        # Actualiza los campos
        carta.nombre_carta = request.POST['nombre_carta']
        carta.rareza = request.POST['rareza']
        carta.condicion = request.POST['condicion']
        carta.precio_compra = request.POST['precio_compra']
        carta.id_expansion = request.POST['id_expansion']
        
        carta.save()
        return redirect('inicio')
    return render(request, 'editar_carta.html', {'carta': carta})

# Borrar carta
def borrar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    if request.method == 'POST':
        carta.delete()
        return redirect('inicio')
    return render(request, 'borrar_carta.html', {'carta': carta})