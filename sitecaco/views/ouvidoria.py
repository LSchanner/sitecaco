#Funções úteis a todas as views
from .views_common import *

from django.core.mail import send_mail

def view(request):
    t = loader.get_template('ouvidoria.html')
    c = RequestContext(request,{})

    if request.method == 'GET':
        return HttpResponse(t.render(c))

    send_mail(request.POST['subject'], request.POST['message'] ,
            request.POST['email'], ['caco@ic.unicamp.br'])

    t = loader.get_template('obrigado.html')
    return HttpResponse(t.render(c))



