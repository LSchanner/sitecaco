from django import forms

from ckeditor.widgets import CKEditorWidget

from institucional.models import Ata

class formsAta(forms.ModelForm):
    title = forms.CharField(label ="Nome",
                            help_text="Deixe em branco para preencher com o modelo usando o dia de hoje - Reunião - DD/MM/YYYY",
                            required=False
                            )
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Ata
        fields = ['title','content']
