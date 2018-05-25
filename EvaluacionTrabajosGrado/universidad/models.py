# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Programa(models.Model):
    nombre_del_programa = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre_del_programa.encode("utf-8")


class Docente(models.Model):
    codigo_docente = models.CharField(max_length=100, primary_key=True, null=False)
    cedula = models.CharField(max_length=20, null=False, unique=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    correo_principal = models.EmailField(null=False, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres+' '+self.apellidos.encode("utf-8")

class Estudiante(models.Model):
    codigo_estudiante = models.CharField(max_length=100, primary_key=True, null=False)
    identificacion = models.CharField(max_length=20, null=False, unique=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    correo_principal = models.EmailField(null=False, unique=True)
    fecha_nacimiento = models.DateField(null=True,  blank=True)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)
    fecha_sustentacion = models.DateField(null=True,  blank=True)

    def __str__(self):
        return self.nombres+' '+self.apellidos.encode("utf-8")