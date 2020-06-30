from django.shortcuts import render
from random import randint

# Create your views here.
def listar_tarefas(request):
    nome = 'Assistir a Semana Python/Django da TreinaWeb'




    return render(request, 'tarefas/listar_tarefas.html', {
        "nome": nome,
        "tarefa_2": "Programar em Python",
        })
