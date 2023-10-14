from django.contrib import admin
from .models import CategoriaCur, Curso
from registrarse.models import Estudiantes

# Register your models here.

class CategoriaCurAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class CursoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaCur, CategoriaCurAdmin)

admin.site.register(Curso, CursoAdmin)

admin.site.register(Estudiantes)

    
