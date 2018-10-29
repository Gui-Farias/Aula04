
from django.contrib import admin
from django.urls import path
from LMS.views import *

urlpatterns = [
    path('', index),
    path('contato/', contato),
    path('graduacao/', graduacao),
    path('login/', login),
    path('noticia/', noticia),
    path('ADS/', ads),
    path('WebDesigner/', WebDesigner),
    path('BancoDeDados/', BancoDeDados),

    path('graduacao/ADS/', ads),
    path('graduacao/SI/', si),
    path('graduacao/WebDesigner/', WebDesigner),
    path('graduacao/JogosDigitais/', JogosDigitais),
    path('graduacao/BancoDeDados/', BancoDeDados),
    path('graduacao/ProducaoMultimidia/', ProducaoMultimidia),

    path('login/dashboardAluno/', DashAluno),
    path('login/dashboardProf/', DashProf),



    path('admin/', admin.site.urls),
]
