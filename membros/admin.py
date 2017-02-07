# This admin interface is using django-import-export module
# https://django-import-export.readthedocs.io
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from membros.models import Aluno

## Class to allow importing and exporting via admin interface
class ResourceAluno(resources.ModelResource):

    class Meta:
        model = Aluno
        import_id_fields = ['ra']


class AdminAluno(ImportExportModelAdmin):
    resource_class = ResourceAluno
    list_display = ('nome', 'ra', 'token', 'membro_confirmado','email_pessoal')
    search_fields = ['nome','ra','email_pessoal','ano_ingresso', 'vinculo']
    readonly_fields = ('token', 'ra', 'nome')
    ordering=['ra']

admin.site.register(Aluno, AdminAluno)
