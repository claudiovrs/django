#views.py
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db import models
#from login.models import Usuario

def autenticar(request):
   username = request.POST.get("username")
   senha = request.POST.get("senha")
   
   try:
      usuario = Usuario.objects.get(username=username)
      if senha == usuario.senha:
         return True
      else:
         return False
   except ObjectDoesNotExist:
      return True
   
         