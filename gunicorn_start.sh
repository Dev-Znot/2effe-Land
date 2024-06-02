#!/bin/bash

NAME="setup"                  # Nome da aplicação
DJANGODIR=C:\Users\thall\OneDrive\Documentos\programação\Trabalho\Dragonfy Ltda\2effe Land\setup   # Caminho para o diretório do projeto Django
USER=Thalles                     # O usuário que vai executar o Gunicorn
GROUP=Dragonfy                       # O grupo que vai executar o Gunicorn
WORKERS=1                            # Número de processos worker do Gunicorn
BIND=unix:/run/gunicorn.sock            # Endereço onde o Gunicorn vai escutar
DJANGO_SETTINGS_MODULE=setup.settings  # Nome do módulo de configurações do Django
DJANGO_WSGI_MODULE=setup.wsgi     # Nome do módulo WSGI do Django

echo "Iniciando $NAME as `date`"

# Ativa o ambiente virtual
cd $DJANGODIR
source C:\Users\thall\OneDrive\Documentos\programação\Trabalho\Dragonfy Ltda\2effe Land\env

# Inicia o Gunicorn
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER --group=$GROUP \
  --bind=$BIND \
  --log-level=debug \
  --log-file=-
