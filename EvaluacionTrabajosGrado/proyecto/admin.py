# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

from evaluacion.models import EvaluacionProyecto
# Register your models here.

class EvaluacionInline(admin.TabularInline):
    model = EvaluacionProyecto
    extra = 1

class TrabajoGradoAdmin(admin.ModelAdmin):
    inlines = [EvaluacionInline]

admin.site.register(OpcionDeGrado)

admin.site.register(TrabajoGrado, TrabajoGradoAdmin)