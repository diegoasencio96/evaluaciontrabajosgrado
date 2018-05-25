# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *
from forms import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        
        (
            None, {
                'fields': (
                    'codigo_docente',
                    'cedula',
                    'fecha_nacimiento',
                    
                )
            }
        ),
    )
@admin.register(User)

class UserAdmin(CustomUserAdmin):
    list_display =  [
        'codigo_docente',
        'cedula',
        'email',
        'username',
        'password',
        'first_name',
        'last_name',
        'fecha_nacimiento',
        'is_staff',
        'is_active',
        'is_superuser',
        'last_login',
        'date_joined'
    ]

# Register your models here.

admin.site.register(Programa)

admin.site.register(Estudiante)