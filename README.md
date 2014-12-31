# Site do CACo

## Instalação
### requerimentos do sistema
    * python3

#### libs de python (instale com pip)
    * django
    * pymysql
    * django-forms-bootstp
    * django-haystack
    * pillow
    

### procedimento
    clone o repositório,  
    crie o sitecaco/local_settings.py com o seguinte conteúdo:
    ```
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    SECRET_KEY = "iawepcruqp943rvanh39845yvmmhmofn24jnmnafiuwenkjnbxmcn2948ajv"

    # SECURITY WARNING: don't run with debug turned on in production!  
    DEBUG = True
    TEMPLATE_DEBUG = True 

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }

    # Search Engine
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    }


    #URL Base, usado em todos os links absolutos do site
    URL_BASE = ""

    ```
    depois, execute

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
    ```
    Qualquer problema, não hesite em contatar os administradores do repositório 


