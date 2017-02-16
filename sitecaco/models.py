from django.db import models


# O intuito desse modelo é apenas deixar que os administradores façam upload
# de coisas arbitrárias para o site.
class Arquivo(models.Model):
    tipo_arquivo = (
        ('BannerAtivo', 'BannerAtivo'),
        ('BanneInativo', 'BanneInativo'),
        ('ImagensGeral', 'ImagensGeral'),
        ('Outros', 'Outros')
    )
    # Deixei um deafult = 'Arquivo' para arquivos antigos tere um nome temp
    nome = models.CharField(max_length=100, default='Arquivo')
    Arquivo = models.FileField(upload_to="web/")
    tipo = models.CharField(max_length=30, choices=tipo_arquivo, default='Outros')
    descricao = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.nome

    def url(self):
        return self.Arquivo.url


def nomedoarquivo(instance,filename):
    return("banco_de_provas/" +  '-'.join([instance.materia, instance.tipo,instance.semestre,instance.professor]) + filename[-4:])
