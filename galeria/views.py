from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Create your views here.
def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if 'categoria' in request.GET:
        fotografias = fotografias.filter(categoria=request.GET['categoria'])
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if "nome" in request.GET:
        nome_buscar = request.GET['nome']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})
