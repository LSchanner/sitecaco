from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.core.mail import send_mail

from banco_de_provas.models import Prova

# Views relativas ao banco de provas
def BancoView(request):
    busca = request.GET.get('search')

    #Faz busca
    resultados = ""
    if(busca):
        resultados = busca_BP(busca)

    return render(request, 'banco_provas.html', {'resultados':resultados})




@csrf_protect
def enviar(request):
    if request.method == 'GET':
        return render(request, 'form_bp.html')


    # dados da submissão
    sub = [request.POST['materia'], request.POST['tipo'],
            request.POST['semestre'], request.POST['professor']]


    # a submissão não possui todos os dados obrigatórios
    if not (sub[0] and sub[1] and request.FILES['prova']):
        return render(request, 'form_bp.html', {'erro': True})

    # deixa tudo em minúsculas
    sub = [s.lower() for s in sub]

    # esse formato deixa os nomes dos arquivos mais machine-readable
    sub = [s.replace(' ','_').replace('-','_') for s in sub]


    # salva a prova
    prova = Prova(materia = sub[0], tipo = sub[1], semestre = sub[2],
            professor = sub[3], file = request.FILES['prova'],
            aprovado = False)

    prova.save()

    mensagem = """

        Uma prova nova foi inserida no banco de provas. visite a página
        http://www.caco.ic.unicamp.br/portal/admin/sitecaco/prova/%s/
        e revise as informações antes de aprovar.

        """ % prova.id


    send_mail("Banco de Provas: submissão " + str(prova.id), mensagem ,
            "caco@ic.unicamp.br", ['caco@ic.unicamp.br'])

    ##return render(request, 'form_bp.html')
    return render(request, 'obrigado.html', {'mensagem': """ Obrigado por contribuir com o banco de provas """})


# Implementa a busca no banco de provas. Para entender leia a documentação sobre objetos Q em django
def busca_BP(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(materia__icontains=palavra) | Q(tipo__icontains=palavra) | Q(professor__icontains=palavra) | Q(semestre__icontains=palavra)
        query_final = query & query_final


    return Prova.objects.filter(query_final).filter(aprovado=True).all()
