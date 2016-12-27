from django.contrib import admin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.sites.models import Site

from paginas.models import Pagina

class AdminHtml(admin.ModelAdmin):
    class Media:
        js = [
                '//tinymce.cachefly.net/4.1/tinymce.min.js',
                '/static/js/tinymce_setup.js',
                ]

class AdminPagina(AdminHtml):
    fields = ('title','url','content','cartegoria','banner');
    form = FlatpageForm

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.sites.add(Site.objects.get_current())

admin.site.register(Pagina,AdminPagina)
