from django.shortcuts import render
from django.template import loader, RequestContext, Context as Con
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

from haystack.query import SearchQuerySet

from sitecaco.settings import URL_BASE
from sitecaco.models import *


# HTTP Error 404
def page_not_found(request):
    return render(request, '404.html')


# HTTP Error 500
def server_error(request):
    return render(request, '500.html')
    response =  render_to_response(
        '500.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 500

    return response


# Wrapper sobre a função do django "Context", para incluir sempre a URL base
def Context(dicionario):
    dicionario['URL_BASE'] = URL_BASE
    return Con(dicionario)
