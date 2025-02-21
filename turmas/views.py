from django.shortcuts import render
from django.http import HttpResponse

from turmas.models import Turma

# Create your views here.


def listar(request):
     lista_turma = Turma.objects.all()
     return HttpResponse("<!DOCType html><html><body><main><p style='color:blue;'>'Lista de Turmas' </p> <img src='https://i.pinimg.com/736x/56/a1/0b/56a10b873ffd997856d404fc23a1dd04.jpg'> </main> </body></html>")

