# Truek-e

Truek-e es una plataforma de intercambio de objetos donde los usuarios pueden publicar productos, enviar y recibir solicitudes de intercambio, calificar a otros usuarios y ser notificados sobre el estado de los intercambios. Además, incluye un sistema de moderación para revisar productos antes de ser publicados.

## Tecnologías utilizadas

- **Backend**: Django + Django REST Framework
- **Base de datos**: PostgreSQL
- **Frontend**: React (en desarrollo)
- **Autenticación**: Manual (correo y contraseña)
- **Almacenamiento de imágenes**: Local (`MEDIA_ROOT`)

## Estructura del backend

- `usuarios/`: Registro, login y perfil de usuario
- `productos/`: Publicación y gestión de objetos
- `solicitudes/`: Envío y recepción de solicitudes de intercambio
- `notificaciones/`: Visualización y gestión de notificaciones
- `moderacion/`: Revisión y aprobación/rechazo de objetos por moderadores
- `calificaciones/`: Calificación entre usuarios luego de un intercambio

## Endpoints principales (resumen)

### Usuarios
| Acción | Método | Endpoint | Body (JSON) | Respuesta esperada |
|--------|--------|----------|-------------|---------------------|
| Registro | POST | `/api/usuarios` | `{nombre, apellido, correo, celular, contraseña}` | `{mensaje}` |
| Login | POST | `/api/usuarios/login` | `{correo, contraseña}` | `{mensaje, usuario}` |
| Obtener por ID | GET | `/api/usuarios/:id` | — | `{usuario}` |

### Objetos
| Acción | Método | Endpoint | Body (JSON) | Respuesta esperada |
|--------|--------|----------|-------------|---------------------|
| Listar / Crear | GET / POST | `/api/objetos` | — / `{...}` | Lista / Objeto creado |
| Ver / Editar / Eliminar | GET / PUT / DELETE | `/api/objetos/:id` | `{...}` | Detalles / Mensaje |

### Intercambios (Solicitudes)
| Acción | Método | Endpoint | Body (JSON) | Respuesta esperada |
|--------|--------|----------|-------------|---------------------|
| Enviar solicitud | POST | `/api/solicitudes` | `{solicitanteId, receptorId, objetoSolicitadoId, objetoPropuestoId}` | `{mensaje, id}` |
| Ver solicitudes propias | GET | `/api/solicitudes?usuarioId=…` | — | Lista |
| Cambiar estado | PUT | `/api/solicitudes/:id` | `{estado}` | `{mensaje}` |
| Ver Intercambios Completados | GET | `/api/solicitudes/completados/:id` | - | - |

### Notificaciones
| Acción | Método | Endpoint | Body | Respuesta esperada |
|--------|--------|----------|------|---------------------|
| Ver notificaciones | GET | `/api/notificaciones/:idUsuario` | — | Lista |
| Marcar como leída | PUT | `/api/notificaciones/:id/leida` | — | `{mensaje}` |

### Moderación
| Acción | Método | Endpoint | Body | Respuesta esperada |
|--------|--------|----------|------|---------------------|
| Ver objetos pendientes | GET | `/api/moderacion/pendientes` | — | Lista |
| Aprobar objeto | PUT | `/api/moderacion/aprobar/:id` | — | `{mensaje}` |
| Rechazar objeto | PUT | `/api/moderacion/rechazar/:id` | `{motivo}` | `{mensaje}` |

### Calificaciones
| Acción | Método | Endpoint | Body | Respuesta esperada |
|--------|--------|----------|------|---------------------|
| Crear calificación | POST | `/api/calificaciones` | `{puntuadorId, puntuadoId, valor, comentario}` | `{mensaje}` |
| Ver calificaciones usuario | GET | `/api/calificaciones/:idUsuario` | — | Lista |
| Editar calificación | PUT | `/api/calificaciones/:id` | `{valor, comentario}` | `{mensaje}` |

## Cómo ejecutar el proyecto localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/trueke-backend.git
cd trueke-backend
```

### 2. Crea y activa un entorno virtual (venv)

```bash
python -m venv venv
source venv/Scripts/activate   # En Windows
# o
source venv/bin/activate       # En Linux/macOS
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura la base de datos PostgreSQL

Asegúrate de tener una base de datos creada, por ejemplo `db_trueke`. Luego, en `settings.py`, configura:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_trueke',
        'USER': 'tu_usuario_postgres',
        'PASSWORD': 'tu_contrasena_postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Aplica las migraciones

```bash
python manage.py makemigrations usuarios productos
python manage.py migrate
```

### 6. Ejecuta el servidor

```bash
python manage.py runserver
```

Accede en tu navegador a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Estructura del proyecto

```
trueke_backend/
├── usuarios/             # App para gestión de usuarios
├── productos/            # App para gestión de objetos/productos
├── solicitudes/          # App para gestión de solicitudes
├── moderacion/           # App para gestión del moderador
├── calificaciones/       # App para gestión de calificaciones de usuario
├── trueke_backend/       # Configuración principal del proyecto
├── media/                # Carpeta para almacenamiento de imágenes
├── manage.py             # Script principal de Django
└── requirements.txt      # Dependencias del proyecto
```

## Pruebas con Postman

### Usuarios

#### Registrar usuario

- **POST** `/api/usuarios/`
- **Body (form-data o raw JSON):**

```json
{
  "nombre": "Juan",
  "apellido": "Pérez",
  "correo": "juan@example.com",
  "celular": "123456789",
  "contraseña": "clave123"
}
```

#### Listar usuarios

- **GET** `/api/usuarios/`

### Objetos / Productos

#### Crear objeto

- **POST** `/api/objetos/`
- **Body (form-data):**
  - `nombre`
  - `descripcion`
  - `categoria`
  - `imagenes` (tipo archivo)
  - `usuario` (ID del usuario)

#### Listar objetos

- **GET** `/api/objetos/`

#### Obtener un objeto específico

- **GET** `/api/objetos/<id>/`

#### Editar un objeto

- **PUT** `/api/objetos/<id>/`
- **Body:** (form-data o JSON)

#### Eliminar un objeto

- **DELETE** `/api/objetos/<id>/`


## No subir al repositorio

Asegúrate de que el archivo `.gitignore` contenga lo siguiente:

```
venv/
__pycache__/
*.pyc
*.sqlite3
media/
.env
```

## Notas importantes

- El campo `id` de los modelos se genera automáticamente por Django.
- El `AUTH_USER_MODEL` ha sido configurado para usar nuestro modelo personalizado de usuario.
- La autenticación aún no ha sido implementada (ni login ni tokens).
- El almacenamiento de imágenes funciona correctamente con la configuración de `MEDIA_URL` y `MEDIA_ROOT`.


