from django.contrib import admin

from membros.models import Aluno

class AdminAluno(admin.ModelAdmin):
    # form = ProvaForm
    list_display = ('nome', 'ra', 'token', 'confirmado', 'email_pessoal')
    search_fields = ['nome','ra','email_pessoal','professor']
    readonly_fields = ('token', 'ra', 'nome')


admin.site.register(Aluno, AdminAluno)
