from django.shortcuts import render, HttpResponse
from asignaciondecursos.asignaciondecursos import Asignaciondecursos

# Create your views here.

def inicio(request):

    asignaciondecursos=Asignaciondecursos(request)

    return render(request, "ProyectoWebApp/inicio.html")







