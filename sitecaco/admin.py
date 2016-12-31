from django.contrib import admin

from sitecaco.forms import formArquivo
from sitecaco.models import Arquivo


class AdminArquivo(admin.ModelAdmin):
    form = formArquivo
    list_display = ('nome','Arquivo', 'tipo')
    search_fields = ['Arquivo','tipo']


admin.site.register(Arquivo, AdminArquivo)
