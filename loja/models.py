from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    imagem = models.ImageField()

    def __str__(self):
        return self.name
