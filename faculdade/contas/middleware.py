from login.models import Sessao
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django import http
from django.http import HttpResponse 

class SessaoMiddleware(object): 
   #Construtor necessário para a classe 
   def __init__(self, get_response): 
      self.get_response = get_response 
   
   #Chamada do filtro 
   def __call__(self, request): 

      # vamos pular arquivos estáticos 
      if not request.path_info.startswith("/static/"): 
         if self.sessionId in request.COOKIES:
            cookie = request.COOKIES[self.sessionId]
            sessao = Sessao.objects.get(id=cookie)
            request.sessao = sessao
      response = self.get_response(request)
      
      if hasattr(request,"sessao"):
      #testa se há sessao
         response.set_cookie(self._sessionId, request.sessao.Id)
      else:
         response.delete_cookie(self.sessionId)   
      
      return response
      
   #função de excluir sessão
   def sair(request):
      request.sessao.delete()
     
class AutorizacaoMiddleware(object):
   
   def __init__(self, get_response):
      self.get_response = get_response
   
   def __call__(self, request):
      path = request.path_info
      if path.startswith("/contas/") and not hasattr(request, "sessao"):
         return redirect("/login/")
      else:
         return self.get_response(request)