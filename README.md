# API Tienda Supabase

## Descripción del Proyecto

Este proyecto consiste en una API REST desarrollada con FastAPI y conectada a una base de datos PostgreSQL administrada mediante Supabase.

La aplicación permite gestionar el proceso de liquidación de productos de una tienda, administrando categorías, subcategorías y productos, aplicando automáticamente porcentajes de ganancia según la categoría seleccionada.

Arquitectura implementada:

Usuario → Frontend Web → API REST (FastAPI) → Supabase PostgreSQL

---

## Problemática

Las tiendas pequeñas suelen realizar la liquidación de precios manualmente, lo que genera errores en los cálculos, inconsistencias en los precios de venta y dificultades para administrar el inventario.

Este sistema automatiza el cálculo de precios y centraliza la información de productos.

---

## Objetivos

### Objetivo General

Desarrollar una API REST para gestionar categorías, subcategorías y productos utilizando FastAPI y Supabase.

### Objetivos Específicos

* Registrar categorías de productos.
* Registrar subcategorías.
* Registrar productos.
* Calcular automáticamente el precio de venta.
* Consultar información almacenada.
* Actualizar registros.
* Eliminar registros.
* Documentar los servicios mediante Swagger.

---

## Tecnologías Utilizadas

* Python 3.13
* FastAPI
* Supabase
* PostgreSQL
* Pydantic
* Uvicorn
* Git
* GitHub
* Visual Studio Code

---

## Estructura del Proyecto

```text
api_tienda/
│
├── app/
│   ├── config/
│   │   └── database.py
│   │
│   ├── routers/
│   │   ├── categorias.py
│   │   ├── subcategorias.py
│   │   └── productos.py
│   │
│   ├── schemas/
│   │   ├── categoria.py
│   │   ├── subcategoria.py
│   │   └── producto.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Funcionalidades

### Categorías

* Crear categoría
* Consultar categorías
* Actualizar categoría
* Eliminar categoría

### Subcategorías

* Crear subcategoría
* Consultar subcategorías
* Actualizar subcategoría
* Eliminar subcategoría

### Productos

* Crear producto
* Consultar productos
* Actualizar producto
* Eliminar producto
* Liquidación automática de precios

---

## Configuración del Entorno

### 1. Clonar repositorio

```bash
git clone https://github.com/kathydiazcorrea2019-rgb/api-tienda-supabase.git
```

### 2. Entrar al proyecto

```bash
cd api-tienda-supabase
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de Entorno

Crear un archivo .env con la siguiente información:

```env
SUPABASE_URL=TU_URL_SUPABASE
SUPABASE_KEY=TU_API_KEY
```

---

## Ejecución del Proyecto

```bash
uvicorn app.main:app --reload
```

Servidor local:

```text
http://127.0.0.1:8000
```

---

## Documentación Swagger

FastAPI genera automáticamente la documentación interactiva.

Acceder en:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints Principales

### Categorías

GET /categorias

POST /categorias

PUT /categorias/{id}

DELETE /categorias/{id}

### Subcategorías

GET /subcategorias

POST /subcategorias

PUT /subcategorias/{id}

DELETE /subcategorias/{id}

### Productos

GET /productos

POST /productos

PUT /productos/{id}

DELETE /productos/{id}

---

## Autor

Kathy Julieth Diaz Correa

Estudiante de Ingeniería de Sistemas

Corporación Universitaria Americana

2026
