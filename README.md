# Modular Entity and Mapping API

A modular Django REST Framework backend for managing **Vendors, Products, Courses, Certifications** and their mappings — built using `APIView` only, with Swagger documentation via `drf-yasg`.

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- drf-yasg (Swagger & ReDoc)

---

## Project Structure
```
modular_api/
├── vendor/
├── product/
├── course/
├── certification/
├── vendor_product_mapping/
├── product_course_mapping/
└── course_certification_mapping/
```

Each app contains its own `models.py`, `serializers.py`, `views.py`, `urls.py`, and `admin.py`.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/18Ishika/AI_certs.git
cd AI_certs/modular_api
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv env

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

API base URL: `http://127.0.0.1:8000/`

---

## API Documentation

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/swagger/` | Swagger UI |
| `http://127.0.0.1:8000/redoc/` | ReDoc UI |

---

List APIs support query-parameter-based filtering:
```
GET /api/products/?name=Azure
```

---

## Validations

- Required fields enforced on all models
- `code` field is unique per entity
- Duplicate mappings are prevented
- Only **one** `primary_mapping=True` allowed per parent entity

---

## Soft Delete

Records are not permanently deleted. Instead, `is_active` is set to `False`. Inactive records are excluded from all list queries.

---

## API Testing

All endpoints have been tested using **Postman**.

### Screenshots

> Check out the screenshots folder.


---

## Notes
- All views use `APIView` only — no ViewSets, GenericAPIView, mixins, or routers.
