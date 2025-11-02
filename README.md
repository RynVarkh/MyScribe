# MyScribe

MyScribe is a simple and elegant Django web application designed for **writing and managing blogs**. It allows users to create, edit, and view blog posts in a clean interface.

---

## Features

- Create, edit, and delete blog posts
- List all blog posts
- View individual blog posts
- Simple and clean UI for writing
- Built with Django 5.x

---

## Tech StackUsage

On the home page, select whether you want to:

Generate a password

View saved passwords

If generating:

Enter the application/service name

Select password options (length, character types)

Click Generate Password

Copy or save the password using the buttons provided.

View all saved passwords under the password list section.

- **Backend:** Django
- **Frontend:** Django Templates, HTML, CSS
- **Database:** SQLite (default, can be changed)
- **Python Version:** 3.10+
- **Dependency Management:** Poetry

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/RynVarkh/MyScribe.git
cd MyScribe
```

2. **Install Poetry (if not already installed)**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. **Install dependencies**
```bash
poetry install
```

4. **Apply migrations**
```bash
poetry run python manage.py migrate
```

## **Run Development server**
```bash
python manage.py runserver
```

## **Run Production server with Gunicorn**
```bash
poetry run gunicorn MyScribe.wsgi:application --bind 0.0.0.0:8000
```
