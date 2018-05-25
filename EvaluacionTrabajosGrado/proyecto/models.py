# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from universidad.models import *
from django.contrib.auth.models import User
# Create your models here.


class OpcionDeGrado(models.Model):
    nombre_opcion_de_grado = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre_opcion_de_grado.encode("utf-8")



class TrabajoGrado(models.Model):
    estudiante1 = models.ForeignKey(Estudiante, related_name="%(class)s_estudiante1", on_delete=models.CASCADE)
    estudiante2 = models.ForeignKey(Estudiante, null=True, blank=True, related_name="%(class)s_estudiante2r", on_delete=models.CASCADE)
    opcion_de_grado = models.ForeignKey(OpcionDeGrado, null=False, on_delete=models.CASCADE)
    nombre_trabajo_de_grado = models.CharField(max_length=50, null=False)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)
    director = models.ForeignKey(Docente, null=False, related_name="%(class)s_director", on_delete=models.CASCADE)
    codirector = models.ForeignKey(Docente, null=True, blank=True, related_name="%(class)s_codirector", on_delete=models.CASCADE)
    jurado1 = models.ForeignKey(User, null=False, related_name="%(class)s_jurado1", on_delete=models.CASCADE)
    jurado2 = models.ForeignKey(User, null=True, blank=True, related_name="%(class)s_jurado2", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_trabajo_de_grado.encode("utf-8")