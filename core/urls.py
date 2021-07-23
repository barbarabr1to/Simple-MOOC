""" 
ESSE MÓDULO DEFINE AS URL's, OU SEJA, ATRAVÉS DA DEFINIÇÃO DE UMA EXPRESSÃO REGULAR, 
A MESMA VAI INDICAR QUAL FUNÇÃO DEVE SER EXECUTADA APÓS AQUELA URL SER ACESSADA  
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Obs: as url's não funcionaram sem o '/' e aceitam nomes diferentes da def
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact')
]

