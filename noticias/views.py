from django.shortcuts import render
from noticias.models import Noticia

def NoticiasView(request,pag=1):
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    posts = Noticia.objects.all()[(pag-1)*10  : pag * 10]
    return render(request, 'noticias.html', {'posts': posts , 'pag': pag})

def NoticiaView(request,id):
    post = Noticia.objects.get(id = id)

    return render(request, 'noticia.html', {'post':post})
