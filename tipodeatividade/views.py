from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType html><html><body><main><p style='color:blue;'>'Tipo de Atividade' </p> <img src='https://th.bing.com/th/id/R.84b7c8f6236fefd984268dde706269af?rik=DkEApTxqIr0ifA&pid=ImgRaw&r=0'> </main> </body></html>")

def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.order_by("descricao")
    resposta = "<ul>"
    for tipodeatividade in lista_tipodeatividade:
        resposta +='<li>{0}</li>'.format(tipodeatividade.descricao)
        
    resposta +='</ul>'
    print(resposta)
    
    return HttpResponse(resposta)
    #return HttpResponse("<!DOCType html><html><body><main><p style='color:red;'>'Lista de Tipos de Atividade' </p> <img src='https://th.bing.com/th/id/OIP.Da1XRKx2UN13ANYYqyokdAHaHa?rs=1&pid=ImgDetMain'> </main> </body></html>")
 


def shoe_mensagem(request):
    x = " Blz? "
    nome = x + "Jose, Tudo bem?"
    return HttpResponse(f"Bom Dia!{nome}")

def detalhe_tipodeatividade(request, ta_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    return HttpResponse (tipodeatividade)