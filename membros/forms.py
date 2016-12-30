from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

from membros.models import Aluno

import re

# Form de inscrição
class FormInscricaoMembros(forms.ModelForm):
    vinculo = (
        ('Graduacao', 'Graduacao'),
        ('Pós', 'Pós'),
    )
    nome = forms.CharField(label='Seu Nome', max_length=150)
    ra = forms.IntegerField(label='Seu RA')
    email_pessoal = forms.EmailField(label='Email')
    nascimento = forms.DateField(input_formats=
                                                ['%d-%m-%Y',      # '23-11-1994'
                                                 '%d/%m/%Y'],     # '23/11/1994'
                                 label='Data de Nascimento',
                                 help_text='ex: 23/11/1994'
                                 )
    cpf = forms.CharField(label='CPF', help_text='Sem pontos e espaco, apenas os números')
    vinculo = forms.ChoiceField(vinculo)

    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'email_pessoal', 'nascimento', 'cpf', 'vinculo']
        error_messages =  {x:{"required":"Este campo é obrigatório"} for x in fields}
