from django.contrib import admin

from loja.models import Produto
from loja.forms import formsProduto


class AdminProduto(admin.ModelAdmin):
    form = formsProduto
    list_display = ('name', 'price')
    search_fields = ['name', 'price']

admin.site.register(Produto,AdminProduto)
