from .models import *
from haystack.query import SearchQuerySet
from django.template import loader, RequestContext, Context as Con
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from sitecaco.settings import URL_BASE
from django.core.paginator import Paginator


# Wrapper sobre a função do django "Context", para incluir sempre a URL base
def Context(dicionario):
    dicionario['URL_BASE'] = URL_BASE
    return Con(dicionario)

def HomeView(request):
    return redirect('./noticias')

def NoticiasView(request,pag=1):
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    posts = Noticia.objects.all()[(pag-1)*10  : pag * 10]
    t = loader.get_template('noticias.html')
    c = Context({ 'posts': posts , 'pag':pag})
    return HttpResponse(t.render(c))

def NoticiaView(request,id):
    post = Noticia.objects.get(id = id)

    # Formulário de comentários
    if request.method == 'POST':
        form = formComentario(request.POST)
        if form.is_valid():
            comment = Comentario(author=form.cleaned_data['author'],
                    content=form.cleaned_data['content'], noticia=post)
            comment.save()

    comments = Comentario.objects.filter(noticia=post)
    form = formComentario()

    t = loader.get_template('noticia.html')
    c = RequestContext(request,{'post':post,'form':form,'comments':comments})
    return HttpResponse(t.render(c))


def InstitucionalView(request):
    t = loader.get_template('institucional.html')
    pages = Pagina.objects.filter(cartegoria = 'Institucional')
    c = Context({'pages' : pages})
    return HttpResponse(t.render(c))

def EventosView(request):
    t = loader.get_template('eventos.html')
    pages = Pagina.objects.filter(cartegoria = 'Eventos')
    c = Context({'pages' : pages})
    return HttpResponse(t.render(c))


def ServicosView(request):
    t = loader.get_template('servicos.html')
    pages = Pagina.objects.filter(cartegoria = 'Serviços')
    c = Context({'pages' : pages})
    return HttpResponse(t.render(c))

def AtasView(request,pag):
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    atas = Ata.objects.all()[(pag-1)*30  : pag * 30] #paginação das atas
    t = loader.get_template('atas.html')
    c = Context({ 'atas': atas , 'pag':pag})
    return HttpResponse(t.render(c))

def AtaView(request,id):
    ata = Ata.objects.get(id = id)
    t = loader.get_template('ata_template.html')
    c = Context({'ata':ata})
    return HttpResponse(t.render(c))

def ProdutosView(request,id):
    if(id):
        id = int(id)
        t = loader.get_template('produto.html')
        produto = Produto.objects.get(id = id)
        c = Context({'produto' : produto})
        return HttpResponse(t.render(c))

    t = loader.get_template('produtos.html')
    produtos = Produto.objects.all()
    c = Context({'produtos' : produtos})
    return HttpResponse(t.render(c))



def BancoView(request):
    t = loader.get_template('banco_provas.html')
    c = Context({})

    busca = request.GET.get('search')

    #Faz busca
    if(busca):
        resultados = busca_BP(busca)
        c = Context({'resultados':resultados})

    return HttpResponse(t.render(c))


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


# faz a busca no banco de provas. Para entender leia a documentação sobre objetos Q em django
def busca_BP(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(materia__icontains=palavra) | Q(tipo__icontains=palavra) | Q(professor__icontains=palavra) | Q(semestre__icontains=palavra)
        query_final = query & query_final

    return Prova.objects.filter(query_final).all()



