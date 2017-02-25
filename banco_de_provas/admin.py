from django.contrib import admin

from banco_de_provas.models import Prova
from banco_de_provas.forms import ProvaForm


class AdminProva(admin.ModelAdmin):
    form = ProvaForm
    fields = ( 'aprovado', 'materia', 'semestre', 'professor', 'tipo', 'file')
    list_display = ('materia', 'tipo', 'semestre', 'professor', 'aprovado')
    search_fields = ['materia','tipo','semestre','professor']


admin.site.register(Prova, AdminProva)
