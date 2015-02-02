#Funções úteis a todas as views
from .views_common import *

from django.core.mail import send_mail

def view(request):
    t = loader.get_template('ouvidoria.html')
    c = RequestContext(request,{})

    if request.method == 'GET':
        return HttpResponse(t.render(c))

    send_mail(request.POST['subject'], request.POST['message'] ,
            'ouvidoria@caco.ic.unicamp.br', ['caco@ic.unicamp.br'], fail_silently=False)

    return HttpResponse(t.render(c))



