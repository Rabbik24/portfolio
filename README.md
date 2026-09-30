# Mohamed Rabbik M - Software Developer & Data Analytics Portfolio

A production-ready portfolio website and interactive analytics application built for **Mohamed Rabbik M** based on his technical resume (`MD_RABBIK_RESUME.pdf`).

This application is built with a **Python Flask backend** and modular **Jinja2 / HTML5 / CSS3 / JavaScript** frontend. It is designed for zero-config local execution and immediate one-click deployment to **GitHub Pages** or **Vercel**.

---

## 🛠️ Tech Stack & Architecture

- **Backend / Web Server**: Python 3.11+, Flask 3.0+
- **Frontend & Styling**: Vanilla HTML5, CSS3 (Custom Design Tokens, Glassmorphism, Dark/Light Themes), JavaScript (ES6+)
- **Templating**: Jinja2 (`templates/base.html`, `templates/index.html`)
- **Static Exporter**: `freeze.py` (Builds static site to `build/` directory)
- **Serverless Hosting**: `vercel.json` (WSGI configuration for Vercel Python runtime)
- **CI/CD Automation**: `.github/workflows/deploy.yml` (Automated build & deploy to GitHub Pages)

---

## 📁 Repository Structure

```
Portfolio/
├── app.py                   # Main Flask backend application & REST API routes
├── freeze.py                # Python static site generator exporter (outputs to build/)
├── vercel.json              # Vercel deployment configuration
├── requirements.txt         # Dependencies (Flask, Flask-Freeze, gunicorn)
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions CI/CD to deploy static build to GitHub Pages
├── templates/
│   ├── base.html            # Shared base template (head, navbar, resume modal, footer)
│   └── index.html           # Main portfolio view with Jinja2 context rendering
├── static/
│   ├── css/
│   │   └── styles.css       # Full responsive CSS stylesheet & dark/light theme tokens
│   └── js/
│       └── script.js        # Interactivity, typing effect, modals, & AJAX API calls
└── README.md                # Deployment and setup documentation
```

---

## 🚀 Running Locally

### Option A: Python Flask Server (Recommended)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Open in browser**:
   Navigate to `http://127.0.0.1:5000` to interact with the full dynamic app, including REST API endpoints (`/api/contact`, `/api/verify-doc`, `/api/match-resume`).

---

### Option B: Standalone Static Build

You can also run the exporter script to compile the site into a static folder (`build/`):

```bash
python freeze.py
```

Then open `build/index.html` or `index.html` directly in any web browser without needing any server setup.

---

## 🌐 Deploying to GitHub Pages

This repository includes a pre-configured **GitHub Actions workflow** (`.github/workflows/deploy.yml`).

### Steps to Deploy:

1. **Initialize Git & Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Deploy Mohamed Rabbik Portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/portfolio`
   - Navigate to **Settings** → **Pages**.
   - Under **Build and deployment** → **Source**, select **GitHub Actions**.

3. **Automatic Build & Publish**:
   - Every time you push to `main`, GitHub Actions will automatically execute `python freeze.py` and publish your portfolio live to `https://YOUR_USERNAME.github.io/portfolio/`.

---

## ⚡ Deploying to Vercel

This repository is ready for serverless Python deployment on Vercel using `vercel.json`.

### Option 1: Via Vercel Dashboard (Easiest)

1. Push your code to GitHub.
2. Log in to [Vercel](https://vercel.com/) and click **New Project**.
3. Import your GitHub repository.
4. Click **Deploy**. Vercel will automatically detect `app.py` and `vercel.json` and deploy your Flask app live within seconds.

### Option 2: Via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy directly from your workspace directory
vercel
```

---

## ✨ Resume Content Summary

- **Name**: Mohamed Rabbik M
- **Title**: Software Developer | Data Analytics
- **Contact**: `developer.rabbik@gmail.com` | `+91 7695959281` | Chennai, TN, India
- **Experience**: Technical Consultant at *Vista Tech* & Full Stack Developer Intern at *Qriocity Ventures*
- **Projects**:
  1. *AI-Driven Medical Fundraising Verification System* (YOLOv8, PaddleOCR, Flask, MySQL, JWT, Bcrypt)
  2. *Resume Screening Using NLP* (Python, spaCy, TF-IDF, Streamlit)
- **Education**: MCA (CGPA 8.2/10, Anna University) & BCA (CGPA 8.1/10, Annamalai University)
- **Certifications**: Diploma in Python (*CSN Infotech*), Data Science for Beginners (*NASSCOM Foundation*), Front-end Development (*TechSaksham*)
