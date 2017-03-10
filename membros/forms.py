from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

from membros.models import Aluno

import re


AGREEMENT_TEXT='Li e concordo com o <a href="http://www.caco.ic.unicamp.br/media/web/EstatutoCACo.pdf">Estatuto do CACo</a>'


# Form de inscrição
class FormInscricaoMembros(forms.ModelForm):
    vinculo = (
        ('Graduacao', 'Graduacao'),
        ('Pós', 'Pós'),
    )
    nome = forms.CharField(label='Seu Nome Completo',
                            max_length=150)
    ra = forms.IntegerField(label='Seu RA')
    ano_ingresso = forms.DateField(input_formats=['%Y'],
                                    label='Ano de Ingresso',
                                    help_text='ex: 2014'
                                    )
    vinculo = forms.ChoiceField(vinculo)
    email_pessoal = forms.EmailField(label='Email Pessoal',required=True)
    concordo = forms.BooleanField(label=AGREEMENT_TEXT,
                                  required = True);

    #nascimento = forms.DateField(input_formats=
    #                                            ['%d-%m-%Y',      # '23-11-1994'
    #                                             '%d/%m/%Y'],     # '23/11/1994'
    #                             label='Data de Nascimento',
    #                             help_text='ex: 23/11/1994'
    #                             )
    #cpf = forms.CharField(label='CPF', help_text='Sem pontos e espaco, apenas os números')


    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'vinculo', 'ano_ingresso', 'email_pessoal']
