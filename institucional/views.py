from django.shortcuts import render

from institucional.models import Ata
from paginas.models import Pagina


def InstitucionalView(request):
    pages = Pagina.objects.filter(cartegoria = 'Institucional')
    return render(request, 'institucional.html', {'pages' : pages})


def AtasView(request,pag):
    if pag != '':
        pag = int(pag)
    else :
        pag = 1

    atas = Ata.objects.all()[(pag-1)*30  : pag * 30] #paginação das atas

    return render(request, 'atas.html', {'atas': atas , 'pag':pag})


def AtaView(request,id):
    ata = Ata.objects.get(id = id)

    return render(request, 'atas.html', {'ata':ata})
