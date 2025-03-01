from django.shortcuts import render
from django.http import HttpResponse
from django.forms import forms
from instrutores.models import Instrutores
from titulo.models import Titulo
from instrutores.forms import InstrutoresForm



# Create your views here.

def listar(request):
    lista_instrutores = Instrutores.objects.all()
    contexto = {
        'instrutores': lista_instrutores

    }
    return render(request, 'instrutores/listarinstrutores.html', context=contexto)

def carregar_cadastro(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'instrutores/cadastrarInstrutores.html', context=contexto)

def cadastrar(request):
    form = InstrutoresForm(request.POST)
    if form.is_valid():
        dados_intrutores = form.cleaned_data
        titulo = Titulo.objects.get(pk=dados_intrutores["codigo_titulo"])
        
        instrutores = Instrutores(
            id = dados_intrutores["id"],
            rg = dados_intrutores["rg"],
            nome = dados_intrutores["nome"],
            data_nascimento = dados_intrutores["data_nascimento"],
            telefone = dados_intrutores["telefone"],
            ddd = dados_intrutores["ddd"],
            codigo_titulo = titulo, 
            
            
            descricao = dados_intrutores['descricao'],
        )
        instrutores.save()
        
    return render(request, 'instrutores/cadastrarInstrutores.html')
