from django.shortcuts import render, HttpResponse, redirect
from core.models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Eventos.objects.filter(usuario=usuario)
    response = {'eventos':evento}

    return render(request, 'agenda.html', response)

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect ('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(username=username, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    
    return redirect('/')
