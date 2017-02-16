from django.shortcuts import render
#Funções úteis a todas as views
import fisl.forms as forms

inscricao_confirmada = """
    Sua Pré-Inscrição foi enviada com sucesso.

    Em breve entraremos em contato.
    """
inscricao_fechada = """
    As inscrições para o caravana para o FISL desse ano já foram encerradas.

    """

def submit_form(request):
    if request.method == 'GET':
        return render(request, 'inscricaofisl.html', {"form": forms.FormInscricaoFisl})

    else:
        form = forms.FormInscricaoFisl(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'obrigado.html', {"mensagem": inscricao_confirmada})

    return render(request, 'inscricaofisl.html', {"form": form})


def inscricoes_fechadas(request):
    return render(request, 'inscricaofisl.html', {"fechadas": True})
