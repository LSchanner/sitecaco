FROM ubuntu:latest
MAINTAINER Centro Academico da Computação - CACo caco@ic.unicamp.br

RUN apt-get update &&\
    apt-get upgrade -y && \
    apt-get install -y \
    build-essential \
    ca-certificates \
    git \
    libpq-dev \
    make \
    pkg-config \
    python3 \
    python3-pip \
    python3-dev \
    libssl-dev \
    libssl-dev &&\
    apt-get autoremove &&\
    apt-get clean

COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY ./static/ /static/
COPY . /code/

WORKDIR /code

RUN echo "America/Sao_Paulo" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

VOLUME /static

CMD ["uwsgi", "--chdir", "/code/", "--module", "sitecaco.wsgi:application", "--socket", "0.0.0.0:8001", "--processes", "5", "--max-requests", "5000", "--vacuum", "--buffer-size", "32768", "--harakiri", "20", "--master"]
