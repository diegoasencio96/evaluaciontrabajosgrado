# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from evaluacion.models import *
#from proyecto.models import TrabajoGrado
# Register your models here.


admin.site.register(CalificacionProyecto)

@admin.register(EvaluacionProyecto)
class evaluacionAdmin(admin.ModelAdmin):
	raw_id_fields = ("trabajo_grado",)
	list_filter = ("resultado_consolidado",)
	search_fields = ("titulo",)
#admin.site.register(EvaluacionProyecto)
