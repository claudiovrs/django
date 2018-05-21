from django.db import models
from django import forms

class Curriculo(models.Model):
   nome = models.CharField("Nome", max_length=100)
   qtdHora = models.IntegerField("QTD Hora")
   matricula = models.CharField("Matricula", max_length=50)
   
   def __str__(self):
      return self.nome