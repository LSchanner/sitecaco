from django.shortcuts import render, get_object_or_404

from loja.models import Produto

def ProdutosView(request,id):
    if(id):
        produto = get_object_or_404(Produto, id = int(id))
        return render(request, 'produto.html', {'produto' : produto})

    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos' : produtos})
