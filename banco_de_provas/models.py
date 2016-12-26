from django.db import models

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
