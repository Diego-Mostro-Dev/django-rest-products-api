# Django REST Products API

Production-ready REST API built with Django and Django REST Framework.

This project demonstrates a backend architecture with authentication, permissions, filtering, and automated tests. It is designed as a portfolio project to showcase backend development skills.

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

Body

{
"name": "Laptop",
"price": 1000
}

---

## Running the Project Locally

Clone the repository

git clone https://github.com/yourusername/django-rest-products-api  
cd django-rest-products-api

Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Create `.env` file

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

Example `.env` file

DATABASE_URL=your_database_url_here  
SECRET_KEY=your_secret_key  
DEBUG=True

---

## Project Structure

project

│  
├── apiP  
│ ├── models.py  
│ ├── serializers.py  
│ ├── views.py  
│ ├── permissions.py  
│ ├── filters.py  
│ ├── services.py  
│ └── tests.py

│  
├── config  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py

│  
└── manage.py

---

## Author

Backend developer focused on building REST APIs with Django.

GitHub:  
https://github.com/yourusername
