# Docker Setup - PostgreSQL + PgAdmin

## Instrucciones Rápidas

### 1. Levantar Servicios

```bash
cd docker
./setup-postgres.sh
```

### 2. En otra terminal, levantar Django

```bash
cd patrimonio
DB_ENGINE=postgresql python manage.py runserver
```

### 3. Acceder a servicios

- Django Admin: http://127.0.0.1:8000/admin/
- PgAdmin: http://localhost:5050

### 4. Detener servicios

```bash
cd docker
./stop-postgres.sh
```

---

## Archivos

- `docker-compose.yml` - Configuración de servicios
- `.env` - Variables de entorno
- `setup-postgres.sh` - Script de inicio
- `stop-postgres.sh` - Script de parada
