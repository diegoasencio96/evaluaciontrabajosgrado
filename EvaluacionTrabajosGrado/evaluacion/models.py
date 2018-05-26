# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from proyecto.models import TrabajoGrado
# Create your models here.

class CalificacionProyecto(models.Model):
    id_calificacion_proyecto = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_calificacion_proyecto = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_calificacion_proyecto.encode("utf-8")

class EvaluacionProyecto(models.Model):
    #id_evaluacion_proyecto = models.CharField(max_length=10, primary_key=True, null=False)
    trabajo_grado = models.ForeignKey(TrabajoGrado,  null=False, on_delete=models.CASCADE)
    listo_para_evaluar = models.BooleanField()
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

    
    def __str__(self):
        return "Evaluacion Proyecto: "+str(self.trabajo_grado).encode("utf-8")