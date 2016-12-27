from django.contrib import admin
from noticias.models import Noticia


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

admin.site.register(Noticia,AdminNoticia)
