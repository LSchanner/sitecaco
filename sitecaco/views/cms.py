#Funções úteis a todas as views
from .views_common import *

# Implementação de um cms básico

# TODO: estudar se vale a pena migrar para uma plataforma de cms pronta,
# tipo o mezzanine


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



