#!/bin/bash
echo "=== INICIANDO DIAGNÓSTICO ==="
echo "Verificando variáveis de ambiente..."
echo "DEBUG: $DEBUG"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "PORT: $PORT"

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Executando migrações..."
python manage.py migrate --noinput

echo "Testando configuração Django..."
python manage.py check --deploy

echo "Iniciando Gunicorn..."
exec gunicorn config.wsgi --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --log-level debug --access-logfile - --error-logfile -
