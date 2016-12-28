from django.shortcuts import render, get_object_or_404
from django.http import Http404

from noticias.models import Noticia

def NoticiasView(request,pag=1):
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    posts = Noticia.objects.all()[(pag-1)*10  : pag * 10]
    return render(request, 'noticias.html', {'posts': posts, 'pag': pag})

def NoticiaView(request,id):
    if id:
        post = get_object_or_404(Noticia, id = int(id))
        return render(request, 'noticia.html', {'post': post})
    raise Http404("Noticia inexistente")
