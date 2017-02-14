from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings

import simplejson as json

from membros.models import Aluno
from membros.forms import FormInscricaoMembros
from sitecaco.tools.token import generateToken

config = json.load(open('config.json'))

URL = config['URL_NAME']
# Nome vai ser: Nome <nome@email.com>
FROM_EMAIL = config['EMAIL_NAME'] + ' <' + config['EMAIL_HOST_USER'] + '>'

INCRICAO_CONFIRMADA = """
    Você completou sua inscrição, um email foi mandado ao email academico do IC para que você confirme sua identidade.

    Cheque seu email em até 30 minutos e se não receber, entre em contato em nosso email
    """
MSG_EMAIL = """
    Olá, essa é uma mensagem automatica para envio do link de inscricao de membro do CACo.
    O link para sua confirmação é: {}

    Caso tenha recebido esse email por engano, por favor, apenas desconsidere a mensagem <3. Mas se você aina não for membro do CACo, torne-se um!
    """
MSG_BOAS_VINDAS = """
    Seja bem vindo como membro do CACo {primeiro_nome}!
    Ficamos muito contentes em ter você conosco. Participe de nossas reuniões e aproveite a nossa salinha!
    """
MSG_ERRO_TOKEN = """
    Esse token já foi utilizado.
    Se você esta tendo problemas para fazer login, entre em contato conosco na aba contato
    """


# Home dos membros
# Lista todos os membros do CACow
def homeMembros(request):
    c = dict()
    membros = Aluno.objects.filter(membro_confirmado=True).order_by('ra')
    c['membros'] = membros

    return render(request, 'membros.html', c)

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
        sjt = '[CACo] Confirmação da Inscricao para Membro'
        link = URL + 'membros/confirmacao/' + str(a.token)
        msg = MSG_EMAIL.format(link)

        # Faz um novo email
        email = EmailMessage(
            sjt,
            msg,
            FROM_EMAIL,
            [a.email_ic()]
        )

        # Caso esteja no modo debug, nao envia o email, apenas imprime na tela
        try:
            email.send()

            return render(request, 'obrigado.html', {"mensagem": INCRICAO_CONFIRMADA})
        except Exception as inst:
            print("Erro ao enviar email membros")
            print(type(inst))
            print(inst)

    return render(request, 'inscricaoMembros.html', {"form": form})


# View para lidar com o token
def dealToken(request, token):
    c = dict()
    aluno_para_confirmar = get_object_or_404(Aluno, token=token)

    # Caso o token já tenha sido utilizado
    if aluno_para_confirmar.membro_confirmado:
        c['title'] = 'Aluno já confirmado'
        c['body'] = MSG_ERRO_TOKEN
        return render(request, 'confirmacaoMembros.html', c)

    # Caso esteja lidando com um token que será
    aluno_para_confirmar.membro_confirmado = True
    aluno_para_confirmar.save()


    # TODOS : Elaborar textos melhores para as páginas
    c['title'] = 'Você confirmou sua incrição como membro do CACo'
    c['body'] = MSG_BOAS_VINDAS.format(
                    primeiro_nome=aluno_para_confirmar.nome.partition(' ')[0]
                )
    return render(request, 'confirmacaoMembros.html', c)
