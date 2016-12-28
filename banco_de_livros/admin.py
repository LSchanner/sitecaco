from django.contrib import admin

from banco_de_livros.models import Livro


class AdminLivro(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'edicao', 'disponivel')
    search_fields = ['nome', 'autor', 'edicao', 'observacao']

admin.site.register(Livro, AdminLivro)
