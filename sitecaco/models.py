from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.flatpages.models import FlatPage



class Noticia(models.Model):
    user = models.ForeignKey(User, editable = False)
    title = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.title)


class Ata(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.title)

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia)
    author = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return self.author + " no post " + self.noticia.title


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


class Produto(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    imagem = models.ImageField()

    def __str__(self):
        return self.name

class formComentario(forms.Form):
    author = forms.CharField(label="Nome",max_length=50)
    content = forms.CharField(label = "Comentário",widget = forms.Textarea)


# O intuito desse modelo é apenas deixar que os administradores façam upload
# de coisas arbitrárias para o site.
class Arquivo(models.Model):
    Arquivo = models.FileField(upload_to="web/")

    def __str__(self):
        return self.Arquivo.url


# Salva o arquivo com um nome regular
def nomedoarquivo(instance,filename):
    return("banco_de_provas/" +  '-'.join([instance.materia, instance.tipo,instance.semestre,instance.professor]) + filename[-4:])



# Modelo do banco de provas
class Prova(models.Model):
    file = models.FileField(upload_to=nomedoarquivo)
    materia = models.CharField(max_length=10)
    semestre = models.CharField(max_length=10)
    professor = models.CharField(max_length=50,blank=True)
    tipo = models.CharField(max_length=15)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.materia + " " + self.tipo + " " + self.professor + " " +  self.semestre






