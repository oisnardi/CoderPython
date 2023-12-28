from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Disco(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    año = models.IntegerField()

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    duracion = models.DurationField()

    def __str__(self):
        return self.titulo
