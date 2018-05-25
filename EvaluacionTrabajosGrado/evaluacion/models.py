# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from proyecto.models import *
# Create your models here.

class CalificacionProyecto(models.Model):
    nombre_calificacion_proyecto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_calificacion_proyecto.encode("utf-8")

class EvaluacionProyecto(models.Model):
    trabajo_grado = models.ForeignKey(TrabajoGrado,  null=False, on_delete=models.CASCADE)
    titulo = models.BooleanField()
    descripcion_problema = models.BooleanField()
    hipotesis = models.BooleanField()
    objetivos_generales = models.BooleanField()
    objetivos_especificos = models.BooleanField()
    justificacion = models.BooleanField()
    marco_de_referencia_teorico_conceptual = models.BooleanField()
    metodologia = models.BooleanField()
    resultados_esperados = models.BooleanField()
    cronograma_de_actividades = models.BooleanField()
    recursos_o_presupuesto = models.BooleanField()
    literatura_citada = models.BooleanField()
    redaccion_y_ortografia = models.BooleanField()
    pertenece_al_area_formacion_estudiante = models.BooleanField()
    recomendaciones_observaciones_correciones = models.TextField( null=True, blank=True)
    resultado_consolidado = models.ForeignKey(CalificacionProyecto,  null=True, blank=True, related_name="%(class)s_resultado_consolidado", on_delete=models.CASCADE)
