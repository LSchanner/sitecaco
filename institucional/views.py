from django.shortcuts import render, get_object_or_404
from django.http import Http404

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
    if id:
        ata = get_object_or_404(Ata, id = int(id))
        return render(request, 'ata_template.html', {'ata':ata})
    else:
        raise Http404("Ata inexistente")
