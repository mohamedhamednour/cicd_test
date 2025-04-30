# Django CI/CD Pipeline 🚀

This project demonstrates a basic **CI/CD pipeline** setup for a Django project using **GitHub Actions**.

---

## ✅ Features

- **CI/CD with GitHub Actions**
- **PostgreSQL** service for testing
- Automatic:
  - Code checkout
  - Python environment setup
  - Dependency installation
  - Django migrations
  - Test execution
  - Deployment step (dummy for now)

---

## 🛠️ GitHub Actions Workflow

File: `.github/workflows/django.yml`

### Triggers:
- On push to `main` branch
- On pull requests

### Jobs:

#### `test`:
- Runs on `ubuntu-latest`
- Sets up PostgreSQL service
- Installs requirements
- Runs migrations and tests with `pytest`

#### `deploy`:
- Runs only if tests succeed on `main` branch
- Placeholder for deployment logic

---

## 🔧 Environment Variables

These are required in the GitHub Actions environment:

| Variable             | Value            |
|----------------------|------------------|
| POSTGRES_DB          | cicd             |
| POSTGRES_USER        | postgres         |
| POSTGRES_PASSWORD    | password         |
| POSTGRES_HOST        | localhost        |
| POSTGRES_PORT        | 5432             |
| DJANGO_SETTINGS_MODULE | shopping.settings |

---

## 🚀 How to Run Locally

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
pytest
