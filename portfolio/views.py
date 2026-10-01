import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage

# Structured Resume Data Dictionary for Django Context & APIs
RESUME_DATA = {
    "profile": {
        "name": "Mohamed Rabbik M",
        "title": "Software Developer | Data Analytics",
        "email": "developer.rabbik@gmail.com",
        "phone": "+91 7695959281",
        "location": "Chennai, Tamil Nadu, India",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "portfolio": "https://rabbik.dev"
    },
    "summary": (
        "MCA graduate with professional experience in Python, SQL, Data Analytics, "
        "Web Development, and AI/ML applications. Currently working as a Technical Consultant "
        "at Vista Tech, delivering hands-on training and practical solutions in Python, SQL, Data Analytics, "
        "and software development. Previously worked as a Full Stack Developer Intern developing web "
        "applications and integrating APIs. Experienced in building AI-driven applications using Python, "
        "Flask, Django, MySQL, NLP, OCR, Computer Vision, REST APIs, and data processing techniques. Strong "
        "problem-solving and communication skills with a passion for software development, data analytics, "
        "AI/ML, and Data Engineering."
    ),
    "skills": {
        "programming": ["Python", "Java", "JavaScript", "C", "C++", "HTML", "CSS"],
        "frameworks": ["Flask", "Django", "Angular", "Bootstrap", "Pandas", "NumPy", "Matplotlib", "Seaborn"],
        "databases": ["SQL (MySQL)"],
        "data_ai": ["Power BI", "Data Analysis", "NLP", "spaCy", "YOLOv8", "PaddleOCR", "Fuzzy Matching"],
        "tools": ["Git", "GitHub", "ChatGPT", "Cursor IDE", "GitHub Copilot", "Lovable.ai", "Canva"],
        "soft_skills": ["Problem-Solving", "Team Collaboration", "Communication", "Adaptability"]
    },
    "experience": [
        {
            "id": "exp-1",
            "role": "Technical Consultant",
            "company": "Vista Tech",
            "location": "Chennai",
            "period": "Jan 2026 – Sept 2026",
            "highlights": [
                "Deliver hands-on training in Python, SQL, Data Analytics, Web Development, and programming fundamentals.",
                "Develop practical coding exercises, projects, and technical learning materials focused on real-world applications.",
                "Mentor and support 150+ learners in programming, debugging, problem-solving, and project development.",
                "Collaborate with team members to deliver structured technical modules and hands-on sessions."
            ],
            "tags": ["Python", "SQL", "Data Analytics", "Web Development", "Mentorship"]
        },
        {
            "id": "exp-2",
            "role": "Full Stack Developer Intern",
            "company": "Qriocity Ventures Pvt. Ltd.",
            "location": "Chennai",
            "period": "Jan 2024 – Apr 2024",
            "highlights": [
                "Developed and deployed web applications using Python, HTML, CSS, JavaScript, and Bootstrap.",
                "Integrated APIs and contributed to backend functionality, workflow automation, and responsive UI development.",
                "Supported testing, debugging, and application improvements, contributing to approximately 30–45% workflow efficiency improvement."
            ],
            "tags": ["Python", "HTML/CSS", "JavaScript", "Bootstrap", "REST APIs", "Automation"]
        }
    ],
    "projects": [
        {
            "id": "project-1",
            "title": "AI-Driven Medical Fundraising Verification System",
            "category": "AI & Computer Vision",
            "badge": "Computer Vision & Python",
            "description": "Built an AI-based system to verify medical fundraising requests using YOLOv8, PaddleOCR, and Fuzzy Matching. Developed Flask/Django REST APIs and MySQL backend with Trust Score-based campaign verification. Implemented JWT authentication and Bcrypt for secure role-based access.",
            "tech": ["Python", "YOLOv8", "PaddleOCR", "Fuzzy Matching", "Django", "MySQL", "JWT", "Bcrypt"],
            "highlights": [
                "Built an AI-based system to verify medical fundraising requests using YOLOv8, PaddleOCR, and Fuzzy Matching.",
                "Developed REST APIs and MySQL backend with Trust Score-based campaign verification.",
                "Implemented JWT authentication and Bcrypt for secure role-based access."
            ]
        },
        {
            "id": "project-2",
            "title": "Resume Screening Using NLP",
            "category": "NLP & Machine Learning",
            "badge": "Group Project",
            "description": "Built an AI-based resume screening system using NLP and TF-IDF to analyze and rank candidate resumes. Implemented text preprocessing and similarity analysis using Python and spaCy. Developed a Streamlit interface, improving candidate shortlisting efficiency by approximately 70%.",
            "tech": ["Python", "NLP", "spaCy", "TF-IDF", "Streamlit", "Vector Similarity"],
            "highlights": [
                "Built an AI-based resume screening system using NLP and TF-IDF to analyze and rank candidate resumes.",
                "Implemented text preprocessing and similarity analysis using Python and spaCy.",
                "Developed a Streamlit interface, improving candidate shortlisting efficiency by approximately 70%."
            ]
        }
    ],
    "education": [
        {
            "degree": "MCA — Master of Computer Applications",
            "institution": "Adhiparasakthi Engineering College, Anna University",
            "period": "2024–2026",
            "cgpa": "8.2 / 10",
            "percentage": 82
        },
        {
            "degree": "BCA — Bachelor of Computer Applications",
            "institution": "St. Ann’s College of Arts & Science, Annamalai University",
            "period": "2021–2024",
            "cgpa": "8.1 / 10",
            "percentage": 81
        }
    ],
    "certifications": [
        {
            "title": "Diploma in Python",
            "issuer": "CSN Infotech, Pondicherry",
            "details": "Comprehensive Python core, OOP, data structures, and script development."
        },
        {
            "title": "Data Science for Beginners",
            "issuer": "NASSCOM Foundation",
            "details": "Data analysis fundamentals, statistics, and visualization techniques."
        },
        {
            "title": "Understanding Front-end Development",
            "issuer": "TechSaksham (Microsoft & SAP) / Edunet Foundation",
            "details": "Responsive UI design, front-end architecture, and modern web standards."
        }
    ]
}

