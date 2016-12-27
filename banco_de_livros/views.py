from django.shortcuts import render


def LivroView(request):
    busca = request.GET.get('search')

    resultados = ""
    if(busca):
        resultados = busca_livros(busca)

    return render(request, 'banco_livros.html', {'resultados':resultados})

#Busca implementada apenas para nome da obra e do autor
def busca_livros(busca):
    query_final = Q()
    palavras = busca.split()
    for palavra in palavras:
        query = Q(nome__icontains=palavra) | Q(autor__icontains=palavra)
        query_final = query & query_final


    return Livro.objects.filter(query_final).all()
