from django.db import models

from sitecaco.tools.token import generateToken

from unidecode import unidecode


# Modelo de um Aluno
# Cada aluno tem um token para gerar um página de confirmação para ele
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.IntegerField(primary_key=True, unique=True)
    token = models.CharField(max_length = 37)
    confirmado = models.BooleanField(default = False)
    email_pessoal = models.EmailField()
    nascimento = models.DateField()
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ra) + ' - ' + self.nome

    def email_ic(self):
        return ('ra'+str(self.ra)+'@students.ic.unicamp.br')

    def email_dac(self):
        firstLetter = self.nome[0].lower()
        firstLetter = unidecode(firstLetter)
        ra = str(self.ra)
        mail = '@dac.unicamp.br'
        return (firstLetter + ra + mail)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.token = generateToken(self.nome + str(self.ra))
    #     super().save(*args, **kwargs)
