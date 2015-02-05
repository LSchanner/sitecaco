#Funções úteis a todas as views
from .views_common import *


from django.core.mail import send_mail

# Views relativas ao banco de provas
def BancoView(request):
    t = loader.get_template('banco_provas.html')
    c = Context({})

    busca = request.GET.get('search')

    #Faz busca
    if(busca):
        resultados = busca_BP(busca)
        c = Context({'resultados':resultados})

    return HttpResponse(t.render(c))

def enviar(request):
    c = RequestContext(request,{})

    if request.method == 'GET':
        t = loader.get_template('form_bp.html')
        return HttpResponse(t.render(c))


    # dados da submissão
    sub = [request.POST['materia'], request.POST['tipo'],
            request.POST['semestre'], request.POST['professor']]


    # a submissão não possui todos os dados obrigatórios
    if not (sub[0] and sub[1] and request.POST['prova']):
        t = loader.get_template('form_bp.html')
        c['erro'] = True
        return HttpResponse(t.render(c))

    # deixa tudo em minúsculas
    sub = [s.lower() for s in sub]

    # esse formato deixa os nomes dos arquivos mais machine-readable
    sub = [s.replace(' ','_').replace('-','_') for s in sub]


    # salva a prova
    prova = Prova(materia = sub[0], tipo = sub[1], semestre = sub[2],
            professor = sub[3], file = request.POST['prova'],
            aprovado = False)

    prova.save()

    mensagem = """

        Uma prova nova foi inserida no banco de provas. visite a página
        http://www.caco.ic.unicamp.br/portal/admin/sitecaco/prova/%s/
        e revise as informações antes de aprovar.

        """ % prova.id


    send_mail("Banco de Provas: submissão " + str(prova.id), mensagem ,
            "caco@ic.unicamp.br", ['caco@ic.unicamp.br'])

    c['mensagem'] = """ Obrigado por contribuir com o banco de provas """

    t = loader.get_template('obrigado.html')
    return HttpResponse(t.render(c))



# Implementa a busca no banco de provas. Para entender leia a documentação sobre objetos Q em django
def busca_BP(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(materia__icontains=palavra) | Q(tipo__icontains=palavra) | Q(professor__icontains=palavra) | Q(semestre__icontains=palavra)
        query_final = query & query_final


    return Prova.objects.filter(query_final).filter(aprovado=True).all()




