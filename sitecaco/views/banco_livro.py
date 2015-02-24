#Aproveitado código banco_provas, sem implementação de envio#

from .views_common import *

def LivroView(request):
    t = loader.get_template('banco_livros.html')
    c = Context({})

    busca = request.GET.get('search')

    #Faz busca
    if(busca):
        resultados = busca_livros(busca)
        c = Context({'resultados':resultados})

    return HttpResponse(t.render(c))

#Busca implementada apenas para nome da obra e do autor
def busca_livros(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(nome__icontains=palavra) | Q(autor__icontains=palavra)
        query_final = query & query_final


    return Livro.objects.filter(query_final).all()
