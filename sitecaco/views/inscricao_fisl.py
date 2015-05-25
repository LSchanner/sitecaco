#Funções úteis a todas as views
from .views_common import *
import sitecaco.forms as forms

inscricao_confirmada = """
    Sua Pré-Inscrição foi enviada com sucesso.

    Em breve entraremos em contato.
    """
inscricao_fechada = """
    As inscrições para o caravana para o FISL desse ano já foram encerradas.

    """

def submit_form(request):
    if request.method == 'GET':
        t = loader.get_template('inscricaofisl.html')
        c = RequestContext(request,{"form":forms.FormInscricaoFisl})
        return HttpResponse(t.render(c))

    else:
        form = forms.FormInscricaoFisl(request.POST)
        if form.is_valid():
            form.save()
            t = loader.get_template("obrigado.html")
            c = Context({"mensagem":inscricao_confirmada})
            return HttpResponse(t.render(c))

    t = loader.get_template('inscricaofisl.html')
    c = RequestContext(request,{"form":form})
    return HttpResponse(t.render(c))


def inscricoes_fechadas(request):
    t = loader.get_template("inscricaofisl.html")
    c = Context({"fechadas":True})
    return HttpResponse(t.render(c))
