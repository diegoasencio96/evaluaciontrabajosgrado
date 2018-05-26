# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from universidad.models import Programa, User, Estudiante
#from evaluacion.models import EvaluacionProyecto
# Create your models here.


class OpcionDeGrado(models.Model):
    id_opcion_grado = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_opcion_de_grado = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.nombre_opcion_de_grado.encode("utf-8")



class TrabajoGrado(models.Model):
    #id_trabajo_grado = models.CharField(max_length=10, primary_key=True, null=False)
    estudiante1 = models.ForeignKey(Estudiante, related_name="%(class)s_estudiante1", on_delete=models.CASCADE)
    estudiante2 = models.ForeignKey(Estudiante, null=True, blank=True, related_name="%(class)s_estudiante2", on_delete=models.CASCADE)
    opcion_de_grado = models.ForeignKey(OpcionDeGrado, null=False, on_delete=models.CASCADE)
    nombre_trabajo_de_grado = models.CharField(max_length=50, null=False, unique=True)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)
    director = models.ForeignKey(User, null=False, related_name="%(class)s_director", on_delete=models.CASCADE)
    codirector = models.ForeignKey(User, null=True, blank=True, related_name="%(class)s_codirector", on_delete=models.CASCADE)
    jurado1 = models.ForeignKey(User, null=False, related_name="%(class)s_jurado1", on_delete=models.CASCADE)
    jurado2 = models.ForeignKey(User, null=True, blank=True, related_name="%(class)s_jurado2", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_trabajo_de_grado.encode("utf-8")

    def save(self, *args, **kwargs):
        '''
        evaluacion = User.objects.create(trabajo_grado=self.id)
        evaluacion.save()
        '''
    	return super(TrabajoGrado, self).save( *args, **kwargs)  # llamada al save() original con sus parámetros correspondientes


from evaluacion.models import EvaluacionProyecto

from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=TrabajoGrado)
def socket(sender,instance,created,**kwargs):
    evaluacion = EvaluacionProyecto.objects.get_or_create(
        trabajo_grado = instance,
        
        )
