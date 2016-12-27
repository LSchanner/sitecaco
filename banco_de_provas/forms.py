from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

from banco_de_provas.models import Prova

class ProvaForm(forms.ModelForm):
    materia = forms.RegexField(label="Matéria", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: MC102",
            error_message="Mensagem de erro" )

    semestre = forms.RegexField(label="Semestre", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: 2014s2",
            error_message="Mensagem de erro",
            required=False
            )

    tipo = forms.RegexField(label="tipo", max_length=10, regex=r'.*', #futuramente podemos validar esse campo
            help_text= "Ex: p1",
            error_message="Mensagem de erro")

    class Meta:
        model = Prova
        fields = '__all__'
