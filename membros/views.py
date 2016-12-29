from django.shortcuts import render

#Funções úteis a todas as views
from membros.forms import FormInscricaoMembros

from sitecaco.tools.token import generateToken


inscricao_confirmada = """
    Você completou sua inscrição, um email foi mandado ao email academico do IC para que você confirme sua identidade.

    Cheque seu email em até 30 minutos e se não receber, entre em contato em nosso email
    """


# Home dos membros (pensei em listar os membros inscritos)
def homeMembros(request):
    return redirect('./noticias/')

# View para gerar o forms de inscricao de membros
def forms_incricao_membros(request):
    if request.method == 'GET':
        return render(request, 'inscricaoMembros.html', {"form": FormInscricaoMembros})

    else:
        form = FormInscricaoMembros(request.POST)
        if form.is_valid():
            # Salva o formulario e adiciona o token unico nele
            a = form.save()
            a.token = generateToken(a.nome + str(a.ra))
            a.save()

            # Falta enviar o email para o usuário

            return render(request, 'obrigado.html', {"mensagem": inscricao_confirmada})

    return render(request, 'inscricaoMembros.html', {"form": form})
