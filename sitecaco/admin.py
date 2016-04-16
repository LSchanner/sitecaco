from django.contrib import admin
from .models import *
from django import forms
from django.contrib.sites.models import Site
from django.contrib.flatpages.forms import FlatpageForm


#Nesse arquivo são definidos as classes admins dos modelos criados em
# models.py

class AdminHtml(admin.ModelAdmin):
    class Media:
        js = [
                '//tinymce.cachefly.net/4.1/tinymce.min.js',
                '/static/js/tinymce_setup.js',
                ]

class AdminNoticia(AdminHtml):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class AdminAta(AdminHtml):
    pass

class AdminProduto(AdminHtml):
    pass


class AdminPagina(AdminHtml):
    fields = ('title','url','content','cartegoria','banner');
    form = FlatpageForm

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.sites.add(Site.objects.get_current())


class ProvaForm(forms.ModelForm):
    materia = forms.RegexField(label="Matéria", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: MC102",
            error_message="Mensagem de erro" )

    semestre = forms.RegexField(label="Semestre", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: 2014s2",
            error_message="Mensagem de erro",
            required=False
            )

    tipo = forms.RegexField(label="tipo", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: p1",
            error_message="Mensagem de erro")

    class Meta:
        model = Prova
        fields = '__all__'


class AdminProva(admin.ModelAdmin):
    form = ProvaForm
    search_fields = ['materia','tipo','semestre','professor']



admin.site.register(Livro);
admin.site.register(InscricaoFISL);
admin.site.register(Prova,AdminProva)
admin.site.register(Produto,AdminProduto)
admin.site.register(Ata,AdminAta)
admin.site.register(Arquivo);
admin.site.register(Noticia,AdminNoticia)
admin.site.register(Pagina,AdminPagina)
