# Employee Project

A simple Employee CRUD application built with Django + Django REST Framework, with a responsive GUI.

## Features
- Create Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee
- Search Employee by Employee ID in GUI

## Tech Stack
- Python
- Django
- Django REST Framework
- MySQL

## Requirements
Install dependencies:

```bash
pip install -r requirements.txt
```



## Run Project
From project root:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## GUI
Open:
- http://127.0.0.1:8000/

## API Endpoints
- `POST /api/employees/` — Create employee
- `GET /api/employees/` — List employees
- `GET /api/employees/?employee_id=<value>` — Search by employee ID
- `GET /api/employees/<employee_id>/` — Get by ID
- `PUT /api/employees/<employee_id>/` — Full update
- `PATCH /api/employees/<employee_id>/` — Partial update
- `DELETE /api/employees/<employee_id>/` — Delete

## Employee Model Notes
- `employee_id` is user-provided and stored as string primary key.
- `email` must be valid and unique.
