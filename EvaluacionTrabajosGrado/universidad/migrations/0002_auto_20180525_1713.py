# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='nombre_del_programa',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
