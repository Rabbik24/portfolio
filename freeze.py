"""
=============================================================================
Django Static Site Exporter Script
Freezes the Django app into a standalone static site inside the build/ directory
for deployment to GitHub Pages or static web hosts.
=============================================================================
"""

import os
import sys
import shutil

# Configure Django Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

import django
django.setup()

from django.test import Client

def build_static_site():
    print("[+] Initializing Django Static Exporter...")

    build_dir = os.path.join(os.path.dirname(__file__), 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)

    # Copy static folder
    static_src = os.path.join(os.path.dirname(__file__), 'static')
    static_dst = os.path.join(build_dir, 'static')
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst)

    # Render main index view using Django Test Client
    client = Client()
    response = client.get('/')
    if response.status_code == 200:
        index_path = os.path.join(build_dir, 'index.html')
        with open(index_path, 'wb') as f:
            f.write(response.content)
        print("[SUCCESS] Django static site exported successfully to build/index.html!")
    else:
        print(f"[!] Error exporting index view: Status {response.status_code}")

if __name__ == '__main__':
    build_static_site()
