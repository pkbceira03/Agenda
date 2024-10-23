from django.shortcuts import render, HttpResponse, redirect
from core.models import Eventos

# Create your views here.

def index(request):
    return redirect('/agenda')

def lista_eventos(request):
    evento = Eventos.objects.all()
    response = {'eventos':evento}

    return render(request, 'agenda.html', response)