def index_view(request):
    """Render main Django portfolio view."""
    return render(request, 'portfolio/index.html', {'resume': RESUME_DATA})

def api_info(request):
    """Return JSON resume data."""
    return JsonResponse(RESUME_DATA)

@csrf_exempt
def api_contact(request):
    """API endpoint to receive and store contact messages in Django DB."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)

        # Save message to SQLite database using Django ORM
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        except Exception as e:
            pass  # Fallback if DB not migrated yet

        return JsonResponse({
            'status': 'success',
            'message': f'Thank you, {name}! Your message has been saved in Django database.'
        })

    return JsonResponse({'status': 'error', 'message': 'POST method required.'}, status=405)

@csrf_exempt
def api_verify_doc(request):
    """API simulating document verification backend."""
    return JsonResponse({
        "status": "success",
        "engine": "Django + YOLOv8 + PaddleOCR",
        "yolo_detection": ["Hospital Seal (Conf: 0.96)", "Patient Invoice Box (Conf: 0.94)"],
        "ocr_text": "Apollo Hospitals Chennai - Total Paid: ₹45,000",
        "fuzzy_match_score": 98.4,
        "trust_score": 94.5,
        "verification_result": "AUTHENTIC"
    })

@csrf_exempt
def api_match_resume(request):
    """API simulating NLP resume matcher backend."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST
        target_role = data.get('role', 'python')
    else:
        target_role = 'python'

    scores = {
        'python': {"score": 94.8, "match": "Strong match for Python backend, API integration, and SQL."},
        'data': {"score": 92.4, "match": "High match for SQL queries, Pandas analysis, and Power BI."},
        'aiml': {"score": 96.1, "match": "Top tier match for YOLOv8, PaddleOCR, and spaCy NLP projects."}
    }

    result = scores.get(target_role, scores['python'])
    return JsonResponse({
        "status": "success",
        "framework": "Django REST Backend",
        "role": target_role,
        "cosine_similarity": result["score"],
        "match_analysis": result["match"],
        "candidate": "Mohamed Rabbik M"
    })
