from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings

from membros.models import Aluno
from membros.forms import FormInscricaoMembros

from sitecaco.tools.token import generateToken


URL = 'http://127.0.0.1:8000/'
FROM_EMAIL = 'CACo <caco@ic.unicamp.br>'
inscricao_confirmada = """
    Você completou sua inscrição, um email foi mandado ao email academico do IC para que você confirme sua identidade.

    Cheque seu email em até 30 minutos e se não receber, entre em contato em nosso email
    """


# Home dos membros
# Lista todos os membros do CACo
def homeMembros(request):
    c = dict()
    membros = Aluno.objects.filter(confirmado=True)
    c['membros'] = membros

    return render(request, 'membros.html', c)

    return redirect('/noticias')

# View para gerar o forms de inscricao de membros
def forms_incricao_membros(request):
    if request.method == 'GET':
        return render(request, 'inscricaoMembros.html', {"form": FormInscricaoMembros})

    # Caso a requisao seja post...
    # (Talvez seja melhor ser explicitamente post, e isso acontece em mais
    #  locais do código)
    form = FormInscricaoMembros(request.POST)
    if form.is_valid():
        # Salva o formulario e adiciona o token unico nele
        a = form.save()
        a.token = generateToken(a.nome + str(a.ra))
        a.save()

        # Para envio do email
        header = '[CACo] Confirmação da Inscricao para Membro'
        link = URL + 'membros/confirmacao/' + str(a.token)
        message = 'Olá, essa é uma mensagem automatica para envio do link de inscricao de membro do CACo. \nO link para sua confirmação é: %s\nCaso tenha recebido esse email por engano, por favor, apenas desconsidere a mensagem <3\n\n' % link

        # Faz um novo email
        email = EmailMessage(
            header,
            message,
            FROM_EMAIL,
            [a.email_ic()]
        )

        # Caso esteja no modo debug, nao envia o email, apenas imprime na tela
        if settings.DEBUG:
            print('TO: ' + str(a))
            print(header)
            print(message)
        else:
            email.send()

        return render(request, 'obrigado.html', {"mensagem": inscricao_confirmada})

    return render(request, 'inscricaoMembros.html', {"form": form})


def dealToken(request, token):
    c = dict()
    aluno_para_confirmar = get_object_or_404(Aluno, token=token)

    # Caso o token já tenha sido utilizado
    if aluno_para_confirmar.confirmado:
        c['title'] = 'Aluno já confirmado'
        c['body'] = """ Esse token já foi utilizado.
                        Se você esta tendo problemas para fazer login, entre em contato conosco na aba contato
                    """
        return render(request, 'confirmacaoMembros.html', c)

    # Caso esteja lidando com um token que será
    aluno_para_confirmar.confirmado = True
    aluno_para_confirmar.save()


    # TODOS : Elaborar textos melhores para as páginas
    c['title'] = 'Você confirmou sua incrição como membro do CACo'
    c['body'] = 'Seja bem vindo como membro do CACo {primeiro_nome}!'.format(primeiro_nome=aluno_para_confirmar.nome.partition(' ')[0])
    return render(request, 'confirmacaoMembros.html', c)
