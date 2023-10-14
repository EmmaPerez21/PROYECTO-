from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Estudiantes

# Create your views here.

class VRegistro(View):

    def get(self, request):
        form=CustomUserCreationForm()
        return render(request,"registrarse/registrarse.html",{"form":form})

    def post(self, request):
        form=CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():

            usuario=form.save()
            ncui = form.cleaned_data.get('cui')
            # nimagen = form.cleaned_data.get('profile_imagen')
            img = form.cleaned_data.get("profile_imagen")
            # print(cui)
            # username=request.user.username
            # password=request.user.password1
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            usuario = authenticate(request=request, username=username, password=password)
            login(request, usuario)
            nuevo_usuario = Estudiantes(user=request.user, username=request.user.username, fisrt_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email, cui=ncui, profile_image = img)
            nuevo_usuario.save()
            return redirect("Estudiante")
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

                
            return render(request,"registrarse/registrarse.html",{"form":form})

def cerrar_session(request):
    logout(request)

    return redirect("Estudiante")

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("Estudiante")
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

