from django import forms

from ckeditor.widgets import CKEditorWidget

from loja.models import Produto

class formsProduto(forms.ModelForm):
    name = forms.CharField()
    price = forms.IntegerField()
    description = forms.CharField(widget=CKEditorWidget())
    imagem = forms.ImageField()

    class Meta:
        model = Produto
        fields = ['name','price','description','imagem']
