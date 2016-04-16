#Funções úteis a todas as views
from .views_common import *

import urllib.request,urllib.parse
import json
from django.core.mail import send_mail
from sitecaco.settings import RECAPTCHA_SECRET

def view(request):
    t = loader.get_template('ouvidoria.html')
    c = RequestContext(request,{})

    if request.method == 'GET':
        return HttpResponse(t.render(c))

    if(not verify_recaptcha(request)):
        return HttpResponse(t.render(c))

    header = ""
    if request.POST['email']:
        header = " email para resposta: " + request.POST['email'] + \
                "\n\n---------------------------------------------\n\n"

    send_mail("Ouvidoria: " + request.POST['subject'], header + request.POST['message'] ,
            "caco@ic.unicamp.br", ['caco@ic.unicamp.br'])

    t = loader.get_template('obrigado.html')
    c['mensagem'] = """
            Obrigado por entrar em contato.

            Se você deixou um email, em breve responderemos sua mensagem.
            """

    return HttpResponse(t.render(c))


def verify_recaptcha(request):
    try:
        post_data = [('secret',RECAPTCHA_SECRET),
                ('response',request.POST['g-recaptcha-response']),
                ('remoteip',client_ip(request))]
    except:
        return False

    post_data = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request(
            'https://www.google.com/recaptcha/api/siteverify',
            post_data
            )
    result = urllib.request.urlopen(req).read()
    return json.loads(result.decode('utf-8'))['success']


# Retorna o ip de uma solicitação HTTP. Lida inteligentemente com proxies
def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

