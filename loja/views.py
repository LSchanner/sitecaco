from django.shortcuts import render

from loja.models import Produto

def ProdutosView(request,id):
    if(id):
        id = int(id)
        produto = Produto.objects.get(id = id)
        return render(request, 'produto.html', {'produto' : produto})

    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos' : produtos})
