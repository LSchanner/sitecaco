# Arquivo de reload para produção do código do site
# Se detectar alguma mudança no projeto, ele dispara um uwsgi.reload()
from django.utils import autoreload
from django.conf import settings

import uwsgi
from uwsgidecorators import timer

# Ajuste do autoreload
@timer(6)
def change_code_gracefull_reload(sig):
    if autoreload.code_changed():
        uwsgi.reload()
