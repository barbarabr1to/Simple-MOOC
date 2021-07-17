"""
NESSE MÓDULO FICAM AS FUNÇÕES QUE SERÃO EXECUTADAS DE ACORDO COM CADA URL
"""

from django.shortcuts import render
# A classe HttpResponse deve ser retornada nas views, ela é a reposta da requisição
from django.http import HttpResponse

# A função recebe obrigatoriamente o request que é a requisição atual
def home(request):
    return HttpResponse('Hello, world!')
