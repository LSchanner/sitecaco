from django.db import models
from django.contrib.flatpages.models import FlatPage

class Pagina(FlatPage):
    CARTEGORIAS = (
        ('Serviços','Serviços'),
        ('Institucional','Institucional'),
        ('Eventos','Eventos'),
        ('Livre','Livre'),
    )

    cartegoria = models.CharField(max_length=15,choices=CARTEGORIAS);
    banner = models.ImageField(blank=True)

    def __str__(self):
        return self.title
