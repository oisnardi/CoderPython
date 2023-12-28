from django.urls import path
from .views import agregar_artista, agregar_disco, agregar_cancion, buscar_bd

urlpatterns = [
    path('agregar/artista/', agregar_artista, name='agregar_artista'),
    path('agregar/disco/', agregar_disco, name='agregar_disco'),
    path('agregar/cancion/', agregar_cancion, name='agregar_cancion'),
    path('buscar/', buscar_bd, name='buscar_bd'),
]
