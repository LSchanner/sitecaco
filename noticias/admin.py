from django.contrib import admin
from noticias.models import Noticia

class AdminNoticia(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Noticia,AdminNoticia)
