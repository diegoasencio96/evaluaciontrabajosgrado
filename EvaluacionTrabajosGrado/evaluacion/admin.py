# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from evaluacion.models import *
from proyecto.models import TrabajoGrado
# Register your models here.


class EvaluacionAdmin(admin.ModelAdmin):
    list_filter = ['trabajo_grado']

admin.site.register(CalificacionProyecto)

admin.site.register(EvaluacionProyecto, EvaluacionAdmin)
