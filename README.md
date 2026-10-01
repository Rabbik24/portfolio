# Mohamed Rabbik M - Software Developer & Data Analytics Portfolio (Django Edition)

A production-ready portfolio website and interactive analytics application built for **Mohamed Rabbik M** based on his technical resume (`MD_RABBIK_RESUME.pdf`).

This application is built with a **Python Django 5+ backend** (with SQLite database ORM, Django Admin, REST APIs) and modular **Django Templates / HTML5 / CSS3 / JavaScript** frontend.

---

## 🛠️ Tech Stack & Architecture

- **Backend / Web Framework**: Python 3.11+, Django 5.0+
- **Database / ORM**: SQLite (`db.sqlite3`), Django Admin (`/admin/`), `ContactMessage` model
- **Frontend & Styling**: Vanilla HTML5, CSS3 (Custom Design Tokens, Glassmorphism, Dark/Light Themes), JavaScript (ES6+)
- **Templating Engine**: Django Template Language (`portfolio/templates/portfolio/`)
- **Static Exporter**: `freeze.py` (Freezes Django views into static `build/` directory)
- **Serverless Hosting**: `vercel.json` (WSGI configuration for Vercel Python runtime)
- **CI/CD Automation**: `.github/workflows/deploy.yml` (Automated build & deploy to GitHub Pages)

---

## 📁 Repository Structure

```
Portfolio/
├── manage.py                          # Django management CLI script
├── db.sqlite3                         # Django SQLite database
├── requirements.txt                   # Dependencies (Django 5+, gunicorn)
├── vercel.json                        # Vercel deployment configuration
├── freeze.py                          # Django static site exporter script (outputs to build/)
├── portfolio_project/                 # Django Settings & WSGI configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                         # Main Django App
│   ├── admin.py                       # Admin interface registration for ContactMessage
│   ├── models.py                      # ContactMessage model definition
│   ├── views.py                       # Core views & REST API endpoints
│   ├── urls.py                        # App route patterns
│   └── templates/
│       └── portfolio/
│           ├── base.html              # Django base template
│           └── index.html             # Django template with template tags & context
├── static/
│   ├── css/
│   │   └── styles.css                 # Responsive design system
│   └── js/
│       └── script.js                  # Interactivity, typing effect, & API calls
└── README.md                          # Documentation
```

---

## 🚀 Running Locally with Django

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Apply Django Database Migrations
```bash
python manage.py migrate
```

### Step 3: Start the Django Development Server
```bash
python manage.py runserver
```

### Step 4: Open in Browser
Navigate to **`http://127.0.0.1:8000`** in your browser.

---

## 🔒 Optional: Create Django Superuser (Admin Access)

To access the Django Admin panel at `http://127.0.0.1:8000/admin/` and view messages sent via the contact form:

```bash
python manage.py createsuperuser
```

---

## 🌐 Deployment Instructions

### Deploying to GitHub Pages
```bash
git add .
git commit -m "Converted portfolio to Django 5"
git push
```
The automated GitHub Actions workflow will run `python freeze.py` and update your live site at `https://rabbik24.github.io/portfolio/`.

### Deploying to Vercel
Vercel automatically detects `portfolio_project/wsgi.py` and `vercel.json` for serverless Django hosting. Simply push to GitHub or run `vercel` in terminal.
