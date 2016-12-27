from django.contrib import admin

from institucional.models import Ata

class AdminHtml(admin.ModelAdmin):
    class Media:
        js = [
                '//tinymce.cachefly.net/4.1/tinymce.min.js',
                '/static/js/tinymce_setup.js',
                ]
class AdminAta(AdminHtml):
    pass
#         model = Prova

admin.site.register(Ata,AdminAta)
