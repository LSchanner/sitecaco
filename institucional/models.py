from django.db import models

from ckeditor.fields import RichTextField

import datetime

class Ata(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    content = RichTextField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.title)

    # Para automaticamente criar com o nome correto
    def save(self, *args, **kwargs):
        if not self.pk:
            self.title = "Reunião - " + str(datetime.datetime.today().strftime('%d/%m/%Y'))
        super().save(*args, **kwargs)
