# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin
from evaluacion.models import *
#from proyecto.models import TrabajoGrado
# Register your models here.


admin.site.register(CalificacionProyecto)

@admin.register(EvaluacionProyecto)
class evaluacionAdmin(SummernoteModelAdmin):
	summernote_fields = ('recomendaciones_observaciones_correciones',)
	raw_id_fields = ("trabajo_grado",)
	list_filter = ("resultado_consolidado",)
	search_fields = ("titulo",)

	def get_queryset(self, request):
		qs = super(evaluacionAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		    return qs
		return qs.filter(trabajo_grado__jurado1=request.user)

#admin.site.register(EvaluacionProyecto)
