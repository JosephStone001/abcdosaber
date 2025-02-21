from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType html><html><body><main><p style='color:blue;'>'Titulo' </p> <img src='https://th.bing.com/th/id/R.84b7c8f6236fefd984268dde706269af?rik=DkEApTxqIr0ifA&pid=ImgRaw&r=0'> <img src='https://i.pinimg.com/236x/d4/26/42/d426423f41bbbab27512ec9b2476e122.jpg'> </main> </body></html>")

def listar(request):
    return HttpResponse("<!DOCType html><html><body><main><p style='color:blue;'>'Lista de Titulo' </p> <img src='https://th.bing.com/th/id/OIP.Da1XRKx2UN13ANYYqyokdAHaHa?rs=1&pid=ImgDetMain'> </main> </body></html>")



def shoe_mensagem(request):
    x = " Blz? "
    nome = x + "Jose, Tudo bem?"
    return HttpResponse(f"Bom Dia!{nome}")

# Create your views here.
