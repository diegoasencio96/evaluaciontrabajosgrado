# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evaluacion', '0001_initial'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacionproyecto',
            name='trabajo_grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.TrabajoGrado'),
        ),
    ]
