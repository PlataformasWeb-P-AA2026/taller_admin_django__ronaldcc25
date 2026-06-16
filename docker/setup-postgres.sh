#!/bin/bash

# Script para levantar PostgreSQL y PgAdmin con docker compose

set -e

# Ir a la carpeta docker
cd "$(dirname "$0")"

# Levantar los contenedores
docker compose up -d
