# TODO: estudar se vale a pena migrar para uma plataforma de cms pronta,
# tipo o mezzanine
from django.shortcuts import render, redirect

from paginas.models import Pagina
from noticias.models import Noticia
from sitecaco.models import Arquivo


# HomePage
# Por default, deixei as ultimas 6 noticias na HomePage
def HomeView(request):
    posts = Noticia.objects.all()[0:6]

    # Para gerar banners dinâmicos
    banners = Arquivo.objects.filter(tipo='BannerAtivo')
    if banners:
        return render(request, 'home.html', {'posts': posts, 'banners': banners})
    return render(request, 'home.html', {'posts': posts})

# Eventos
def EventosView(request):
    pages = Pagina.objects.filter(cartegoria = 'Eventos')
    return render(request, 'eventos.html', {'pages' : pages})


# Servicoes
def ServicosView(request):
    pages = Pagina.objects.filter(cartegoria = 'Serviços')
    return render(request, 'servicos.html', {'pages' : pages})
