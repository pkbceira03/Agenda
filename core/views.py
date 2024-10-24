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

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Eventos.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data')
        usuario = request.user
        id_evento = request.POST.get('id_evento')

        if id_evento:
            evento = Eventos.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            # Eventos.objects.filter(id=id_evento).update(titulo=titulo, descricao=descricao, data_evento=data, usuario=usuario)
        else:
            Eventos.objects.create(titulo=titulo, descricao=descricao, data_evento=data, usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Eventos.objects.get(id=id_evento)

    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')
