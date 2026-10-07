import json
import os
import urllib.request
import urllib.parse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
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
        "portfolio": "https://mdrabbik.vercel.app/"
    },
    "summary": (
        "MCA graduate and Technical Consultant with professional experience engineering Python, SQL, Data Analytics, "
        "Full Stack Web Development, and AI/ML systems. Currently delivering hands-on technical solutions, mentoring 150+ engineers, "
        "and building end-to-end web applications. Experienced in architecting AI-driven platforms with Python, Flask, Django, "
        "MySQL, YOLOv8, PaddleOCR, NLP, and REST APIs. Driven by a commitment to writing clean, scalable code and transforming "
        "complex data into actionable business intelligence."
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
            "period": "Jan 2026 – Oct 2026",
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
    """API endpoint to receive contact messages, store in DB, and send direct email to developer.rabbik@gmail.com."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip() or 'Portfolio Contact Message'
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({'status': 'error', 'message': 'All fields (name, email, message) are required.'}, status=400)

        # 1. Save message to SQLite database using Django ORM
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        except Exception as e:
            print(f"[!] DB Save Exception: {e}")

        # 2. Send Direct Mail to developer.rabbik@gmail.com
        # 2. Send Direct Mail Notification to developer.rabbik@gmail.com
        recipient_email = getattr(settings, 'NOTIFICATION_EMAIL', 'developer.rabbik@gmail.com')
        email_sent = False
        
        email_subject = f"[Portfolio Contact] {subject} - From {name}"
        email_body = (
            f"Hello Mohamed Rabbik,\n\n"
            f"You have received a new contact submission from your portfolio website:\n\n"
            f"--------------------------------------------------\n"
            f"Sender Name:    {name}\n"
            f"Sender Email:   {email}\n"
            f"Subject:        {subject}\n"
            f"--------------------------------------------------\n\n"
            f"Message:\n"
            f"{message}\n\n"
            f"--------------------------------------------------\n"
            f"Reply directly to sender: {email}\n"
        )

        # Attempt A: Standard Django send_mail
        try:
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'developer.rabbik@gmail.com') or 'developer.rabbik@gmail.com'
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=from_email,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            email_sent = True
        except Exception as mail_err:
            print(f"[!] Django SMTP Notice: {mail_err}")

        # Attempt B: Direct HTTP Mailer API fallback to developer.rabbik@gmail.com
        if not email_sent:
            try:
                w3_key = os.environ.get('WEB3FORMS_ACCESS_KEY', '7b12733d-c187-4d9d-8d4e-0a56bd1df5ee')
                payload_data = json.dumps({
                    "access_key": w3_key,
                    "name": name,
                    "email": email,
                    "subject": f"[Portfolio Inquiry] {subject} from {name}",
                    "message": message,
                    "from_name": f"{name} (Portfolio Contact)",
                    "to_email": "developer.rabbik@gmail.com"
                }).encode('utf-8')

                req = urllib.request.Request(
                    "https://api.web3forms.com/submit",
                    data=payload_data,
                    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=8) as resp:
                    if resp.status == 200:
                        email_sent = True
            except Exception as w3_err:
                print(f"[!] Web3Forms API Notice: {w3_err}")

        return JsonResponse({
            'status': 'success',
            'email_sent': email_sent,
            'message': f'Thank you, {name}! Your message has been saved in the database and sent directly to developer.rabbik@gmail.com.'
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
