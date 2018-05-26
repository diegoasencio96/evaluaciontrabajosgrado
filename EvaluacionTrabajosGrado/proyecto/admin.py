# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

from evaluacion.models import EvaluacionProyecto
# Register your models here.


admin.site.register(OpcionDeGrado)

@admin.register(TrabajoGrado)
class trabajogradoAdmin(admin.ModelAdmin):
	raw_id_fields = ("estudiante1","estudiante2","director","codirector")

	def get_queryset(self, request):
		qs = super(trabajogradoAdmin, self).get_queryset(request)
		if request.user.is_superuser:
		    return qs
		return qs.filter(jurado1=request.user)