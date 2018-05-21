from django.contrib import admin
from django.urls import path
from . import views
from faculdade.views import *

urlpatterns = [
   path('', index),
   path('index/', index),
   path('login/', login),
   path('contas/', contas),
   path('contasAdicionar/', contasAdicionar),
   path('contasAlterar/', contasAlterar),
   path('contasExcluir/', contasExcluir),
   path('curriculo/', curriculo),
   path('curriculoAdicionar/', curriculoAdicionar),
   path('curriculoAlterar/', curriculoAlterar),
   path('curriculoExcluir/', curriculoExcluir),
]
