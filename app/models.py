from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    numero_paginas = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")

    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    libros = models.ManyToManyField(Libro, related_name="editoriales")

    def __str__(self):
        return self.nombre