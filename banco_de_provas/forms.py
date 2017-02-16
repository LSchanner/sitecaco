from django import forms
from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError

from banco_de_provas.models import Prova

class ProvaForm(forms.ModelForm):
    materia = forms.RegexField(label="Matéria",
                               max_length=10,
                               regex=r'.*', # podemos validar esse campo?
                               help_text= "Ex: MC102",
                               error_message="Matéria Inválida"
                               )

    semestre = forms.RegexField(label="Semestre",
                                max_length=10,
                                regex=r'.*', # podemos validar esse campo
                                help_text= "Ex: 2014s1, 2015s2, 2016fer",
                                error_message="Semestre inválido",
                                required=False
                                )

    tipo = forms.RegexField(label="Tipo",
                            max_length=10,
                            regex=r'.*', #futuramente podemos validar esse campo
                            help_text= "Ex: p1, p2_res, teste1, exame, lista",
                            error_message="Tipo incorreto"
                            )
    professor = forms.CharField(label="Professor",
                                max_length=50,
                                help_text="Nome do professor que está ministrando a matéria",
                                required=False)
    file = forms.FileField(label="Arquivo",
                           help_text="Dê preferencia para arquivos PDF"
                        );

    class Meta:
        model = Prova
        fields = ('materia', 'semestre', 'tipo', 'professor', 'file')
