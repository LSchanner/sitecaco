#Funções úteis a todas as views
from .views_common import *
import sitecaco.forms as forms

mensagem = """
    Sua Pré-Inscrição foi enviada com sucesso.

    Em breve entraremos em contato.
    """

def view(request):

    if request.method == 'GET':
        t = loader.get_template('inscricaofisl.html')
        c = RequestContext(request,{"form":forms.FormInscricaoFisl})
        return HttpResponse(t.render(c))

    else:
        form = forms.FormInscricaoFisl(request.POST)
        if form.is_valid():
            form.save()
            t = loader.get_template("obrigado.html")
            c = Context({"mensagem":mensagem})
            return HttpResponse(t.render(c))

    t = loader.get_template('inscricaofisl.html')
    c = RequestContext(request,{"form":form})
    return HttpResponse(t.render(c))

