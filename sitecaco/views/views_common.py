#Imports e funções uteis a todas as views

from sitecaco.models import *
from haystack.query import SearchQuerySet
from django.template import loader, RequestContext, Context as Con
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from sitecaco.settings import URL_BASE
from django.core.paginator import Paginator


# Wrapper sobre a função do django "Context", para incluir sempre a URL base
def Context(dicionario):
    dicionario['URL_BASE'] = URL_BASE
    return Con(dicionario)


