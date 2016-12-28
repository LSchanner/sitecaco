from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.sites.models import Site
from django import forms

from ckeditor.widgets import CKEditorWidget

from paginas.models import Pagina


# Extende a classe FlatpageForm e adiciona o CKEdito widget no campo content
# para que assim o editor de texto das páginas seja WYSIWYG
# https://github.com/django-ckeditor/django-ckeditor#widget
class FlatpageFormPagina(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


# Classe para gerar a interface admin das páginas
# Nelas teremos os fields selecionados e seguira o modelo
class FlatPageAdminPagina(admin.ModelAdmin):
    list_display = ('title', 'url', 'cartegoria')
    fields = ('title','url','content','cartegoria','banner');
    form = FlatpageFormPagina

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.sites.add(Site.objects.get_current())

# Faz o registro na interface admin do modelo Pagina
admin.site.register(Pagina, FlatPageAdminPagina)

# Não aparecerá na interface de admin essas duas opções
admin.site.unregister(FlatPage)
admin.site.unregister(Site)
