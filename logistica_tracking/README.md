# Plataforma de Monitoreo de Envíos Logísticos

Sistema completo para gestionar clientes, transportistas, envíos y tracking de paquetes.

## Arquitectura

- **Backend**: Django + Django REST Framework + SQLite
- **Frontend**: HTML + CSS + JavaScript (Fetch API)
- **Documentación**: DRF (Swagger deshabilitado temporalmente)

## Instalación

1. Clonar o descargar el proyecto.
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Migrar base de datos: `python manage.py migrate`
6. Ejecutar servidor: `python manage.py runserver`

## Uso

- Abrir `frontend/index.html` en el navegador.
- El backend corre en `http://127.0.0.1:8000`

## APIs

- Clientes: `/api/clientes/`
- Transportistas: `/api/proveedores/`
- Envíos: `/api/envios/`
- Tracking: `/api/tracking/{tracking_number}/`
- API Externa Simulada: `/external-api/tracking/{tracking_number}/`
- JWT Token: `/api/token/` (POST con username/password)
- JWT Refresh: `/api/token/refresh/` (POST con refresh token)
- Swagger UI: `/api/schema/swagger-ui/`
- ReDoc: `/api/schema/redoc/`
- Schema: `/api/schema/`

## Autenticación JWT

Para usar las APIs protegidas, obtener un token JWT:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password"}'
```

Usar el token en headers: `Authorization: Bearer <token>`

## Pruebas con Postman

Importar colección de Postman con los endpoints arriba. Para APIs que requieren autenticación, incluir el header Authorization.

## Notas

- JWT deshabilitado temporalmente.
- Swagger deshabilitado por compatibilidad con Python 3.14.