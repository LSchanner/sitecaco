from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from sitecaco.models import *
import re

def DV_maker(v):
    if v >= 2:
        return 11 - v
        return 0

#Field de CPF
class CPFField(Field):
    def __init__(self,*args,**kwargs):
        super(CPFField, self).__init__(error_messages = {"required":"Este campo é obrigatório"},*args,**kwargs)

    #Função de validar cpf, copiada da net huehue
    def validate_CPF(self, value):
        """
        Value can be either a string in the format XXX.XXX.XXX-XX or an
        11-digit number.
        """
        if value in EMPTY_VALUES:
            return u''
        if not value.isdigit():
            value = re.sub("[-\.]", "", value)
        orig_value = value[:]
        try:
            int(value)
        except ValueError:
            raise ValidationError("Este campo deve conter apenas dígitos ou caracteres '-' e '.'")
        if len(value) != 11:
            raise ValidationError("Número de dígitos errado")
        orig_dv = value[-2:]

        new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
        new_1dv = DV_maker(new_1dv % 11)
        value = value[:-2] + str(new_1dv) + value[-1]
        new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
        new_2dv = DV_maker(new_2dv % 11)
        value = value[:-1] + str(new_2dv)
        if value[-2:] != orig_dv:
            raise ValidationError("CPF inválido")
        return orig_value


    def clean(self, value):
        value = super(CPFField, self).clean(value)
        orig_value = self.validate_CPF(value)
        return orig_value

# Form de inscrição
class FormInscricaoFisl(forms.ModelForm):
    RA = forms.CharField(max_length=10,required=False,label="RA",
            help_text="Apenas para alunos Unicamp")
    cpf = CPFField(label="CPF")

    class Meta:
        model = InscricaoFISL
        fields = ["nome","email","sexo","RA","nascimento","cidade","cpf","RG","Orgao_expedidor","telefone","vinculo"]
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'sexo': 'Sexo',
            'nascimento': 'Data de Nascimento',
            'cidade': 'Cidade',
            'Orgao_expedidor': 'Orgão Expedidor do RG',
            'telefone': 'Número de Telefone',
            'vinculo': 'Vínculo com a Unicamp',
        }
        help_texts = {
            'nascimento': 'ex: 1995-10-25',
        }
        error_messages =  {x:{"required":"Este campo é obrigatório"} for x in fields}

