
from django.contrib import admin
from django.urls import path
from LMS.views import *

urlpatterns = [
    #PAGINAS DAS HOMES
    path('', index),
    path('contato/', contato),
    path('graduacao/', graduacao),
    path('login/', login),
    path('noticia/', noticia),
    path('ADS/', ads),
    path('WebDesigner/', WebDesigner),
    path('BancoDeDados/', BancoDeDados),

#CURSOS
    path('graduacao/ADS/', ads),
    path('graduacao/SI/', si),
    path('graduacao/WebDesigner/', WebDesigner),
    path('graduacao/JogosDigitais/', JogosDigitais),
    path('graduacao/BancoDeDados/', BancoDeDados),
    path('graduacao/ProducaoMultimidia/', ProducaoMultimidia),

#DASHBOARDS ALUNO
    path('login/dashboardAluno/', DashAluno),
    path('login/dashboardAluno/calendario_geral/', calendario_aluno),
    path('login/dashboardAluno/atividades_entregue/', atividades_entregue_aluno),
    path('login/dashboardAluno/ouvidoria/', ouvidoria_aluno),
    path('login/dashboardAluno/financeiro/', financeiro_aluno),
    path('login/dashboardAluno/conta/', conta_aluno),


    path('login/dashboardProf/', DashProf),
    path('login/dashboardProf/calendario_prof/', calendario_prof),
    path('login/dashboardProf/planejamento_aula/', planejamento_aula),
    path('login/dashboardProf/ouvidoria_prof/', ouvidoria_prof),
    path('login/dashboardProf/corrigir_atividade_prof/', corrigir_atividade_prof),
    path('login/dashboardProf/conta_prof/', conta_prof),

    path('admin/', admin.site.urls),
]
