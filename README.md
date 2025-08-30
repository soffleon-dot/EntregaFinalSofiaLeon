# EntregaFinal+Leon

Proyecto web hecho con **Django** siguiendo el patrón **MVT**. Es mi entrega final del curso de Python en Coderhouse.

---

Objetivo

Armar una app sencilla que permita:

- Registrar usuarios (username y email únicos) con reglas básicas de contraseña.
- Iniciar sesión, cerrar sesión y editar el perfil.
- Cambiar la contraseña de la cuenta.
- Cargar **álbumes musicales** con: nombre del álbum, **artista**, **género**, **año** y **portada** (imagen).
- Ver el **listado** con buscador.
- Ver el **detalle** de cada álbum.
- **Editar** o **borrar** álbumes (CRUD completo).
- Usar **herencia de templates** y una barra de navegación.
- Páginas de **Inicio** y **Acerca de mí**.

---

Tecnologías

- Python 3
- Django 4
- SQLite3 (base de datos por defecto)
- HTML + CSS (templates con herencia)
- Git & GitHub

---

Instalación y ejecución

1) **Clonar el repo** (o descomprimir el .zip y entrar a la carpeta)
```bash
git clone https://github.com/usuario/SofiaLeonEntregaFinal.git
cd SofiaLeonEntregaFinal
```

2) **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv env
# Mac/Linux
source env/bin/activate
# Windows
.\env\Scripts\activate
```

3) **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4) **Base de datos y migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5) **Levantar el servidor**
```bash
python manage.py runserver
```

👉 Abrir en el navegador: `http://127.0.0.1:8000/`

---

Funcionalidades

- **Home** con acceso al catálogo.
- **Acerca de mí** (bio corta de Sofía León).
- **Catálogo de álbumes** con buscador.
- **Detalle de álbum**.
- **CRUD**: crear, editar y eliminar álbumes (con subida de imagen).
- **Autenticación**:
  - Registro (username + email únicos) y password con 8+ caracteres, al menos una letra y un número.
  - Login y logout.
  - **Perfil** editable (nombre, apellido, email).
  - **Cambio de contraseña**.
- **Mensajes y validaciones**.
- **Herencia de templates** (`base.html` + `nav.html`).

---

Estructura del proyecto (resumen)

SofiaLeonEntregaFinal/
├── albums/                 # Modelo Album y vistas (CBV: List/Detail/Create/Update/Delete + LoginRequiredMixin)
├── accounts/               # Registro, login/logout, perfil y cambio de contraseña (decorador @login_required en perfil)
├── entrega/                # Configuración del proyecto (settings, urls, wsgi, asgi)
├── templates/              # base.html, nav.html, home, about + templates de apps
├── static/                 # CSS simple del sitio
├── media/                  # Portadas subidas por usuarios (IGNORADA en git)
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md

---

Notas

- **No subir** `db.sqlite3` ni la carpeta `media/` al repositorio (están en `.gitignore`).  
  También se ignoran `env/` y `__pycache__/`.
- Se usan **mínimo 2 CBVs** y un **mixin** (`LoginRequiredMixin`) para proteger crear/editar/borrar.
- Se usa **un decorador** `@login_required` en la vista de perfil.

---


