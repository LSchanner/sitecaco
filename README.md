# Site do CACo

Este é o código do site do CACo, servido na url www.caco.ic.unicamp.br

Todos são bem-vindos a colaborar com o desenvolvimento, reportar bugs ou pedir features.

## Instalação
### virtualenv
É recomendado executar o projeto e instalar as dependências em um ambiente virtual de Python (virtualenv) para evitar conflitos de versões e problemas de dependencias. Para isso, execute os seguintes comandos para criar o ambiente virtual e ativá-lo.

#### Instalando
    pip3 install virtualenv

#### Executando
    virtualenv env
    source env/bin/activate

Para desativar o ambiente, basta executar o comando `deactivate`, carregado ao se ativar o ambiente.

### Requerimentos do sistema
* python 3
* pip 3

### Dependencias
Todas as dependencias estão no arquivo dependencies.txt na raiz do projeto

#### Instalando com pip
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
    # https://docs.djangoproject.com/en/1.10/ref/settings/#email-backend

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Configurações para envio de email - configure de sua maneira
    # as configurações podem varias dependendo do seu servidor
    # EMAIL_HOST = 'smtp.gmail.com'  
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # EMAIL_HOST_USER = 'email@gmail.com'
    # EMAIL_HOST_PASSWORD = 'senha'

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

## Dump do BD
### Exportando
    python3 manage.py dumpdata -e contenttypes -e admin -e auth.Permission --natural-foreign --indent=2 > bd.json

### Importando
    python3 manage.py loaddata bd.json
