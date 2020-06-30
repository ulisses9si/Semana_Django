from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar-tarefas/', listar_tarefas, name="listar_tarefas"),
]


