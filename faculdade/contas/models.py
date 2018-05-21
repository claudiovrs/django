from django.db import models
from django import forms

class Contas(models.Model):
   nome = models.CharField("Nome", max_length=100)
   ra = models.CharField("RA", max_length=10)
   senha = models.CharField("Senha", max_length=50)
   telefone = models.CharField("Telefone", max_length=50)
   
   def __str__(self):
      return str(self.nome)