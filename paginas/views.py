# Implementação de um cms básico

# TODO: estudar se vale a pena migrar para uma plataforma de cms pronta,
# tipo o mezzanine

from django.shortcuts import render, redirect
from paginas.models import Pagina


# HomePage
def HomeView(request):
    return redirect('./noticias/')


# Eventos
def EventosView(request):
    pages = Pagina.objects.filter(cartegoria = 'Eventos')
    return render(request, 'eventos.html', {'pages' : pages})


# Servicoes
def ServicosView(request):
    pages = Pagina.objects.filter(cartegoria = 'Serviços')
    return render(request, 'servicos.html', {'pages' : pages})
