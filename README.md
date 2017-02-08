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

##### config.json
crie o arquivo `config.json` com o seguinte conteúdo - modificando nas partes necessárias
```json
{
  "URL_BASE": "",
  "DEBUG": true,
  "SECRET_KEY": "chave-super-ultra-hiper-mega-secreta",
  "LANGUAGE_CODE": "pt-BR",
  "TIME_ZONE": "America/Sao_Paulo",
  "DATABASE_NAME": "db.sqlite3",
  "DATABASE_USER": "user do postgres(só necessario se usado com NAME postgres)",
  "DATABASE_PASS": "pass do postgres(só necessario se usado com NAME postgres)",
  "DATABASE_HOST": "host do postgres(só necessario se usado com NAME postgres)",
  "DATABASE_PORT": 5432,
  "EMAIL_HOST": "smtp.gmail.com",
  "EMAIL_PORT": 587,
  "EMAIL_USE_TLS": true,
  "EMAIL_HOST_USER": "seu email",
  "EMAIL_HOST_PASSWORD": "sua senha",
  "RECAPTCHA_SECRET": "recaptcha secret"
}

```
os dois tipos de database disponíveis de cara para serem executados são `db.sqlite3` ou `postgres`


depois, execute
```console
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### Docker
Se você possui [Docker](https://docs.docker.com/engine/installation/) (com [Docker Compose](https://docs.docker.com/compose/install/)) você pode rodar o site com PostgreSQL e NGINX utilizando-o. Para isso, crie o arquivo `config.json` com o seguinte conteudo (substituindo as variaveis `$` do jeito necessario):

##### config.json

```json
{
  "URL_BASE": "",
  "DEBUG": true,
  "SECRET_KEY": "chave_secreta",
  "LANGUAGE_CODE": "pt-BR",
  "TIME_ZONE": "America/Sao_Paulo",
  "DATABASE_NAME": "postgres",
  "DATABASE_USER": "postgres",
  "DATABASE_PASS": "postgres",
  "DATABASE_HOST": "postgres",
  "DATABASE_PORT": 5432,
  "EMAIL_HOST": "smtp.gmail.com",
  "EMAIL_PORT": 587,
  "EMAIL_USE_TLS": true,
  "EMAIL_HOST_USER": "seu-email",
  "EMAIL_HOST_PASSWORD": "sua-senha",
  "RECAPTCHA_SECRET": "segredo-do-recaptcha"
}
```

e depois executar os seguintes comandos:

```console
$ docker-compose up -d --build
$ docker-compose run --rm site_do_caco python manage.py migrate

$ (...)
```

você pode acessar atravéz da porta 80 em localhost

## Dados
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
