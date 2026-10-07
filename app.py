"""
=============================================================================
Mohamed Rabbik M - Portfolio & Analytics Platform (Flask Web Application)
=============================================================================
"""

import os
from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'rabbik-portfolio-secret-key-2026'

# Complete Resume Data Dictionary for Templating and APIs
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
            "badge": "Computer Vision & Flask",
            "description": "Built an AI-based system to verify medical fundraising requests using YOLOv8, PaddleOCR, and Fuzzy Matching. Developed Flask REST APIs and MySQL backend with Trust Score-based campaign verification. Implemented JWT authentication and Bcrypt for secure role-based access.",
            "tech": ["Python", "YOLOv8", "PaddleOCR", "Fuzzy Matching", "Flask", "MySQL", "JWT", "Bcrypt"],
            "highlights": [
                "Built an AI-based system to verify medical fundraising requests using YOLOv8, PaddleOCR, and Fuzzy Matching.",
                "Developed Flask REST APIs and MySQL backend with Trust Score-based campaign verification.",
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

@app.route('/')
def home():
    """Render main portfolio home page."""
    return render_template('index.html', resume=RESUME_DATA)

@app.route('/api/info')
def get_info():
    """Return structured JSON resume data."""
    return jsonify(RESUME_DATA)

@app.route('/api/contact', methods=['POST'])
def contact_api():
    """API endpoint for contact form submission & direct email notification to developer.rabbik@gmail.com."""
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip() or 'Portfolio Contact Message'
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({"status": "error", "message": "All fields (name, email, message) are required."}), 400

    recipient = os.environ.get('NOTIFICATION_EMAIL', 'developer.rabbik@gmail.com')
    smtp_user = os.environ.get('EMAIL_HOST_USER') or os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('EMAIL_HOST_PASSWORD') or os.environ.get('SMTP_PASSWORD')
    smtp_server = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('EMAIL_PORT', 587))

    email_sent = False
    if smtp_user and smtp_pass:
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = recipient
            msg['Reply-To'] = email
            msg['Subject'] = f"[Portfolio Contact] {subject} - From {name}"

            body_content = (
                f"Hello Mohamed Rabbik,\n\n"
                f"You have received a new contact submission on your portfolio:\n\n"
                f"Sender Name:    {name}\n"
                f"Sender Email:   {email}\n"
                f"Subject:        {subject}\n\n"
                f"Message:\n{message}\n\n"
                f"--------------------------------------------------\n"
                f"Reply directly to sender: {email}\n"
            )
            msg.attach(MIMEText(body_content, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            server.quit()
            email_sent = True
        except Exception as e:
            print(f"[!] SMTP Error in Flask app: {e}")

    return jsonify({
        "status": "success",
        "email_sent": email_sent,
        "message": f"Thank you, {name}! Your message and details have been sent directly to developer.rabbik@gmail.com."
    })


@app.route('/api/verify-doc', methods=['POST'])
def verify_doc_api():
    """Simulates AI Document Verification API backend (YOLOv8 + PaddleOCR + Fuzzy Match)."""
    data = request.get_json() or {}
    doc_type = data.get('doc_type', 'hospital_bill')

    return jsonify({
        "status": "success",
        "document": doc_type,
        "yolo_detection": ["Hospital Seal (Conf: 0.96)", "Patient Invoice Box (Conf: 0.94)"],
        "ocr_text": "Apollo Hospitals Chennai - Total Paid: ₹45,000",
        "fuzzy_match_score": 98.4,
        "trust_score": 94.5,
        "verification_result": "AUTHENTIC"
    })

@app.route('/api/match-resume', methods=['POST'])
def match_resume_api():
    """Simulates NLP Resume Matcher API backend (spaCy TF-IDF Cosine Similarity)."""
    data = request.get_json() or {}
    target_role = data.get('role', 'python')

    scores = {
        'python': {"score": 94.8, "match": "Strong match for Python backend, API integration, and SQL."},
        'data': {"score": 92.4, "match": "High match for SQL queries, Pandas analysis, and Power BI."},
        'aiml': {"score": 96.1, "match": "Top tier match for YOLOv8, PaddleOCR, and spaCy NLP projects."}
    }

    result = scores.get(target_role, scores['python'])
    return jsonify({
        "status": "success",
        "role": target_role,
        "cosine_similarity": result["score"],
        "match_analysis": result["match"],
        "candidate": "Mohamed Rabbik M"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
