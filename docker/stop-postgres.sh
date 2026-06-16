#!/bin/bash

# Script para detener PostgreSQL y PgAdmin

echo "======================================"
echo "Deteniendo contenedores..."
echo "======================================"

docker compose down

echo "======================================"
echo "✓ Contenedores detenidos"
echo "======================================"
