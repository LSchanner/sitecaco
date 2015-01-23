#Funções úteis a todas as views
from .views_common import *


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


# Implementa a busca no banco de provas. Para entender leia a documentação sobre objetos Q em django
def busca_BP(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(materia__icontains=palavra) | Q(tipo__icontains=palavra) | Q(professor__icontains=palavra) | Q(semestre__icontains=palavra)
        query_final = query & query_final

    return Prova.objects.filter(query_final).all()




