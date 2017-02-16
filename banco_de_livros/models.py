from django.db import models

# Modelo do banco de livros
class Livro(models.Model):
    nome = models.CharField(max_length=150)
    # isbn = models.CharField(max_length=16)
    # identificador = models.CharField(max_length=15)
    autor = models.CharField(max_length=150)
    edicao = models.CharField(max_length=3)
    observacao = models.CharField(max_length=200,blank=True)
    disponivel = models.BooleanField(default=True)


    def __str__(self):
        return self.nome + ", " + self.autor + ", " + self.edicao + " edição," + "obs:" + self.observacao
