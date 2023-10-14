from django.shortcuts import render

from asignaciondecursos.asignaciondecursos import Asignaciondecursos
from .models import Curso

# Create your views here.

def estudiante(request):

    asignaciondecursos=Asignaciondecursos(request)

    cursos=Curso.objects.all()

    return render(request, "estudiante/estudiante.html", {"cursos":cursos})