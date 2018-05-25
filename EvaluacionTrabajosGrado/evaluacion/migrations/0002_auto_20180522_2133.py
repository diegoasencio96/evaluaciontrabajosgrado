# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-23 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacionproyecto',
            name='recomendaciones_observaciones_correciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacionproyecto',
            name='resultado_consolidado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluacionproyecto_resultado_consolidado', to='evaluacion.CalificacionProyecto'),
        ),
    ]