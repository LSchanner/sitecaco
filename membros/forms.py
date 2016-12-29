from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

from membros.models import Aluno

import re

# Form de inscrição
class FormInscricaoMembros(forms.ModelForm):
    nome = forms.CharField(label='Seu Nome', max_length=150)
    ra = forms.IntegerField(label='Seu RA')
    email_pessoal = forms.EmailField(label='Algum email para contato que não seja academico')
    nascimento = forms.DateField(input_formats=
                                                ['%d-%m-%Y',      # '23-11-1994'
                                                 '%d/%m/%Y'],     # '23/11/1994'
                                )
    cpf = forms.CharField(label='CPF')

    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'email_pessoal', 'nascimento', 'cpf']
        labels = {
            'nome': 'Nome Completo',
            'ra': 'RA',
            'email_pessoal': 'Email',
            'nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
        }
        help_texts = {
            'nascimento': 'ex: 23/11/1994',
            'cpf': 'Sem pontos e espaco, apenas os números',
        }
        error_messages =  {x:{"required":"Este campo é obrigatório"} for x in fields}
