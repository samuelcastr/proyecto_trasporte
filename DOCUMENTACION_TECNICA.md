# DOCUMENTACIÓN TÉCNICA
## Plataforma de Monitoreo de Envíos Logísticos

---

## PORTADA

**Proyecto:** Plataforma de Monitoreo de Envíos Logísticos

**Versión:** 1.0.0

**Autor:** Samuel (Desarrollo Senior)

**Fecha de Creación:** 25 de Marzo de 2026

**Estado:** Producción

### Tecnologías Principales

- **Backend:** Django 5.1.3 + Django REST Framework
- **Frontend:** HTML5, CSS3, JavaScript Vanilla (Fetch API)
- **Base de Datos:** SQLite3
- **Autenticación:** JWT (Simple JWT)
- **Documentación API:** DRF Spectacular (OpenAPI 3.0)
- **CORS:** Django CORS Headers

---

## ÍNDICE

1. [Portada](#portada)
2. [Introducción](#introducción)
3. [Objetivos](#objetivos)
4. [Alcance del Proyecto](#alcance-del-proyecto)
5. [Tecnologías Utilizadas](#tecnologías-utilizadas)
6. [Arquitectura del Sistema](#arquitectura-del-sistema)
7. [Diseño de Base de Datos](#diseño-de-base-de-datos)
8. [Endpoints de la API](#endpoints-de-la-api)
9. [Instalación del Proyecto](#instalación-del-proyecto)
10. [Estructura del Proyecto](#estructura-del-proyecto)
11. [Conclusión](#conclusión)

---

## INTRODUCCIÓN

### Descripción del Proyecto

La **Plataforma de Monitoreo de Envíos Logísticos** es un sistema integral diseñado para gestionar y monitorear el ciclo completo de envíos en operaciones logísticas. El sistema proporciona funcionalidades para administrar clientes, transportistas, envíos y el seguimiento en tiempo real de paquetes a través de diferentes estados logísticos.

Este sistema permite:

- Registrar y gestionar clientes e información de contacto
- Administrar transportistas y sus servicios de envío
- Crear y monitorear envíos con números de rastreo únicos
- Registrar eventos de seguimiento en tiempo real
- Consultar el estado actual de cualquier envío
- Generar reportes del histórico de entregas

### Propósito del Sistema

El propósito fundamental es proporcionar una solución centralizada que mejore la eficiencia operativa en procesos logísticos, permitiendo:

- **Transparencia:** Clientes y operadores pueden conocer el estado exacto de sus envíos
- **Automatización:** Reducir procesos manuales y minimizar errores
- **Escalabilidad:** Preparado para crecer con más transportistas y envíos
- **Interoperabilidad:** Integración con APIs externas de transportistas
- **Seguridad:** Autenticación y autorización mediante JWT

---

## OBJETIVOS

### Objetivo General

Desarrollar una plataforma web robusta y escalable que centralice la gestión y monitoreo de envíos logísticos, mejorando la eficiencia operativa y proporcionando visibilidad en tiempo real a clientes y operadores.

### Objetivos Específicos

1. **Gestión de Actores Logísticos**
   - Permitir el registro y administración de clientes con información de contacto
   - Administrar transportistas con sus respectivos servicios

2. **Gestión de Envíos**
   - Crear envíos con identificadores únicos de rastreo
   - Asociar envíos con clientes y transportistas específicos
   - Definir orígenes y destinos geograficos
   - Rastrear el estado actual de cada envío

3. **Monitoreo en Tiempo Real**
   - Registrar eventos de seguimiento en diferentes etapas logísticas
   - Consultar el historial completo de eventos por envío
   - Mantener ubicación y descripción de cada evento

4. **Seguridad y Autenticación**
   - Implementar autenticación JWT para proteger endpoints críticos
   - Validar permisos de usuario antes de acceder a recursos

5. **Integración Externa**
   - Preparar endpoints simulados para integración con APIs de transportistas
   - Permitir consultas a sistemas externos de rastreo

---

## ALCANCE DEL PROYECTO

### Funcionalidades Incluidas

✅ **Gestión de Clientes**
- CRUD completo de clientes
- Campos: nombre, email, teléfono, empresa, fecha de registro

✅ **Gestión de Transportistas**
- CRUD de transportistas y proveedores de servicios
- Campos: nombre, tipo de servicio, país, endpoint API

✅ **Gestión de Envíos**
- Crear envíos con tracking automático
- Estados: Registrado, En Tránsito, Centro de Distribución, En Reparto, Entregado, Incidente
- Rastreo de origen y destino

✅ **Seguimiento de Eventos**
- Registro de eventos de rastreo por envío
- Estados, ubicaciones y descripciones
- Historial temporal completo

✅ **API REST**
- Endpoints para todas las operaciones CRUD
- Documentación interactiva (Swagger/ReDoc)
- Autenticación mediante JWT

✅ **Interfaz Frontend**
- Dashboard interactivo
- Vistas para cada módulo (clientes, transportistas, envíos, tracking)
- Consulta de rastreo en tiempo real

### Limitaciones y Restricciones

⚠️ **Base de Datos:** SQLite (adecuada para desarrollo, se recomienda PostgreSQL para producción)

⚠️ **Autenticación JWT:** Deshabilitada temporalmente en algunas rutas

⚠️ **Documentación Swagger:** Deshabilitada por compatibilidad con Python 3.14

⚠️ **Escalabilidad:** El sistema está optimizado para operaciones medianas; requiere optimización para millones de registros

### Fuera del Alcance

❌ Facturación y cobros financieros
❌ Integraciones reales con transportistas internacionales
❌ Sistema de notificaciones push por dispositivo móvil
❌ Sistema de chat en tiempo real
❌ Análisis de datos avanzados y machine learning

---

## TECNOLOGÍAS UTILIZADAS

### Backend

| Tecnología | Versión | Propósito |
|---|---|---|
| Python | 3.10+ | Lenguaje de programación |
| Django | 5.1.3 | Framework web |
| Django REST Framework | 3.15.2 | Arquitectura RESTful |
| Simple JWT | 5.3.1 | Autenticación por tokens JWT |
| DRF Spectacular | 0.27.2 | Generación de documentación OpenAPI |
| Gunicorn | - | Servidor WSGI para producción |

### Frontend

| Tecnología | Descripción |
|---|---|
| HTML5 | Estructura semántica de la interfaz |
| CSS3 | Estilos responsivos y diseño moderno |
| JavaScript Vanilla | Interactividad del cliente sin frameworks |
| Fetch API | Comunicación HTTP con el backend |

### Base de Datos

| Componente | Especificaciones |
|---|---|
| Motor | SQLite 3 |
| Ubicación | `backend/db.sqlite3` |
| ORM | Django ORM |
| Migración | Sistema de migraciones de Django |

### Herramientas y Utilitarias

| Herramienta | Uso |
|---|---|
| Django CORS Headers | Configuración de CORS para desarrollo |
| PyYAML | Procesamiento de configuraciones |
| Requests | Llamadas HTTP a APIs externas |
| Git | Control de versiones |

### Dependencias Completas

```
Django==5.1.3
djangorestframework==3.15.2
drf-spectacular==0.27.2
djangorestframework-simplejwt==5.3.1
requests==2.32.3
PyYAML==6.0.3
setuptools==82.0.1
django-cors-headers==4.4.0
```

---

## ARQUITECTURA DEL SISTEMA

### Patrón Arquitectónico: MVC + REST

El proyecto sigue el patrón **Modelo-Vista-Controlador** con arquitectura **REST**, donde:

- **Modelos (M):** Definición de entidades de datos
- **Serializadores:** Transformación entre modelos Django y JSON
- **Vistas (V):** ViewSets que manejan la lógica de negocio
- **Enrutamiento (C):** URLs que mapean a vistas específicas

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENTE (Frontend)                    │
│  HTML + CSS + JavaScript (Fetch API)                    │
│  Dashboard, Formularios, Reportes                       │
└────────────────┬────────────────────────────────────────┘
                 │
                 │ HTTP/REST
                 ↓
┌─────────────────────────────────────────────────────────┐
│              CAPA DE ENRUTAMIENTO (Django URLs)          │
│  /api/clientes/                                         │
│  /api/proveedores/                                      │
│  /api/envios/                                           │
│  /api/tracking/                                         │
│  /api/token/                                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────┐
│         CAPA DE VISTAS (ViewSets DRF)                   │
│  ClienteViewSet                                         │
│  TransportistaViewSet                                   │
│  EnvioViewSet                                           │
│  TrackingViewSet                                        │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────┐
│    CAPA DE SERIALIZADORES (Validación y Mapeo)          │
│  ClienteSerializer                                      │
│  TransportistaSerializer                                │
│  EnvioSerializer                                        │
│  TrackingEventoSerializer                               │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────┐
│         CAPA DE MODELOS (Django Models)                 │
│  CBA_Cliente                                            │
│  CBA_Transportista                                      │
│  CBA_Envio                                              │
│  CBA_TrackingEvento                                     │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────┐
│      BASE DE DATOS (SQLite)                             │
│  db.sqlite3                                             │
└─────────────────────────────────────────────────────────┘
```

### Flujo del Sistema

#### 1. Flujo de Registro de Envío

```
1. Cliente realiza solicitud POST /api/envios/
2. Frontend valida datos del formulario
3. Las credenciales se envían con JWT Token
4. Vista ClienteViewSet procesa y valida
5. Serializador EnvioSerializer normaliza datos
6. Modelo CBA_Envio se persiste en BD
7. Genera tracking_number único
8. Retorna JSON con ID y tracking
9. Frontend actualiza lista y muestra confirmación
```

#### 2. Flujo de Consulta de Rastreo

```
1. Usuario ingresa tracking number en frontend
2. Fetch API realiza GET /api/tracking/{tracking_number}/
3. TrackingViewSet consulta BD por tracking_number
4. Retorna los eventos asociados en JSON
5. JavaScript renderiza timeline de eventos
6. Actualiza estado actual y ubicación
7. Muestra histórico completo de movimientos
```

#### 3. Flujo de Autenticación

```
1. Usuario entra credenciales en login
2. POST /api/token/ con username y password
3. Simple JWT valida contra DB de usuarios
4. Retorna access_token y refresh_token
5. Frontend almacena token localmente
6. Token se incluye en header Authorization
7. Middleware valida token en cada solicitud
8. Autoriza acceso si token es válido
```

### Capas de Aplicación

El proyecto contiene 5 aplicaciones Django especializadas:

| Aplicación | Propósito | Modelos |
|---|---|---|
| **clientes** | Gestión de clientes | CBA_Cliente |
| **transportistas** | Manejo de transportistas | CBA_Transportista |
| **envios** | Registro y gestión de envíos | CBA_Envio |
| **tracking** | Seguimiento de eventos | CBA_TrackingEvento |
| **external_api** | Integración con APIs externas | - |

---

## DISEÑO DE BASE DE DATOS

### Diagrama Entidad-Relación

```
┌────────────────────┐         ┌─────────────────────┐
│   CBA_Cliente      │         │ CBA_Transportista   │
├────────────────────┤         ├─────────────────────┤
│ id (PK)           │         │ id (PK)            │
│ nombre            │         │ nombre             │
│ correo            │         │ tipo_servicio      │
│ telefono          │         │ pais               │
│ empresa           │         │ endpoint_api       │
│ fecha_registro    │         └─────────────────────┘
└────────────────────┘                  ↑
         ↑                              │
         │                              │
         │         1:N                  │ 1:N
         └─────────→┌──────────────────┴──┐
                    │   CBA_Envio         │
                    ├─────────────────────┤
                    │ id (PK)            │
                    │ tracking_number    │
                    │ cliente_id (FK)    │
                    │ transportista_id   │
                    │ (FK)               │
                    │ origen             │
                    │ destino            │
                    │ fecha_envio        │
                    │ estado_actual      │
                    └──────────┬──────────┘
                               │ 1:N
                               ↓
              ┌────────────────────────────┐
              │  CBA_TrackingEvento        │
              ├────────────────────────────┤
              │ id (PK)                   │
              │ tracking_number           │
              │ estado                    │
              │ ubicacion                 │
              │ fecha_evento              │
              │ descripcion               │
              └────────────────────────────┘
```

### Tablas y Campos

#### 1. Tabla: CBA_Cliente

| Campo | Tipo | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | NOT NULL | Nombre del cliente |
| correo | VARCHAR(254) | NOT NULL, UNIQUE | Email único |
| telefono | VARCHAR(20) | NOT NULL | Número de contacto |
| empresa | VARCHAR(100) | NOT NULL | Empresa del cliente |
| fecha_registro | DATETIME | NOT NULL, AUTO_NOW_ADD | Timestamp de creación |

**Índices:** UNIQUE en correo

**Propósito:** Almacenar información de clientes que crean envíos

---

#### 2. Tabla: CBA_Transportista

| Campo | Tipo | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | NOT NULL | Nombre transportista |
| tipo_servicio | VARCHAR(50) | NOT NULL | Tipo: Nacional, Internacional, Expreso |
| pais | VARCHAR(50) | NOT NULL | País de operación |
| endpoint_api | URL | NOT NULL | Endpoint para consultas externas |

**Propósito:** Registrar transportistas disponibles en el sistema

---

#### 3. Tabla: CBA_Envio

| Campo | Tipo | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| tracking_number | VARCHAR(50) | NOT NULL, UNIQUE | Código rastreo |
| cliente_id | INTEGER | NOT NULL, FOREIGN KEY | Referencia a CBA_Cliente |
| transportista_id | INTEGER | NOT NULL, FOREIGN KEY | Referencia a CBA_Transportista |
| origen | VARCHAR(100) | NOT NULL | Ciudad/ubicación origen |
| destino | VARCHAR(100) | NOT NULL | Ciudad/ubicación destino |
| fecha_envio | DATETIME | NOT NULL, AUTO_NOW_ADD | Timestamp envío |
| estado_actual | VARCHAR(20) | NOT NULL, DEFAULT='registrado' | Estado actual del envío |

**Estados Válidos:**
- `registrado` - Envío registrado en sistema
- `en_transito` - En camino a destino
- `centro_distribucion` - En centro de distribución
- `en_reparto` - Salió para reparto final
- `entregado` - Entregado al destinatario
- `incidente` - Problema durante entrega

**Índices:** UNIQUE en tracking_number

**Relaciones:**
- FK: cliente_id → CBA_Cliente.id (ON DELETE CASCADE)
- FK: transportista_id → CBA_Transportista.id (ON DELETE CASCADE)

---

#### 4. Tabla: CBA_TrackingEvento

| Campo | Tipo | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| tracking_number | VARCHAR(50) | NOT NULL | Número de seguimiento |
| estado | VARCHAR(20) | NOT NULL | Estado en este evento |
| ubicacion | VARCHAR(100) | NOT NULL | Ubicación geográfica |
| fecha_evento | DATETIME | NOT NULL, AUTO_NOW_ADD | Timestamp del evento |
| descripcion | TEXT | NOT NULL | Detalles del evento |

**Propósito:** Registrar historial de eventos para cada envío

**Índices:** se recomienda índice en tracking_number para consultas rápidas

---

### Relaciones Identificadas

| Relación | Tipo | Descripción |
|---|---|---|
| Cliente → Envíos | 1:N | Un cliente puede crear múltiples envíos |
| Transportista → Envíos | 1:N | Un transportista puede manejar múltiples envíos |
| Envío → Eventos Tracking | 1:N | Un envío puede tener múltiples eventos |

### Integridad de Datos

- **Integridad Referencial:** Cascada en borrado de clientes y transportistas
- **Unicidad:** tracking_number y correo de cliente
- **Validación de Estados:** Enum de estados predefinidos
- **Timestamps:** Auto-generados en INSERT

---

## ENDPOINTS DE LA API

### Base URL

```
http://localhost:8000
```

### Autenticación

```
Header: Authorization: Bearer <access_token>
```

Obtener token:
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password"}'
```

---

### 1. GESTIÓN DE CLIENTES

#### GET - Listar todos los clientes

```http
GET /api/clientes/ HTTP/1.1
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan@example.com",
    "telefono": "3001234567",
    "empresa": "Ejemplo S.A.",
    "fecha_registro": "2026-03-25T10:30:00Z"
  }
]
```

---

#### GET - Obtener cliente por ID

```http
GET /api/clientes/{id}/ HTTP/1.1
```

**Parámetros de URL:**
- `id`: INTEGER - ID del cliente

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@example.com",
  "telefono": "3001234567",
  "empresa": "Ejemplo S.A.",
  "fecha_registro": "2026-03-25T10:30:00Z"
}
```

---

#### POST - Crear nuevo cliente

```http
POST /api/clientes/ HTTP/1.1
Content-Type: application/json

{
  "nombre": "María García",
  "correo": "maria@example.com",
  "telefono": "3009876543",
  "empresa": "García Logística"
}
```

**Respuesta (201 Created):**
```json
{
  "id": 2,
  "nombre": "María García",
  "correo": "maria@example.com",
  "telefono": "3009876543",
  "empresa": "García Logística",
  "fecha_registro": "2026-03-25T11:45:00Z"
}
```

---

#### PUT - Actualizar cliente completo

```http
PUT /api/clientes/{id}/ HTTP/1.1
Content-Type: application/json

{
  "nombre": "María García López",
  "correo": "maria.garcia@example.com",
  "telefono": "3009876544",
  "empresa": "García Logística Mejorada"
}
```

**Parámetros de URL:**
- `id`: INTEGER - ID del cliente

**Respuesta (200 OK):**
```json
{
  "id": 2,
  "nombre": "María García López",
  "correo": "maria.garcia@example.com",
  "telefono": "3009876544",
  "empresa": "García Logística Mejorada",
  "fecha_registro": "2026-03-25T11:45:00Z"
}
```

---

#### PATCH - Actualizar cliente parcialmente

```http
PATCH /api/clientes/{id}/ HTTP/1.1
Content-Type: application/json

{
  "telefono": "3009876511"
}
```

**Respuesta (200 OK):**
```json
{
  "id": 2,
  "nombre": "María García López",
  "correo": "maria.garcia@example.com",
  "telefono": "3009876511",
  "empresa": "García Logística Mejorada",
  "fecha_registro": "2026-03-25T11:45:00Z"
}
```

---

#### DELETE - Eliminar cliente

```http
DELETE /api/clientes/{id}/ HTTP/1.1
```

**Parámetros de URL:**
- `id`: INTEGER - ID del cliente

**Respuesta (204 No Content):**
```
(Sin contenido)
```

---

### 2. GESTIÓN DE TRANSPORTISTAS

#### GET - Listar todos los transportistas

```http
GET /api/proveedores/ HTTP/1.1
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "nombre": "Fedex Colombia",
    "tipo_servicio": "Expreso",
    "pais": "Colombia",
    "endpoint_api": "https://api.fedex.com/tracking"
  }
]
```

---

#### POST - Crear transportista

```http
POST /api/proveedores/ HTTP/1.1
Content-Type: application/json

{
  "nombre": "DHL Express",
  "tipo_servicio": "Internacional",
  "pais": "Colombia",
  "endpoint_api": "https://api.dhl.com/tracking"
}
```

**Respuesta (201 Created):**
```json
{
  "id": 2,
  "nombre": "DHL Express",
  "tipo_servicio": "Internacional",
  "pais": "Colombia",
  "endpoint_api": "https://api.dhl.com/tracking"
}
```

---

#### PUT - Actualizar transportista

```http
PUT /api/proveedores/{id}/ HTTP/1.1
Content-Type: application/json

{
  "nombre": "DHL Express Updated",
  "tipo_servicio": "Nacional",
  "pais": "Colombia",
  "endpoint_api": "https://api.dhl.com/v2/tracking"
}
```

**Parámetros de URL:**
- `id`: INTEGER - ID del transportista

**Respuesta (200 OK):**
```json
{
  "id": 2,
  "nombre": "DHL Express Updated",
  "tipo_servicio": "Nacional",
  "pais": "Colombia",
  "endpoint_api": "https://api.dhl.com/v2/tracking"
}
```

---

#### DELETE - Eliminar transportista

```http
DELETE /api/proveedores/{id}/ HTTP/1.1
```

**Parámetros de URL:**
- `id`: INTEGER - ID del transportista

**Respuesta (204 No Content):**
```
(Sin contenido)
```

---

### 3. GESTIÓN DE ENVÍOS

#### GET - Listar todos los envíos

```http
GET /api/envios/ HTTP/1.1
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "tracking_number": "TRACK123456789",
    "cliente": 1,
    "transportista": 1,
    "origen": "Bogotá",
    "destino": "Medellín",
    "fecha_envio": "2026-03-25T10:00:00Z",
    "estado_actual": "en_transito"
  }
]
```

---

#### GET - Obtener envío por ID

```http
GET /api/envios/{id}/ HTTP/1.1
```

**Parámetros de URL:**
- `id`: INTEGER - ID del envío

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "tracking_number": "TRACK123456789",
  "cliente": 1,
  "transportista": 1,
  "origen": "Bogotá",
  "destino": "Medellín",
  "fecha_envio": "2026-03-25T10:00:00Z",
  "estado_actual": "en_transito"
}
```

---

#### POST - Crear envío

```http
POST /api/envios/ HTTP/1.1
Content-Type: application/json

{
  "tracking_number": "TRACK987654321",
  "cliente": 1,
  "transportista": 1,
  "origen": "Cali",
  "destino": "Barranquilla",
  "estado_actual": "registrado"
}
```

**Respuesta (201 Created):**
```json
{
  "id": 2,
  "tracking_number": "TRACK987654321",
  "cliente": 1,
  "transportista": 1,
  "origen": "Cali",
  "destino": "Barranquilla",
  "fecha_envio": "2026-03-25T11:20:00Z",
  "estado_actual": "registrado"
}
```

---

#### PUT - Actualizar envío

```http
PUT /api/envios/{id}/ HTTP/1.1
Content-Type: application/json

{
  "tracking_number": "TRACK987654321",
  "cliente": 1,
  "transportista": 2,
  "origen": "Cali",
  "destino": "Barranquilla",
  "estado_actual": "en_transito"
}
```

**Parámetros de URL:**
- `id`: INTEGER - ID del envío

**Respuesta (200 OK):**
```json
{
  "id": 2,
  "tracking_number": "TRACK987654321",
  "cliente": 1,
  "transportista": 2,
  "origen": "Cali",
  "destino": "Barranquilla",
  "fecha_envio": "2026-03-25T11:20:00Z",
  "estado_actual": "en_transito"
}
```

---

#### DELETE - Eliminar envío

```http
DELETE /api/envios/{id}/ HTTP/1.1
```

**Parámetros de URL:**
- `id`: INTEGER - ID del envío

**Respuesta (204 No Content):**
```
(Sin contenido)
```

---

### 4. CONSULTAAS DE RASTREO/TRACKING

#### GET - Obtener eventos de rastreo por tracking_number

```http
GET /api/tracking/{tracking_number}/ HTTP/1.1
```

**Parámetros de URL:**
- `tracking_number`: STRING - Número de rastreo

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "tracking_number": "TRACK123456789",
    "estado": "registrado",
    "ubicacion": "Almacén Bogotá",
    "fecha_evento": "2026-03-25T10:00:00Z",
    "descripcion": "Paquete registrado en sistema"
  },
  {
    "id": 2,
    "tracking_number": "TRACK123456789",
    "estado": "en_transito",
    "ubicacion": "Centro Distribución Facatativá",
    "fecha_evento": "2026-03-25T14:30:00Z",
    "descripcion": "Paquete en tránsito hacia destino"
  },
  {
    "id": 3,
    "tracking_number": "TRACK123456789",
    "estado": "en_reparto",
    "ubicacion": "Centro Medellín",
    "fecha_evento": "2026-03-25T19:00:00Z",
    "descripcion": "Paquete en reparto local"
  }
]
```

---

#### GET - Listar todos los eventos de rastreo

```http
GET /api/tracking/ HTTP/1.1
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "tracking_number": "TRACK123456789",
    "estado": "registrado",
    "ubicacion": "Almacén Bogotá",
    "fecha_evento": "2026-03-25T10:00:00Z",
    "descripcion": "Paquete registrado en sistema"
  },
  {
    "id": 2,
    "tracking_number": "TRACK987654321",
    "estado": "en_transito",
    "ubicacion": "Cali - Centro",
    "fecha_evento": "2026-03-25T12:45:00Z",
    "descripcion": "Paquete despachado desde Cali"
  }
]
```

---

#### POST - Crear evento de rastreo

```http
POST /api/tracking/ HTTP/1.1
Content-Type: application/json

{
  "tracking_number": "TRACK123456789",
  "estado": "entregado",
  "ubicacion": "Domicilio Cliente Medellín",
  "descripcion": "Paquete entregado exitosamente"
}
```

**Respuesta (201 Created):**
```json
{
  "id": 4,
  "tracking_number": "TRACK123456789",
  "estado": "entregado",
  "ubicacion": "Domicilio Cliente Medellín",
  "fecha_evento": "2026-03-25T20:15:00Z",
  "descripcion": "Paquete entregado exitosamente"
}
```

---

### 5. AUTENTICACIÓN JWT

#### POST - Obtener Token JWT

```http
POST /api/token/ HTTP/1.1
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Respuesta (200 OK):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

#### POST - Refrescar Token JWT

```http
POST /api/token/refresh/ HTTP/1.1
Content-Type: application/json

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Respuesta (200 OK):**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 6. API EXTERNA SIMULADA

#### GET - Consultar tracking en API extterna simulada

```http
GET /external-api/tracking/{tracking_number}/ HTTP/1.1
```

**Parámetros de URL:**
- `tracking_number`: STRING - Número de rastreo

**Respuesta (200 OK):**
```json
{
  "tracking_number": "TRACK123456789",
  "estado": "entregado",
  "ubicacion_actual": "Medellín, Colombia",
  "proveedor": "Fedex Colombia",
  "fecha_ultima_actualizacion": "2026-03-25T20:15:00Z"
}
```

---

### 7. DOCUMENTACIÓN DE API

#### GET - Esquema OpenAPI 3.0

```http
GET /api/schema/ HTTP/1.1
```

**Descripción:** Retorna el esquema completo OpenAPI 3.0 en formato JSON

---

#### GET - Swagger UI

```http
GET /api/schema/swagger-ui/ HTTP/1.1
```

**Descripción:** Interfaz interactiva Swagger para explorar y probar la API

---

#### GET - ReDoc

```http
GET /api/schema/redoc/ HTTP/1.1
```

**Descripción:** Documentación interactiva ReDoc para la API

---

### Códigos de Respuesta HTTP

| Código | Significado | Descripción |
|---|---|---|
| 200 | OK | Solicitud exitosa |
| 201 | Created | Recurso creado exitosamente |
| 204 | No Content | Recurso eliminado exitosamente |
| 400 | Bad Request | Datos inválidos en solicitud |
| 401 | Unauthorized | Autenticación requerida |
| 403 | Forbidden | Acceso denegado |
| 404 | Not Found | Recurso no encontrado |
| 500 | Server Error | Error interno del servidor |

---

## INSTALACIÓN DEL PROYECTO

### Requisitos Previos

- Python 3.10 o superior
- Git
- pip (administrador de paquetes Python)
- Navegador web moderno

### Paso 1: Clonar el Repositorio

```bash
# Navegar a la carpeta deseada
cd C:\Users\samue\Documents\archivos_adso__3trimestre\apis\proyecto_1

# Clonar o descargar el proyecto
# Si usa Git:
git clone <url-repositorio>
cd logistica_tracking
```

### Paso 2: Crear Entorno Virtual

```bash
# En Windows PowerShell
python -m venv venv

# Activar entorno virtual
venv\Scripts\Activate.ps1
```

Si obtiene error de ejecución, ejecute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Paso 3: Instalar Dependencias

```bash
# Asegúrese de estar en el directorio raíz del proyecto
cd backend

# Instalar todas las dependencias
pip install -r requirements.txt
```

Verifique la instalación:
```bash
pip list
```

### Paso 4: Aplicar Migraciones de Base de Datos

```bash
# En el directorio `backend/`
python manage.py migrate
```

Se crearán las tablas automáticamente:
- auth_user
- auth_group
- CBA_Cliente
- CBA_Transportista
- CBA_Envio
- CBA_TrackingEvento

### Paso 5: Crear Usuario Administrador (Opcional)

```bash
python manage.py createsuperuser
```

Siga las indicaciones para crear un usuario admin.

### Paso 6: Ejecutar el Servidor de Desarrollo

```bash
# En el directorio backend/
python manage.py runserver
```

Debería ver:
```
Django version 5.1.3
System check identified no issues (0 silenced).
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Paso 7: Acceder a la Aplicación

**Backend:**
```
http://127.0.0.1:8000/admin
```

**Frontend:**
```
Abrir: frontend/index.html en navegador
```

**Documentación API:**
```
http://127.0.0.1:8000/api/schema/swagger-ui/
http://127.0.0.1:8000/api/schema/redoc/
```

### Paso 8: Verificación Rápida

1. Acceda a `http://127.0.0.1:8000/api/clientes/`
2. Debería ver `[]` (lista vacía) en JSON
3. Las CORS están configuradas correctamente
4. El servidor está funcionando

### Solución de Problemas

| Problema | Solución |
|---|---|
| ModuleNotFoundError | Ejecute `pip install -r requirements.txt` de nuevo |
| Puerto 8000 en uso | `python manage.py runserver 8080` |
| Error de migraciones | Elimine `db.sqlite3` y ejecute `migrate` nuevamente |
| CORS bloqueados | Verifique CORS_ALLOWED_ORIGINS en settings.py |

---

## ESTRUCTURA DEL PROYECTO

### Árbol de Directorios

```
logistica_tracking/
│
├── README.md                          # Documentación inicial
├── DOCUMENTACION_TECNICA.md           # Este archivo - Documentación completa
│
├── backend/                           # 🔧 Aplicación Django
│   ├── manage.py                      # Script de gestión Django
│   ├── db.sqlite3                     # Base de datos SQLite
│   ├── requirements.txt               # Dependencias Python
│   │
│   ├── config/                        # ⚙️ Configuración principal
│   │   ├── __init__.py
│   │   ├── settings.py                # Configuración Django
│   │   ├── urls.py                    # Enrutamiento principal
│   │   ├── asgi.py                    # Configuración ASGI
│   │   ├── wsgi.py                    # Configuración WSGI
│   │   └── __pycache__/
│   │
│   ├── clientes/                      # 👥 App: Gestión de Clientes
│   │   ├── models.py                  # Modelo CBA_Cliente
│   │   ├── serializers.py             # ClienteSerializer
│   │   ├── views.py                   # ClienteViewSet
│   │   ├── urls.py                    # Rutas de clientes
│   │   ├── admin.py                   # Admin Django
│   │   ├── apps.py                    # Configuración app
│   │   ├── tests.py                   # Tests unitarios
│   │   ├── __init__.py
│   │   ├── migrations/                # Historial migraciones
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   │   └── __pycache__/
│   │   └── __pycache__/
│   │
│   ├── transportistas/                # 🚚 App: Gestión Transportistas
│   │   ├── models.py                  # Modelo CBA_Transportista
│   │   ├── serializers.py             # TransportistaSerializer
│   │   ├── views.py                   # TransportistaViewSet
│   │   ├── urls.py                    # Rutas transportistas
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── __pycache__/
│   │
│   ├── envios/                        # 📦 App: Gestión Envíos
│   │   ├── models.py                  # Modelo CBA_Envio
│   │   ├── serializers.py             # EnvioSerializer
│   │   ├── views.py                   # EnvioViewSet
│   │   ├── urls.py                    # Rutas envíos
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── __pycache__/
│   │
│   ├── tracking/                      # 📍 App: Seguimiento eventos
│   │   ├── models.py                  # Modelo CBA_TrackingEvento
│   │   ├── serializers.py             # TrackingEventoSerializer
│   │   ├── views.py                   # TrackingEventoViewSet
│   │   ├── urls.py                    # Rutas tracking
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── __pycache__/
│   │
│   ├── external_api/                  # 🔗 App: Integración APIs externas
│   │   ├── models.py
│   │   ├── views.py                   # Vistas para API externa
│   │   ├── urls.py                    # Rutas API externa
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── __pycache__/
│   │
│
├── frontend/                          # 🎨 Interfaz de Usuario
│   ├── index.html                     # Página principal/dashboard
│   ├── clientes.html                  # Gestión de clientes
│   ├── transportistas.html            # Gestión transportistas
│   ├── envios.html                    # Registro de envíos
│   ├── tracking.html                  # Consulta de rastreo
│   │
│   ├── css/                           # 🎨 Estilos
│   │   └── style.css                  # Estilos principales
│   │
│   ├── js/                            # ⚡ Scripts JavaScript
│   │   ├── api.js                     # Funciones API (Fetch)
│   │   ├── clientes.js                # Lógica gestión clientes
│   │   ├── transportistas.js          # Lógica gestión transportistas
│   │   ├── envios.js                  # Lógica registro envíos
│   │   ├── tracking.js                # Lógica consulta tracking
│   │   └── dashboard.js               # Lógica dashboard principal
│
└── .gitignore                         # Archivos ignorados en Git
```

### Descripción de Carpetas Clave

**`config/`** — Centro de configuración de Django
- `settings.py`: Variables globales, apps instaladas, BD, seguridad
- `urls.py`: Mapeo de todas las rutas principales
- `wsgi.py` / `asgi.py`: Servidores web

**`clientes/`** — Módulo de gestión de clientes completo
- CRUD autónomo de clientes
- Accesible vía `/api/clientes/`

**`transportistas/`** — Módulo de proveedores logísticos
- CRUD de transportistas
- Accesible vía `/api/proveedores/`

**`envios/`** — Core del sistema de envíos
- Creación y seguimiento de envíos
- Estados de envío
- Accesible vía `/api/envios/`

**`tracking/`** — Registro de eventos de rastreo
- Historial de movimientos por envío
- Accesible vía `/api/tracking/`

**`frontend/`** — Interfaz visual
- HTML semántico
- CSS responsivo
- JavaScript para interactividad

---

## CONCLUSIÓN

### Logros Alcanzados

La **Plataforma de Monitoreo de Envíos Logísticos** representa una solución integral que:

✅ **Simplifica Operaciones:** Centraliza la gestión de múltiples actores logísticos (clientes, transportistas, envíos)

✅ **Proporciona Transparencia:** Permite a clientes y operadores seguir envíos en tiempo real

✅ **Escalable y Mantenible:** Arquitectura modular basada en Django permite agregar nuevas funcionalidades fácilmente

✅ **API-First:** Posibilita integración con plataformas externas y aplicaciones móviles futuras

✅ **Segura:** Implementa autenticación JWT para proteger datos sensibles

✅ **Documentada:** Incluye documentación completa de API y arquitectura

### Beneficios Clave

| Beneficio | Valor |
|---|---|
| **Eficiencia** | Reducción de tiempo en gestión manual de envíos |
| **Visibilidad** | Seguimiento de paquetes desde origen a destino |
| **Confiabilidad** | Base de datos estructurada con integridad referencial |
| **Escalabilidad** | Preparada para crecer con la organización |
| **Extensibilidad** | APIs bien documentadas para integraciones futuras |

### Recomendaciones Futuras

#### Corto Plazo (1-2 meses)

1. **Habilitar JWT completamente** en todos los endpoints protegidos
2. **Implementar validaciones avanzadas** en modelos (campos de entrada)
3. **Agregar pruebas automatizadas** (unit tests y integration tests)
4. **Optimizar consultas** con índices de base de datos
5. **Mejorar frontend** con framework (React, Vue.js o Angular)

#### Mediano Plazo (3-6 meses)

1. **Migrar a PostgreSQL** para mejor rendimiento en producción
2. **Implementar caché** con Redis
3. **Agregar notificaciones en tiempo real** via WebSockets
4. **Crear aplicación móvil** con React Native o Flutter
5. **Implementar reportes analíticos** con gráficos avanzados

#### Largo Plazo (6-12 meses)

1. **Machine Learning** para predicción de entregas
2. **Integraciones reales** con APIs de transportistas principales
3. **Blockchain** para garantía de entregas
4. **IoT** con sensores de temperatura/humedad
5. **Inteligencia artificial** para optimización de rutas

### Consideraciones de Seguridad

⚠️ **Para Producción:**
- [ ] Cambiar SECRET_KEY en settings.py
- [ ] Establecer DEBUG = False
- [ ] Configurar ALLOWED_HOSTS con dominio real
- [ ] Usar HTTPS (SSL/TLS)
- [ ] Configurar política CORS restrictiva
- [ ] Implementar rate limiting
- [ ] Agregar logging y monitoreo
- [ ] Realizar auditoría de seguridad

### Soporte y Contacto

Para preguntas, reportar bugs o sugerencias:

- **Email:** samuel@example.com
- **Documentación:** READMEs en cada carpeta
- **API Docs:** `/api/schema/swagger-ui/`

---

## APÉNDICE A: Glosario de Términos

| Término | Definición |
|---|---|
| **API** | Interfaz de Programación de Aplicaciones |
| **CRUD** | Create, Read, Update, Delete |
| **Django** | Framework web Python |
| **DRF** | Django REST Framework |
| **Endpoint** | Ruta accesible en la API |
| **GET** | Método HTTP para obtener datos |
| **JWT** | JSON Web Token - autenticación basada en tokens |
| **Middleware** | Software que procesa solicitudes HTTP |
| **Modelo** | Representación de datos en BD |
| **POST** | Método HTTP para enviar datos |
| **PUT** | Método HTTP para actualizar recursos completos |
| **PATCH** | Método HTTP para actualizar recursos parcialmente |
| **DELETE** | Método HTTP para eliminar recursos |
| **Serializer** | Convierte modelos Django a JSON |
| **ViewSet** | Combina múltiples vistas en una clase |
| **REST** | Representational State Transfer |
| **Webhook** | Callback HTTP para eventos remotos |

---

## APÉNDICE B: Comandos Útiles

### Gestión de Proyecto

```bash
# Crear nueva aplicación Django
python manage.py startapp nombre_app

# Chequear errores del proyecto
python manage.py check

# Ver migraciones
python manage.py showmigrations

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de fixture
python manage.py loaddata fixture.json

# Generar dump de datos
python manage.py dumpdata > backup.json

# Shell interactivo Django
python manage.py shell
```

### Migraciones

```bash
# Crear migración
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Deshacer última migración
python manage.py migrate app_name 0002
```

### Servidor

```bash
# Ejecutar servidor estándar
python manage.py runserver

# Ejecutar en puerto diferente
python manage.py runserver 0.0.0.0:8080

# Servidor en Gunicorn (producción)
gunicorn config.wsgi:application
```

### Testing

```bash
# Ejecutar todos los tests
python manage.py test

# Tests de aplicación específica
python manage.py test clientes

# Tests con verbosidad
python manage.py test --verbosity=2
```

---

**Documento Generado Automáticamente por Sistema de Documentación**
**Última Actualización:** 25 de Marzo de 2026
**Versión del Documento:** 1.0.0

---
