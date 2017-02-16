from django.contrib import admin

from loja.models import Produto

class AdminHtml(admin.ModelAdmin):
    class Media:
        js = [
                '//tinymce.cachefly.net/4.1/tinymce.min.js',
                '/static/js/tinymce_setup.js',
                ]
class AdminProduto(AdminHtml):
    pass

admin.site.register(Produto,AdminProduto)
