from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listar(request):
    return HttpResponse("<!DOCType html><html><body><main><p style='color:blue;'>'Lista dos Instrutores' </p> <img src='https://i.redd.it/gc2m1tdq22w81.jpg'> </main> </body></html>")

