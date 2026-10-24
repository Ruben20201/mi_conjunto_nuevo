#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos para que Render los muestre correctamente
python manage.py collectstatic --no-input

# Aplicar las migraciones a la base de datos de producción
python manage.py migrate