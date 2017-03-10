from django.shortcuts import render
from django.core.paginator import Paginator

from haystack.query import SearchQuerySet

from noticias.models import Noticia
from paginas.models import Pagina
from institucional.models import Ata


# View usada para busca "geral"
def BuscaView(request):
    c = dict()

    try:
        termo = request.GET['q']
    except:
        return render(request, 'busca.html')

    # Indica que existe termo de busca
    c['query'] = termo

    # Busca pelo em todo o banco de dads
    results = SearchQuerySet().auto_query(termo).order_by("-time")

    # Separa os resultados
    noticias = results.models(Noticia)
    atas = results.models(Ata)
    paginas = results.models(Pagina)

    count = 0
    if noticias:
        count = count + 1
    if atas:
        count = count + 1
    if paginas:
        count = count + 1

    # verifica se há mais resultados
    if noticias.count() > 10:
        c['mais_noticias'] = True
        noticias = noticias[:10]

    if atas.count() > 10:
        c['mais_atas'] = True
        atas = atas[:10]

    if paginas.count() > 10:
        c['mais_paginas'] = True
        paginas = paginas[:10]

    c['noticias'] =  noticias
    c['atas'] =  atas
    c['paginas'] =  paginas
    c['morethan2'] = True if count > 1 else False

    return render(request, 'busca.html', c)


#View usada para busca em Cartegorias específicas
def BuscaCartegoriaView(request,tipo,pag):
    c = dict()

    # Determina em que modelo procurar
    if tipo=="ata":
        template = 'busca_ata.html'
        modelo = Ata

    if tipo=="pagina":
        template = 'busca_pagina.html'
        modelo = Pagina

    if tipo=="noticia":
        template = 'busca_noticia.html'
        modelo = Noticia

    # Página a ser exibida
    if pag:
        pag = int(pag)
    else:
        pag = 1

    # O termo a ser procurado
    try:
        termo = request.GET['q']
    except:
        return render(request, template)


    # indica que existe termo de busca
    c['query'] = termo

    # Busca pelo termo
    resultados = SearchQuerySet().auto_query(termo).order_by("-time")
    resultados = resultados.models(modelo)

    pagina = Paginator(resultados,10).page(pag)
    c['page'] = pagina

    return render(request, template, c)
