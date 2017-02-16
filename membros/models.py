from django.db import models

from unidecode import unidecode

from sitecaco.tools.token import generateToken


# Modelo de um Aluno
# Cada aluno tem um token para gerar um página de confirmação para ele
class Aluno(models.Model):
    vinculo = (
        ('Graduacao', 'Graduacao'),
        ('Pós', 'Pós'),
    )
    nome = models.CharField(max_length=100)
    ra = models.IntegerField(primary_key=True, unique=True)
    ano_ingresso = models.DateField(null=True)
    vinculo = models.CharField(max_length=50,choices=vinculo,null=True)
    email_pessoal = models.EmailField(null=True)
    membro_confirmado = models.BooleanField(default = False)
    token = models.CharField(max_length = 37, null=True)
    # Campo auxiliar para confirmações em outros momentos (votação? rs)
    token_auxiliar_confirmado = models.BooleanField(default = False)
    # A pedido, foram removidos essas informações...
    # nascimento = models.DateField()
    # cpf = models.CharField(max_length=20)

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

    def generate_new_token(self):
        self.token = generateToken()
        self.token_auxiliar_confirmado = False

    # Essa funcao foi feita para quando salvar membros que ja eram do caco
    def save(self, *args, **kwargs):
        self.token = generateToken(self.nome + str(self.ra))
        super().save(*args, **kwargs)
