# Truek-e Backend

Este repositorio contiene el backend del sistema de intercambio de productos **Truek-e**, construido con **Django** y **Django REST Framework**. Provee endpoints para el registro de usuarios, publicación de productos y demás funcionalidades de la plataforma.


## Requisitos previos

- Python 3.10 o superior
- PostgreSQL
- Git
- pip (gestor de paquetes de Python)


## Instalación y ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/trueke_backend
cd trueke_backend
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
  "password": "clave123"
}
```

#### Listar usuarios

- **GET** `/api/usuarios/`

### Objetos / Productos

#### Crear objeto

- **POST** `/api/objetos/`
- **Body (form-data):**
  - `titulo`
  - `descripcion`
  - `categoria`
  - `imagen` (tipo archivo)
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


