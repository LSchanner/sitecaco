#Funções úteis a todas as views
from .views_common import *


# View usada para busca "geral"
def BuscaView(request):
    t = loader.get_template('busca.html')
    c = Context({})

    try:
        termo = request.GET['q']
    except:
        return HttpResponse(t.render(c))

    # indica que existe termo de busca
    c['query'] = termo

    # Busca pelo termo
    results = SearchQuerySet().auto_query(termo).order_by("-time")

    # Separa os resultados
    noticias = results.models(Noticia)
    atas = results.models(Ata)
    paginas = results.models(Pagina)

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


    return HttpResponse(t.render(c))


#View usada para busca em Cartegorias específicas
def BuscaCartegoriaView(request,tipo,pag):
    c = Context({})

    # determina em que modelo procurar
    if tipo=="ata":
        t = loader.get_template('busca_ata.html')
        modelo = Ata

    if tipo=="pagina":
        t = loader.get_template('busca_pagina.html')
        modelo = Pagina

    if tipo=="noticia":
        t = loader.get_template('busca_noticia.html')
        modelo = Noticia

    # Página a ser exibida
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    # O termo a ser procurado
    try:
        termo = request.GET['q']
    except:
        return HttpResponse(t.render(c))


    # indica que existe termo de busca
    c['query'] = termo

    # Busca pelo termo
    resultados = SearchQuerySet().auto_query(termo).order_by("-time")
    resultados = resultados.models(modelo)

    pagina = Paginator(resultados,10).page(pag)
    c['page'] = pagina

    return HttpResponse(t.render(c))


