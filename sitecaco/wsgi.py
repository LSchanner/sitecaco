"""
WSGI config for crashcourse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application

import os
import simplejson as json

from dj_static import Cling, MediaCling


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitecaco.settings")

# Carrega variáveis necessárias para o funcionamento do wsgi
config = json.load(open(BASE_DIR+'/config.json'))

# Setando para ambiente de produção com dj_static
# dessa maneira não é necessário configurar nginx para static e media
# https://github.com/kennethreitz/dj-static
if config['DEBUG']:
    application = get_wsgi_application()
else:
    application = Cling(MediaCling(get_wsgi_application()))
