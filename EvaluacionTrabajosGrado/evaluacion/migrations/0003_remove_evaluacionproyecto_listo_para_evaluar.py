# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-26 16:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0002_evaluacionproyecto_trabajo_grado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacionproyecto',
            name='listo_para_evaluar',
        ),
    ]
