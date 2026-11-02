# Django Company and Product Management

A web application built with Django to manage companies and display their associated products.

## Features

- View a list of companies with their logos.
- View individual company details.
- Display products associated with each company.
- Add new companies through a web form.
- Manage company and product data using Django models and the admin panel.
- Display company and product images.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Git and GitHub

## Project Structure

```text
companydetails/
├── companydetails/
├── companyinformation/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── Templates/
├── media/
├── manage.py
└── README.md
```

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MAfreen3502/django-company-product-management.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-company-product-management
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv env
   ```

   Windows PowerShell:

   ```powershell
   .\env\Scripts\Activate.ps1
   ```

4. Install Django and the image-handling dependency:

   ```bash
   pip install django pillow
   ```

5. Configure the `DJANGO_SECRET_KEY` environment variable before running Django.

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open `http://127.0.0.1:8000/` in your browser.

## Learning Outcomes

This project provided practical experience with Django models, database relationships, class-based views, templates, image uploads, and Git version control.
