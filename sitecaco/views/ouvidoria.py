#Funções úteis a todas as views
from .views_common import *

from django.core.mail import send_mail

def view(request):
    t = loader.get_template('ouvidoria.html')
    c = RequestContext(request,{})

    if request.method == 'GET':
        return HttpResponse(t.render(c))

    header = ""
    if request.POST['email']:
        header = " email para resposta:" + request.POST['email'] + \
                "\n\n---------------------------------------------\n\n"

    send_mail("Ouvidoria: " + request.POST['subject'], header + request.POST['message'] ,
            "caco@ic.unicamp.br", ['caco@ic.unicamp.br'])

    t = loader.get_template('obrigado.html')
    c['mensagem'] = """
            Obrigado por entrar em contato.
            <br>
            Se você deixou um email, em breve responderemos sua mensagem.
            """

    return HttpResponse(t.render(c))



