/* ==========================================================================
   PORTFOLIO INTERACTIVE SCRIPT
   Mohamed Rabbik M - Software Developer & Data Analytics
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    /* --------------------------------------------------------------------------
       1. DYNAMIC TYPING EFFECT FOR HERO SECTION
       -------------------------------------------------------------------------- */
    const typingElement = document.getElementById('typingText');
    const roles = [
        "Software Developer",
        "Data Analytics Specialist",
        "AI & NLP Engineer",
        "Backend API Developer"
    ];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function typeEffect() {
        if (!typingElement) return;

        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typingElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50;
        } else {
            typingElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 100;
        }

        if (!isDeleting && charIndex === currentRole.length) {
            isDeleting = true;
            typingSpeed = 2000; // Pause at full word
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typingSpeed = 500;
        }

        setTimeout(typeEffect, typingSpeed);
    }

    typeEffect();

    /* --------------------------------------------------------------------------
       2. LIGHT / DARK THEME TOGGLE WITH LOCALSTORAGE
       -------------------------------------------------------------------------- */
    const themeToggleBtn = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('rabbik_theme');

    if (savedTheme === 'light') {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            if (document.body.classList.contains('light-theme')) {
                document.body.classList.remove('light-theme');
                document.body.classList.add('dark-theme');
                localStorage.setItem('rabbik_theme', 'dark');
                showToast('Switched to Dark Theme', 'info');
            } else {
                document.body.classList.remove('dark-theme');
                document.body.classList.add('light-theme');
                localStorage.setItem('rabbik_theme', 'light');
                showToast('Switched to Light Theme', 'info');
            }
        });
    }

    /* --------------------------------------------------------------------------
       3. NAVBAR SCROLL BACKGROUND & ACTIVE LINK HIGHLIGHTING
       -------------------------------------------------------------------------- */
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        // Sticky shadow on scroll
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Active section link highlighting
        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });

    /* --------------------------------------------------------------------------
       4. MOBILE HAMBURGER MENU TOGGLE
       -------------------------------------------------------------------------- */
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const navMenu = document.getElementById('navMenu');

    if (hamburgerBtn && navMenu) {
        hamburgerBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            hamburgerBtn.classList.toggle('active');
        });

        // Close mobile nav when clicking a link
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                hamburgerBtn.classList.remove('active');
            });
        });
    }

    /* --------------------------------------------------------------------------
       5. INTERACTIVE SKILL CATEGORY FILTER TABS
       -------------------------------------------------------------------------- */
    const filterTabs = document.querySelectorAll('.filter-tab');
    const skillCards = document.querySelectorAll('.skill-category-card');

    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            filterTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const filterValue = tab.getAttribute('data-filter');

            skillCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filterValue === 'all' || category === filterValue) {
                    card.style.display = 'block';
                    card.style.opacity = '1';
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                }
            });
        });
    });

    /* --------------------------------------------------------------------------
       6. HERO STATS ANIMATED NUMBER COUNTERS
       -------------------------------------------------------------------------- */
    const statNumbers = document.querySelectorAll('.stat-number');
    let animated = false;

    function animateCounters() {
        if (animated) return;
        const heroSection = document.getElementById('hero');
        const sectionPos = heroSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.2;

        if (sectionPos < screenPos) {
            statNumbers.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'));
                const duration = 1500;
                const increment = target / (duration / 16);
                let current = 0;

                const updateCount = () => {
                    current += increment;
                    if (current < target) {
                        counter.textContent = Math.ceil(current);
                        requestAnimationFrame(updateCount);
                    } else {
                        counter.textContent = target;
                    }
                };

                updateCount();
            });
            animated = true;
        }
    }

    window.addEventListener('scroll', animateCounters);
    animateCounters(); // Initial trigger

    /* --------------------------------------------------------------------------
       7. COPY TO CLIPBOARD WITH TOAST FEEDBACK
       -------------------------------------------------------------------------- */
    const copyBtns = document.querySelectorAll('.copy-btn');

    copyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const textToCopy = btn.getAttribute('data-copy');
            navigator.clipboard.writeText(textToCopy).then(() => {
                showToast(`Copied to clipboard: ${textToCopy}`, 'success');
            }).catch(() => {
                showToast('Failed to copy text', 'error');
            });
        });
    });

    /* --------------------------------------------------------------------------
       8. CONTACT FORM SUBMISSION SIMULATOR
       -------------------------------------------------------------------------- */
    const contactForm = document.getElementById('contactForm');
    const sendMsgBtn = document.getElementById('sendMsgBtn');

    if (contactForm && sendMsgBtn) {
        sendMsgBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const name = document.getElementById('senderName').value.trim();
            const email = document.getElementById('senderEmail').value.trim();
            const subject = document.getElementById('msgSubject').value.trim();
            const message = document.getElementById('senderMessage').value.trim();

            if (!name || !email || !subject || !message) {
                showToast('Please fill in all form fields.', 'warning');
                return;
            }

            // Simulate sending message
            sendMsgBtn.disabled = true;
            sendMsgBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Sending...';

            setTimeout(() => {
                showToast(`Thank you, ${name}! Your message has been sent successfully.`, 'success');
                contactForm.reset();
                sendMsgBtn.disabled = false;
                sendMsgBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Message';
            }, 1200);
        });
    }

    /* --------------------------------------------------------------------------
       9. PRINTABLE SINGLE-COLUMN RESUME OVERLAY MODAL
       -------------------------------------------------------------------------- */
    const resumeModeToggle = document.getElementById('resumeModeToggle');
    const openResumeModal = document.getElementById('openResumeModal');
    const resumeViewOverlay = document.getElementById('resumeViewOverlay');
    const closeResumeView = document.getElementById('closeResumeView');

    function openResume() {
        if (resumeViewOverlay) resumeViewOverlay.classList.add('active');
    }

    function closeResume() {
        if (resumeViewOverlay) resumeViewOverlay.classList.remove('active');
    }

    if (resumeModeToggle) resumeModeToggle.addEventListener('click', openResume);
    if (openResumeModal) openResumeModal.addEventListener('click', openResume);
    if (closeResumeView) closeResumeView.addEventListener('click', closeResume);

    if (resumeViewOverlay) {
        resumeViewOverlay.addEventListener('click', (e) => {
            if (e.target === resumeViewOverlay) closeResume();
        });
    }

    /* --------------------------------------------------------------------------
       10. PROJECT INTERACTIVE DEMO MODALS
       -------------------------------------------------------------------------- */
    const projectTriggers = document.querySelectorAll('.project-modal-trigger');
    const projectModalOverlay = document.getElementById('projectModalOverlay');
    const projectModalBody = document.getElementById('projectModalBody');
    const closeProjectModal = document.getElementById('closeProjectModal');

    const projectData = {
        project1: {
            title: "AI-Driven Medical Fundraising Verification System",
            tags: ["Python", "YOLOv8", "PaddleOCR", "Flask", "MySQL", "JWT", "Bcrypt", "Fuzzy Matching"],
            description: "A machine learning and computer vision framework designed to verify medical campaign authenticity and detect fraudulent medical document submissions.",
            architecture: [
                "1. Document Upload (Medical Invoices/Reports) via Flask REST API.",
                "2. YOLOv8 object detection locates bill header, total amount, hospital seals & doctor signatures.",
                "3. PaddleOCR extracts text content from bounded region bounding boxes.",
                "4. Fuzzy Matching algorithms compare extracted hospital names against verified medical databases.",
                "5. Trust Score Engine computes overall confidence score (0 - 100%).",
                "6. JWT authentication ensures role-based authorization for auditors and admins."
            ],
            demoType: "ocr"
        },
        project2: {
            title: "Resume Screening Using NLP | Group Project",
            tags: ["Python", "NLP", "spaCy", "TF-IDF", "Streamlit", "Vector Similarity"],
            description: "An automated candidate shortlisting engine built with Python and spaCy to calculate cosine similarity between candidate resume texts and job descriptions.",
            architecture: [
                "1. Multi-format Resume Ingestion (PDF/Docx/Text).",
                "2. Natural Language Preprocessing: Stopword removal, lemmatization, tokenization using spaCy.",
                "3. Feature Extraction: Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.",
                "4. Cosine Similarity Calculation to rank candidates based on skill match percentage.",
                "5. Streamlit Dashboard providing recruiters visual match metrics and top candidate shortlists."
            ],
            demoType: "nlp"
        }
    };

    projectTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const key = trigger.getAttribute('data-project');
            const data = projectData[key];
            if (!data) return;

            renderProjectModal(data);
            projectModalOverlay.classList.add('active');
        });
    });

    if (closeProjectModal) {
        closeProjectModal.addEventListener('click', () => {
            projectModalOverlay.classList.remove('active');
        });
    }

    if (projectModalOverlay) {
        projectModalOverlay.addEventListener('click', (e) => {
            if (e.target === projectModalOverlay) {
                projectModalOverlay.classList.remove('active');
            }
        });
    }

    function renderProjectModal(data) {
        let demoWidgetHtml = '';

        if (data.demoType === 'ocr') {
            demoWidgetHtml = `
                <div class="interactive-demo-box">
                    <div class="demo-title">
                        <i class="fa-solid fa-microchip"></i> Live AI Document Verification Simulator
                    </div>
                    <p style="font-size:0.85rem; color: var(--text-secondary); margin-bottom:1rem;">
                        Simulate how YOLOv8 + PaddleOCR extracts bounding boxes and calculates the campaign <strong>Trust Score</strong>.
                    </p>
                    <div class="ocr-sim-container">
                        <div class="doc-preview-box">
                            <div class="yolo-box"><i class="fa-solid fa-crop"></i> YOLOv8: Hospital Seal Detected</div>
                            <div class="yolo-box"><i class="fa-solid fa-crop"></i> YOLOv8: Patient ID & Bill Amount</div>
                            <div style="font-size:0.75rem; color:#8b949e; margin-top:0.5rem;">
                                [PaddleOCR Text Extraction]:<br>
                                "Apollo Hospital - Bill #98421 - Amt: ₹45,000"
                            </div>
                        </div>
                        <div class="ocr-result-box">
                            <div><strong>Verification Results:</strong></div>
                            <div style="margin-top:0.4rem;">Hospital DB Match: <span style="color:var(--success);">100% (Fuzzy Ratio: 0.98)</span></div>
                            <div>Doctor Sign Auth: <span style="color:var(--success);">Verified</span></div>
                            <div style="margin-top:0.8rem; font-weight:600;">Calculated Campaign Trust Score:</div>
                            <div style="font-size:1.2rem; font-weight:700; color:var(--success);">94.5% (AUTHENTIC)</div>
                            <div class="score-meter"><div class="score-fill"></div></div>
                        </div>
                    </div>
                </div>
            `;
        } else if (data.demoType === 'nlp') {
            demoWidgetHtml = `
                <div class="interactive-demo-box">
                    <div class="demo-title">
                        <i class="fa-solid fa-brain"></i> Interactive Candidate Match Score Tester
                    </div>
                    <p style="font-size:0.85rem; color: var(--text-secondary); margin-bottom:1rem;">
                        Test Mohamed Rabbik's candidate match score against a target job role using spaCy & TF-IDF similarity.
                    </p>
                    <div style="margin-bottom: 1rem;">
                        <label style="font-size:0.85rem; font-weight:600; display:block; margin-bottom:0.3rem;">Select Target Job Profile:</label>
                        <select id="roleSelector" class="form-input" style="padding:0.5rem;">
                            <option value="python">Python Software Developer (Flask / SQL / REST APIs)</option>
                            <option value="data">Data Analytics Specialist (Pandas / Power BI / SQL)</option>
                            <option value="aiml">AI / ML Engineer (YOLOv8 / spaCy / Computer Vision)</option>
                        </select>
                    </div>
                    <div class="ocr-result-box" id="nlpResultBox">
                        <div><strong>Matching Candidate: Mohamed Rabbik M</strong></div>
                        <div style="margin-top:0.5rem;">Preprocessed Tokens: <code style="color:var(--accent-secondary);">["python", "sql", "flask", "nlp", "spacy", "powerbi", "mca"]</code></div>
                        <div style="margin-top:0.5rem;">TF-IDF Cosine Similarity Score: <strong style="color:var(--success);" id="similarityScore">94.8%</strong></div>
                        <div style="margin-top:0.5rem; font-size:0.85rem; color:var(--text-secondary);" id="matchDetails">High match for Python backend, API integration, and database management.</div>
                    </div>
                </div>
            `;
        }

        const tagsHtml = data.tags.map(t => `<span class="mini-tag">${t}</span>`).join(' ');
        const archHtml = data.architecture.map(a => `<li style="margin-bottom:0.4rem; color:var(--text-secondary);"><i class="fa-solid fa-check text-accent"></i> ${a}</li>`).join('');

        projectModalBody.innerHTML = `
            <div class="pm-header">
                <h2 class="pm-title">${data.title}</h2>
                <div class="pm-tags">${tagsHtml}</div>
                <p style="color:var(--text-secondary); font-size:1.05rem;">${data.description}</p>
            </div>
            
            ${demoWidgetHtml}

            <div style="margin-top:1.5rem;">
                <h3 style="font-family:var(--font-heading); font-size:1.15rem; margin-bottom:0.75rem;"><i class="fa-solid fa-sitemap"></i> System Architecture & Workflow</h3>
                <ul style="list-style:none;">${archHtml}</ul>
            </div>
        `;

        // Add event listener for dynamic roleSelector if NLP demo
        const roleSelector = document.getElementById('roleSelector');
        if (roleSelector) {
            roleSelector.addEventListener('change', (e) => {
                const val = e.target.value;
                const scoreEl = document.getElementById('similarityScore');
                const detailsEl = document.getElementById('matchDetails');

                if (val === 'python') {
                    scoreEl.textContent = '94.8%';
                    detailsEl.textContent = 'Excellent match for Python backend, API integration, and database management.';
                } else if (val === 'data') {
                    scoreEl.textContent = '92.4%';
                    detailsEl.textContent = 'Strong match for SQL queries, Pandas data manipulation, and Power BI reporting.';
                } else if (val === 'aiml') {
                    scoreEl.textContent = '96.1%';
                    detailsEl.textContent = 'Top tier match with hands-on YOLOv8, PaddleOCR, and spaCy project experience!';
                }
            });
        }
    }

    /* --------------------------------------------------------------------------
       11. TOAST NOTIFICATION HELPER
       -------------------------------------------------------------------------- */
    function showToast(message, type = 'info') {
        const toastContainer = document.getElementById('toastContainer');
        if (!toastContainer) return;

        const toast = document.createElement('div');
        toast.className = 'toast-msg';

        let icon = 'fa-info-circle';
        let borderColor = 'var(--accent-primary)';

        if (type === 'success') {
            icon = 'fa-circle-check';
            borderColor = 'var(--success)';
        } else if (type === 'warning') {
            icon = 'fa-triangle-exclamation';
            borderColor = 'var(--warning)';
        } else if (type === 'error') {
            icon = 'fa-circle-xmark';
            borderColor = 'var(--danger)';
        }

        toast.style.borderLeftColor = borderColor;
        toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;

        toastContainer.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideInRight 0.3s reverse forwards';
            setTimeout(() => toast.remove(), 300);
        }, 3500);
    }

});
