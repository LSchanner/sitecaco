from django.db import models
from django import forms


class formComentario(forms.Form):
    author = forms.CharField(label="Nome",max_length=50)
    content = forms.CharField(label = "Comentário",widget = forms.Textarea)


# O intuito desse modelo é apenas deixar que os administradores façam upload
# de coisas arbitrárias para o site.
class Arquivo(models.Model):
    Arquivo = models.FileField(upload_to="web/")

    def __str__(self):
        return self.Arquivo.url


def nomedoarquivo(instance,filename):
    return("banco_de_provas/" +  '-'.join([instance.materia, instance.tipo,instance.semestre,instance.professor]) + filename[-4:])
