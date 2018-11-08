from django.shortcuts import render
from django.http import HttpResponse

############## PAGINAS DAS HOMES ##############

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


############## CURSOS ##############

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

############## AREA ALUNO ##############

def DashAluno(request):
    return render(request,'DashBoard/area_aluno/dashboardAluno.html')

def calendario_aluno(request):
    return render(request,'DashBoard/area_aluno/calendario_geral.html')

def atividades_entregue_aluno(request):
    return render(request,'DashBoard/area_aluno/atividades_entregue.html')

def ouvidoria_aluno(request):
    return render(request,'DashBoard/area_aluno/ouvidoria.html')

def financeiro_aluno(request):
    return render(request,'DashBoard/area_aluno/financeiro.html')

def conta_aluno(request):
    return render(request,'DashBoard/area_aluno/conta.html')

############## AREA PROFESSOR ##############

def DashProf(request):
    return render(request,'DashBoard/area_professor/dashboardProf.html')

def calendario_prof(request):
    return render(request,'DashBoard/area_professor/calendario_prof.html')

def planejamento_aula(request):
    return render(request,'DashBoard/area_professor/planejamento_aula.html')

def ouvidoria_prof(request):
    return render(request,'DashBoard/area_professor/ouvidoria_prof.html')

def corrigir_atividade_prof(request):
    return render(request,'DashBoard/area_professor/corrigir_atividade_prof.html')

def conta_prof(request):
    return render(request,'DashBoard/area_professor/conta_prof.html')

############## AREA Coordenador ##############

def dashboard_coordenador(request):
    return render(request,'DashBoard/area_coordenador/dashboard_coordenador.html')

def cadastrar_prof(request):
    return render(request,'DashBoard/area_coordenador/cadastrar_prof.html')

def cadastrar_aluno(request):
    return render(request,'DashBoard/area_coordenador/cadastrar_aluno.html')

def Conta_Coordenador(request):
    return render(request,'DashBoard/area_coordenador/Conta_Coordenador.html')
