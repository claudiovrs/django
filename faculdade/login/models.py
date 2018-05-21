import uuid
from django.db import models

class Usuario(models.Model):
   username = models.CharField(max_length=50)
   senha = models.CharField(max_length=140)
   
   def __str__(self):
      return self.username
      
class Sessao(models.Model):
   id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4(), editable=False)
   usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
