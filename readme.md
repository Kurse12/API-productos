# Productos API

API REST para manejar productos, construida con **Flask** y **PostgreSQL**. Permite realizar operaciones CRUD: crear, leer, actualizar y eliminar productos.  

---

## 🛠 Tecnologías

- Python 3.x  
- Flask  
- psycopg2 (PostgreSQL driver)  
- PostgreSQL

---

## ⚡ Funcionalidades

- Listar todos los productos (`GET /products`)  
- Obtener un producto por ID (`GET /products/<id>`)  
- Crear un nuevo producto (`POST /products`)  
- Actualizar un producto (`PATCH /products/<id>`)  
- Eliminar un producto (`DELETE /products/<id>`)  

---

## 📦 Estructura de la tabla `products`

```sql
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    descripcion TEXT DEFAULT '',
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀Instalación


- Clonar el repositorio:

```
git clone https://github.com/Kurse12/API-productos.git
cd API-PRODUCTOS
```

- Crear un entorno virtual e instalar dependencias:

```cmd

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```


- Crear archivo .env con variables de conexión a la base de datos:

```
DB_HOST=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_PORT=5432
DB_SSLMODE=require

```


- Correr la API:

```py
python app.py
```

- Por defecto corre en http://localhost:5000

---

## 📬 Endpoints
### GET /products

Devuelve todos los productos.
```
Request:

GET http://localhost:5000/products


Response:

[
  {
    "id": 1,
    "nombre": "Proteína Whey",
    "precio": 15000,
    "descripcion": "Suplemento de proteína",
    "stock": 30
  },
]
```
### GET /products/<id>

Devuelve un producto específico por ID.
```
Request:

GET http://localhost:5000/products/1


Response 404 si no existe:

{
  "Error": "Producto no encontrado"
}
```
### POST /products

Crea un nuevo producto.
```
Body (JSON):

{
  "nombre": "Creatina",
  "precio": 8000,
  "descripcion": "Suplemento de fuerza",
  "stock": 50
}

Response: Producto creado con su id.

{
  "id": 2,
  "nombre": "Creatina",
  "precio": 8000,
  "descripcion": "Suplemento de fuerza",
  "stock": 50
}
```
### PATCH /products/<id>

Actualiza campos de un producto.

Solo los campos presentes en el body se actualizan.
```
{
  "precio": 8500,
  "stock": 40
}


Response: Producto actualizado.

{
  "id": 2,
  "nombre": "Creatina",
  "precio": 8500,
  "descripcion": "Suplemento de fuerza",
  "stock": 40
}
```
### DELETE /products/<id>

Elimina un producto por ID.
```
DELETE http://localhost:5000/products/2

Response: Producto eliminado.

{
  "Mensaje": "Producto eliminado",
  "producto": {
    "id": 2,
    "nombre": "Creatina",
    "precio": 8500,
    "descripcion": "Suplemento de fuerza",
    "stock": 40
  }
}


Response 404 si no existe:

{
  "error": "Producto no encontrado"
}
---
