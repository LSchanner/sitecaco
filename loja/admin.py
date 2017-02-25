from django.contrib import admin

from loja.models import Produto
from loja.forms import formsProduto


class AdminProduto(OrderedModelAdmin):
    form = formsProduto
    list_display = ('name', 'price', 'move_up_down_links')
    search_fields = ['name', 'price']

admin.site.register(Produto,AdminProduto)
