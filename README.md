# Site do CACo

Este é o código do site do CACo, servido na url www.caco.ic.unicamp.br

Todos são bem-vindos a colaborar com o desenvolvimento, reportar bugs ou pedir features.

## Instalação
### Requerimentos do sistema
* python3

### Bibliotecas de python
* django
* pymysql
* django-forms-bootstrap
* django-haystack
* pillow

#### instalando com pip
    pip3 install -r dependencies.txt


### Procedimento
crie o arquivo `sitecaco/local_settings.py` com o seguinte conteúdo:

    import os


    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    SECRET_KEY = "chave_aleatória_qualquer"

    DEBUG = True

    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }

    # Search Engine
    # https://django-haystack.readthedocs.io
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    }

    # Email Console backend
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # URL Base, usado em todos os links absolutos do site
    URL_BASE = ""

    RECAPTCHA_SECRET = "o_segredo_do_recaptcha_do_google"

depois, execute

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

para criar um usuário admin e poder logar em /admin/

    python3 manage.py createsuperuser


Qualquer problema, não hesite em contatar os administradores do repositório
