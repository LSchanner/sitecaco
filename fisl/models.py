from django.db import models

# Modelo de inscrição no FISL
# Modelo de inscrição no FISL
class InscricaoFISL(models.Model):
    generos = (
        ('M', 'M'),
        ('F', 'F'),
    )
    vinculo_com_unicamp = (
        ('Computeiro', 'Aluno Computação Unicamp'),
        ('Unicamper não Computeiro', 'Aluno Unicamp'),
        ('Brother X', 'Nenhum/Outro')
    )
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    sexo = models.CharField(max_length=150,choices=generos)
    RA = models.CharField(max_length=10,null=True)
    nascimento = models.DateField()
    cidade = models.CharField(max_length=150)
    cpf = models.CharField(max_length=20)
    RG = models.CharField(max_length=20)
    Orgao_expedidor = models.CharField(max_length=20)
    telefone = models.CharField(max_length=30)
    vinculo = models.CharField(max_length=50,choices=vinculo_com_unicamp)

    def __str__(self):
        return self.nome
