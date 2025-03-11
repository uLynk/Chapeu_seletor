from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Pergunta, Resposta, Casa, Partida, Time
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioCreationForm


def home(request):
    return render(request, 'core/home.html')


def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = UsuarioCreationForm()
    return render(request, 'core/cadastro.html', {'form': form})

@login_required
def chapeu_seletor(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'chapeu_seletor.html', {'perguntas': perguntas})

@login_required
def chapeu_seletor(request):
    perguntas = Pergunta.objects.prefetch_related('respostas').all() 
    return render(request, 'chapeu_seletor.html', {'perguntas': perguntas})

@login_required
def processar_chapeu(request):
    if request.method == 'POST':
        respostas = request.POST
        pontos = {}

        for key, value in respostas.items():
            if key.startswith('resposta_'):
                resposta = Resposta.objects.get(id=value)
                casa = resposta.casa
                pontos[casa] = pontos.get(casa, 0) + 1

        casa_selecionada = max(pontos, key=pontos.get)
        
        request.user.casa = casa_selecionada
        request.user.save()

        return redirect('minha_casa')

    return redirect('chapeu_seletor')

@login_required
def minha_casa(request):
    casa = request.user.casa
    return render(request, 'minha_casa.html', {'casa': casa})


def beco_diagonal(request):
    return render(request, 'core/beco_diagonal.html')


def quadribol(request):
    partidas = Partida.objects.all().order_by('data')
    times = Time.objects.all().order_by('-pontos')  

    if request.method == 'POST':
        partida_id = request.POST.get('partida_id')
        placar_time1 = request.POST.get('placar_time1')
        placar_time2 = request.POST.get('placar_time2')

        if placar_time1 is not None and placar_time1 != '':
            placar_time1 = int(placar_time1)
        else:
            placar_time1 = 0 

        if placar_time2 is not None and placar_time2 != '':
            placar_time2 = int(placar_time2)
        else:
            placar_time2 = 0 

        partida = Partida.objects.get(id=partida_id)

        partida.pontos_time1 = placar_time1
        partida.pontos_time2 = placar_time2
        partida.save()

        time1 = partida.time1
        time2 = partida.time2

        time1.pontos += placar_time1
        time2.pontos += placar_time2

        time1.save()
        time2.save()

        return redirect('quadribol')  

    return render(request, 'quadribol.html', {'partidas': partidas, 'times': times})


def casa(request):
    return render(request, 'core/casa.html')


def logout_view(request):
    logout(request)
    return redirect('home')