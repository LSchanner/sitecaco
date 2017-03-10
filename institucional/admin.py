from django.contrib import admin

from institucional.models import Ata
from institucional.forms import formsAta

class AdminAta(admin.ModelAdmin):
    form = formsAta
    search_fields = ('title', 'time')

admin.site.register(Ata ,AdminAta)
