from django import forms

from sitecaco.models import Arquivo

texto_arquivo = """
        Banners devem ter o formato 940x440
    """

texto_tipo = """
        Qual a finalidade desse arquivo
    """

texto_descricao = """
        Uma breve descricao do arquivo/imagem.
        Para uma imagem, esse texto será adicionado no campo alt (que é usado por deficientes visuais para saber sobre a imagem)
    """

class formComentario(forms.Form):
    author = forms.CharField(label="Nome",max_length=50)
    content = forms.CharField(label = "Comentário",widget = forms.Textarea)

class formArquivo(forms.ModelForm):
    tipo_arquivo = (
        ('BannerAtivo', 'BannerAtivo'),
        ('BanneInativo', 'BanneInativo'),
        ('ImagensGeral', 'ImagensGeral'),
        ('Outros', 'Outros')
    )

    nome = forms.CharField(help_text='Nome do Arquivo')
    Arquivo = forms.FileField(help_text=texto_arquivo)
    tipo = forms.ChoiceField(choices=tipo_arquivo, help_text=texto_tipo)
    descricao = forms.CharField(required=False, help_text=texto_descricao)

    class Meta:
        model = Arquivo
        fields = ['nome','Arquivo','tipo','descricao']
