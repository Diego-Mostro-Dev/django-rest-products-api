# Django REST Products API

Production-ready REST API built with Django and Django REST Framework.

Este proyecto demuestra una arquitectura de backend con autenticación, permisos, filtrado y tests automatizados. Diseñado como proyecto de portfolio para mostrar habilidades de desarrollo backend.

---

## Features

- JWT Authentication
- User registration
- Product CRUD
- Object-level permissions (users only manage their own products)
- Filtering
- Search
- Ordering
- Pagination
- PostgreSQL database
- Automated API tests

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL (Neon)
- JWT Authentication (SimpleJWT)
- Django Filters

---

## API Endpoints

GET /api/health-check/

### Authentication

POST /api/users/  
POST /api/token/

### Products

GET /api/products/  
POST /api/products/  
PUT /api/products/{id}/  
DELETE /api/products/{id}/

Available features on the products endpoint:

- Filtering by price
- Search by name
- Ordering by name or price
- Pagination

---

## Example Request

Create product

POST /api/products/

Body:

{
"name": "Laptop",
"price": 1000
}

---

## Running the Project Locally

Clone the repository

git clone https://github.com/Diego-Mostro-Dev/django-rest-products-api
cd django-rest-products-api

Create virtual environment

python -m venv venv

Activate environment

Windows:
venv\Scripts\activate

Linux / Mac:
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Create `.env` file:

DATABASE_URL=your_database_url  
SECRET_KEY=your_secret_key  
DEBUG=True

Run migrations

python manage.py migrate

Run server

python manage.py runserver

---

## Running Tests

python manage.py test

The project includes automated tests using Django REST Framework test client.

Tests cover:

- authentication
- product CRUD
- filtering
- permissions
- user data isolation

---

## Environment Variables

Example `.env` file:

DATABASE_URL=your_database_url_here  
SECRET_KEY=your_secret_key  
DEBUG=True

---

## Project Structure

project

│  
├── apiP  
│ ├── admin.py  
│ ├── apps.py  
│ ├── models.py  
│ ├── serializers.py  
│ ├── views.py  
│ ├── urls.py  
│ ├── tests.py  
│ ├── filters  
│ │ └── product_filters.py  
│ │
│ ├── permissions  
│ │ └── product_permissions.py  
│ │  
│ ├── services  
│ │ └── product_service.py  
│  
│  
├── config  
│ ├── settings.py  
│ ├── urls.py  
│ ├── wsgi.py  
│ └── asgi.py  
│
│  
├── staticfiles  
├── venv  
├── .env  
├── .env.example  
├── .gitignore  
├── db.sqlite3  
├── manage.py  
└── requirements.txt

---

## Live API

Base URL:

https://django-rest-products-api.onrender.com/

Interactive API documentation (Swagger):

https://django-rest-products-api.onrender.com/api/docs/

Alternative documentation (ReDoc):

https://django-rest-products-api.onrender.com/api/redoc/

Health check:

https://django-rest-products-api.onrender.com/health-check/

---

## Demo Users

You can use these users to test the API.

Regular user

username: demo  
password: demo1234

Regular user2

username: demo2  
password: demo1234

Admin user

username: admin_demo  
password: admin_demo1234

---

## Author

Diego A. Salvado - Desarrollador Full Stack

Tengo más de 3 años de experiencia en React, JavaScript, Python y Django, orientado al desarrollo de aplicaciones web completas desde la interfaz hasta la lógica backend.Trabajo en proyectos freelance reales, participando en todo el ciclo de desarrollo: análisis de requerimientos, diseño de arquitectura, implementación frontend y backend, integración con APIs, optimización de performance y despliegue en producción. Me destaco por la autonomía, la comunicación con clientes y la capacidad de transformar necesidades funcionales en soluciones técnicas claras y escalables.

Portfolio: https://diegosalvadodev.com.ar/  
LinkedIn: https://www.linkedin.com/in/diegosalvadodev/
GitHub: https://github.com/Diego-Mostro-Dev

Tech stack: Python, Django, Django REST Framework, PostgreSQL, JWT, Docker, Git
