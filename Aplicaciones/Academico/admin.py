"""Importamos los modelos suministrados por django en este caso admin y la clase Curso"""
from django.contrib import admin
from .models import Curso

admin.site.register(Curso)
