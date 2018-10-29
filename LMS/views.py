from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contato(request):
    return render(request,'contato.html')

def graduacao(request):
    return render(request,'graduacao.html')

def noticia(request):
    return render(request,'noticia.html')

def ads(request):
    return render(request,'CursosEspecificados/ADS.html')

def si(request):
    return render(request,'CursosEspecificados/SI.html')

def WebDesigner(request):
    return render(request,'CursosEspecificados/WebDesigner.html')

def JogosDigitais(request):
    return render(request,'CursosEspecificados/JogosDigitais.html')

def BancoDeDados(request):
    return render(request,'CursosEspecificados/BancoDeDados.html')

def ProducaoMultimidia(request):
    return render(request,'CursosEspecificados/ProducaoMultimidia.html')

def DashAluno(request):
    return render(request,'DashBoard/dashboardAluno.html')

def DashProf(request):
    return render(request,'DashBoard/dashboardProf.html')




    