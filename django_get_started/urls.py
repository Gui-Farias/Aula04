'''
from django.contrib import admin
from django.urls import path
from app.views import *

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
'''

"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Pagina Principal:
    url(r'^$', 'app.views.index', name='home'),
    url(r'^contato', 'app.views.contato', name='contato'),
    url(r'^graduacao', 'app.views.graduacao', name='graduacao'),  
    url(r'^noticia', 'app.views.noticia', name='noticia'),
    url(r'^login', 'app.views.login', name='login'),

    # CURSOS
    url(r'^ADS', 'app.views.ads', name='ADS'),
    url(r'^SI', 'app.views.si', name='SI'),
    url(r'^WebDesigner', 'app.views.WebDesigner', name='WebDesigner'),
    url(r'^JogosDigitais', 'app.views.JogosDigitais', name='JogosDigitais'),
    url(r'^BancoDeDados', 'app.views.BancoDeDados', name='BancoDeDados'),
    url(r'^ProducaoMultimidia', 'app.views.ProducaoMultimidia', name='ProducaoMultimidia'),

    # Dash ALuno
    url(r'^dashboardAluno', 'app.views.DashAluno', name='dashAluno'),
    url(r'^calendario_geral', 'app.views.calendario_aluno', name='calendario_aluno'),
    url(r'^atividades_entregue', 'app.views.atividades_entregue_aluno', name='atividades_entregue_aluno'),
    url(r'^ouvidoria_aluno', 'app.views.ouvidoria_aluno', name='ouvidoria_aluno'),
    url(r'^financeiro', 'app.views.financeiro_aluno', name='financeiro_aluno'),
    url(r'^conta_aluno', 'app.views.conta_aluno', name='conta_aluno'),

    # Dash Professor
    url(r'^dashboardProf', 'app.views.DashProf', name='DashProf'),
    url(r'^calendario_prof', 'app.views.calendario_prof', name='calendario_prof'),
    url(r'^planejamento_aula', 'app.views.planejamento_aula', name='planejamento_aula'),
    url(r'^ouvidoria_prof', 'app.views.ouvidoria_prof', name='ouvidoria_prof'),
    url(r'^corrigir_atividade_prof', 'app.views.corrigir_atividade_prof', name='corrigir_atividade_prof'),
    url(r'^conta_prof', 'app.views.conta_prof', name='conta_prof'),
   
   # Dash Coordenador
   url(r'^dashboard_coordenador', 'app.views.dashboard_coordenador', name='dashboard_coordenador'),
   url(r'^cadastrar_prof', 'app.views.cadastrar_prof', name='cadastrar_prof'),
   url(r'^cadastrar_aluno', 'app.views.cadastrar_aluno', name='cadastrar_aluno'),
   url(r'^Conta_Coordenador', 'app.views.Conta_Coordenador', name='Conta_Coordenador'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
