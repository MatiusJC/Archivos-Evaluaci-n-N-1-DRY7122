#!/bin/bash

# Contenido de la carpeta actual
echo "El contenido de la carpeta prueba1 es:"
ls

# Proceso que permite la ejecución del archivo
echo "El proceso que permite la ejecución del archivo es:"
echo "$0"

# Modificacion de los atributos del archivo
chmod 700 $0

# Nombre completo del alumno
echo "El nombre completo del alumno es: Matias Acuña"
