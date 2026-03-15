# AI_certs
# Modular Vendor Product API

## Project Overview

This project implements a modular REST API using Django and Django REST Framework.
It manages Vendors, Products, Certifications, Courses and their mappings.

The API supports CRUD operations, soft delete, filtering, pagination and Swagger documentation.

## Tech Stack

* Python
* Django
* Django REST Framework
* drf-yasg (Swagger documentation)

## Setup Instructions

### 1. Clone Repository

git clone <repo-link>

### 2. Create Virtual Environment

python -m venv env

### 3. Activate Environment

env\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Run Migrations

python manage.py migrate

### 6. Start Server

python manage.py runserver

API will run at:
http://127.0.0.1:8000/

Swagger Documentation:
http://127.0.0.1:8000/swagger/

## API Features

* Vendor CRUD APIs
* Soft delete (inactive records hidden)
* Filtering using query parameters
* Pagination support
* Swagger API documentation

## Example Endpoints

GET /api/vendors/
POST /api/vendors/
GET /api/vendors/{id}/
PUT /api/vendors/{id}/
PATCH /api/vendors/{id}/
DELETE /api/vendors/{id}/

## Soft Delete

Instead of deleting records permanently, the API sets:
is_active = False

Inactive records are excluded from queries.


## Advanced Filtering 

