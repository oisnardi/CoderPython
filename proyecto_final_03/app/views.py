from django.shortcuts import render, redirect
from .models import Artista, Disco, Cancion
from .forms import ArtistaForm, DiscoForm, CancionForm

def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_artista')
    else:
        form = ArtistaForm()

    return render(request, 'agregar_artista.html', {'form': form})

def agregar_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_disco')
    else:
        form = DiscoForm()

    return render(request, 'agregar_disco.html', {'form': form})

def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cancion')
    else:
        form = CancionForm()

    return render(request, 'agregar_cancion.html', {'form': form})

def buscar_bd(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        resultados = Artista.objects.filter(nombre__icontains=query)
    else:
        resultados = []

    return render(request, 'buscar_bd.html', {'resultados': resultados})
