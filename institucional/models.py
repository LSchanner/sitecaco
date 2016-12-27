from django.db import models

class Ata(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.title)
