# Site do CACo

Este é o código do site do CACo, servido na url www.caco.ic.unicamp.br

Todos são bem-vindos a colaborar com o desenvolvimento, reportar bugs ou pedir features.

1. [Instalação](#instalação)
    1. [Instalação Local](#instalação-local)
    1. [Docker](#docker)
1. [Banco de Dados](#banco-de-dados)

Qualquer problema, não hesite em contatar os administradores do repositório

## Instalação
### Instalação Local
#### virtualenv
É recomendado executar o projeto e instalar as dependências em um ambiente virtual de Python (virtualenv) para evitar conflitos de versões e problemas de dependencias. Para isso, execute os seguintes comandos para criar o ambiente virtual e ativá-lo.

##### Instalando
```console
$ pip3 install virtualenv
```

##### Executando
```console
$ virtualenv env
$ source env/bin/activate
```

Para desativar o ambiente, basta executar o comando `deactivate`, carregado ao se ativar o ambiente.

### Requerimentos do sistema
 - python 3
 - pip 3

### Dependencias
Todas as dependencias estão no arquivo `requirements.txt` na raiz do projeto

#### Instalando com pip
```console
$ pip3 install -r requirements.txt
```

##### local_settings.py
crie o arquivo `sitecaco/local_settings.py` com o seguinte conteúdo - modificando nas partes necessárias demarcadas com `$`
```python
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = "$chave_aleatória_qualquer"

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
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '$email@gmail.com'
EMAIL_HOST_PASSWORD = '$senha'

# URL Base, usado em todos os links absolutos do site
URL_BASE = ""

RECAPTCHA_SECRET = "$o_segredo_do_recaptcha_do_google"
```

depois, execute
```console
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### Docker
Se você possui [Docker](https://docs.docker.com/engine/installation/) (com [Docker Compose](https://docs.docker.com/compose/install/)) você pode rodar o site com PostgreSQL e NGINX utilizando-o. Para isso, crie o arquivo sitecaco/local_settings.py com o seguinte conteudo (substituindo as variaveis `$` do jeito necessario):

##### local_settings.py

```python
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = "$chave_aleatória_qualquer"

DEBUG = True

# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                      
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '$email@gmail.com'
EMAIL_HOST_PASSWORD = '$senha'

# URL Base, usado em todos os links absolutos do site
URL_BASE = ""

RECAPTCHA_SECRET = "$o_segredo_do_recaptcha_do_google"
```

e depois executar os seguintes comandos:

```console
$ docker-compose up -d --build
$ docker-compose run --rm site_do_caco python manage.py migrate

$ (...)
```

você pode acessar atravéz da porta 80 em localhost

## Banco de Dados
### Admin
para criar um usuário admin e poder logar em /admin/
```console
$ python3 manage.py createsuperuser
```
### Exportando
```console
$ python3 manage.py dumpdata -e contenttypes -e admin -e auth.Permission --natural-foreign --indent=2 > bd.json
```

### Importando
```console
$ python3 manage.py loaddata bd.json
```
