"""
=============================================================================
Static Site Generator Script (Flask Exporter)
Freezes the Flask app into a standalone static site inside the build/ directory
for deployment to GitHub Pages or static web hosts.
=============================================================================
"""

import os
import shutil

from app import app

def build_static_site():
    print("[+] Initializing Static Build Exporter...")

    build_dir = os.path.join(os.path.dirname(__file__), 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)

    # Copy static folder
    static_src = os.path.join(os.path.dirname(__file__), 'static')
    static_dst = os.path.join(build_dir, 'static')
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst)

    # Try Flask-Freeze or standard Jinja2 context render
    try:
        from flask_frozen import Freezer
        freezer = Freezer(app)
        app.config['FREEZER_DESTINATION'] = 'build'
        app.config['FREEZER_RELATIVE_URLS'] = True
        print("[*] Freezing Flask routes into static HTML using Flask-Freeze...")
        freezer.freeze()
        print("[SUCCESS] Static site generated successfully in build/ directory!")
    except Exception as e:
        print(f"[!] Flask-Freeze fallback mode ({e}). Rendering index.html directly...")
        with app.test_request_context():
            from app import home
            html_content = home()
            index_path = os.path.join(build_dir, 'index.html')
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

        # Copy top-level fallback index.html if needed
        print("[SUCCESS] Static site rendered successfully in build/ directory!")

if __name__ == '__main__':
    build_static_site()
