#views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from curriculo.models import Curriculo
from contas.models import Contas
from django.http import Http404

def index(request):
   return render(request, "page/index.html")
   
def login(request):
   if request.method == "GET":
      print("Acessado via GET")
      return render(request, "page/login.html")
   else:
      if request.POST.get("senha") == "admin":
         print("Acessado via POST com sucesso!")
         print("Username: ", request.POST.get("username"), " | Senha: ", request.POST.get("senha"))
         return render(request, "page/index.html")
      else:
         print("Acessado via POST com insucesso!")
         print("Username: ", request.POST.get("username"), " | Senha: Incorreta")
         return render(request, "page/login.html")
         
def contas(request):
   contas = Contas.objects.all()
   context = {'listarContas':contas}
   return render(request, "page/contas.html", context)
   
def contasAdicionar(request):
   if request.method == "GET":
      print("Acessado via GET")
      return render(request, "page/contaAdicionar.html")
   else:
      conta=Contas.objects.create(nome=request.POST.get("nome"),ra=request.POST.get("ra"),senha=request.POST.get("senha"),telefone=request.POST.get("telefone"))
      conta.save()
      return redirect("/contas/")
      
def contasAlterar(request):
   parametro=request.GET['id']
   conta = Contas.objects.get(id=parametro)
   
   if request.method == "GET":
      print("Acessado via GET")
      print(conta)
      return render(request, "page/contasAlterar.html", {'conta': conta})
      return redirect("/contas/")
   else:
      conta.nome=request.POST.get("nome")
      conta.ra=request.POST.get("ra")
      conta.senha=request.POST.get("senha")
      conta.telefone=request.POST.get("telefone")
      conta.save()
      
      return redirect("/contas/")
      
def contasExcluir(request):
   parametro=request.GET['id']
   conta = Contas.objects.get(id=parametro)
   
   if request.method == "GET":
      print("Acessado via GET")
      return render(request, "page/contasExcluir.html", {'conta': conta})
      return redirect("/contas/")
   else:
      Contas.objects.get(id=parametro).delete()
      return redirect("/contas/")

def curriculo(request):
   curriculos = Curriculo.objects.all()
   context = {'listarCurriculo':curriculos}
   return render(request, "page/curriculo.html", context)
   
def curriculoAdicionar(request):
   if request.method == "GET":
      print("Acessado via GET")
      return render(request, "page/curriculoAdicionar.html")
   else:
      curriculo=Curriculo.objects.create(nome=request.POST.get("nome"),qtdHora=request.POST.get("qtdHora"),matricula=request.POST.get("matricula"))
      curriculo.save()
      return redirect("/curriculo/")

def curriculoAlterar(request):
   parametro=request.GET['id']
   curriculo = Curriculo.objects.get(id=parametro)
   
   if request.method == "GET":
      print("Acessado via GET")
      print(curriculo)
      return render(request, "page/curriculoAlterar.html", {'curriculo': curriculo})
      return redirect("/curriculo/")
   else:
      curriculo.nome=request.POST.get("nome")
      curriculo.qtdHora=request.POST.get("qtdHora")
      curriculo.matricula=request.POST.get("matricula")
      curriculo.save()
      
      return redirect("/curriculo/")

def curriculoExcluir(request):
   parametro=request.GET['id']
   curriculo = Curriculo.objects.get(id=parametro)
   
   if request.method == "GET":
      print("Acessado via GET")
      return render(request, "page/curriculoExcluir.html", {'curriculo': curriculo})
      return redirect("/curriculo/")
   else:
      Curriculo.objects.get(id=parametro).delete()
      return redirect("/curriculo/")
