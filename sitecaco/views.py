from django.shortcuts import render

from sitecaco.settings import URL_BASE


# HTTP Error 404
def page_not_found(request):
    return render(request, '404.html')

# HTTP Error 500
def server_error(request):
    return render(request, '500.html')

# Wrapper sobre a função do django "Context", para incluir sempre a URL base
def Context(dicionario):
    dicionario['URL_BASE'] = URL_BASE
    return Con(dicionario)
