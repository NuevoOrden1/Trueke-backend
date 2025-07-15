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

### 1. Gestión de usuarios

- **Registro**: `POST /api/usuarios`
- **Login**: `POST /api/usuarios/login`
- **Obtener perfil**: `GET /api/usuarios/:id`
- Campos del usuario: nombre, apellido, correo, celular, contraseña, fotoPerfil

### 2. Publicación de productos

- **Publicar producto**: `POST /api/objetos` (multipart/form-data)
- **Listar productos**: `GET /api/objetos`
- **Modificar producto**: `PUT /api/objetos/:id`
- **Eliminar producto**: `DELETE /api/objetos/:id`

### 3. Moderación de productos

- **Ver pendientes**: `GET /api/moderacion/pendientes`
- **Aprobar producto**: `PUT /api/moderacion/aprobar/:id`
- **Rechazar producto**: `PUT /api/moderacion/rechazar/:id` con `{ motivo }`
- Al aprobar o rechazar, se notifica al usuario correspondiente automáticamente.

### 4. Solicitudes de intercambio

- **Enviar solicitud**: `POST /api/solicitudes` con:
  ```json
  {
    "solicitante": ID_usuario,
    "receptor": ID_usuario,
    "objetoSolicitado": ID_objeto,
    "objetoPropuesto": ID_objeto
  }
  ```
- **Ver solicitudes del usuario**: `GET /api/solicitudes?usuarioId=ID`
  - Devuelve solicitudes enviadas y recibidas
- **Actualizar estado**: `PUT /api/solicitudes/:id` con `{ "estado": "aceptado" | "rechazado" }`
- Al aceptar o rechazar, se notifica automáticamente al solicitante.

### 5. Notificaciones

- **Ver notificaciones**: `GET /api/notificaciones/:idUsuario`
- **Marcar como leída**: `PUT /api/notificaciones/:id/leida`
- Tipos: `"solicitud"`, `"estado"`, `"moderacion"`

### 6. Calificaciones

- **Crear calificación**: `POST /api/calificaciones` con:
  ```json
  {
    "usuarioPuntuador": ID,
    "usuarioPuntuado": ID,
    "valor": int (1–5),
    "comentario": "texto"
  }
  ```
- **Editar calificación**: `PUT /api/calificaciones/:id`
- **Ver calificaciones de usuario**: `GET /api/calificaciones/usuario/:id`
- Se actualiza automáticamente la `calificacionPromedio` y `cantIntercambios` del usuario puntuado.

### 7. Intercambios completados

- **Ver historial**: `GET /api/solicitudes/intercambios-completados?usuarioId=ID`
- Lista todas las solicitudes aceptadas donde el usuario fue solicitante o receptor.

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

El archivo `.gitignore` no tiene que contener lo siguiente:

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


