import shutil
import os

def deploy():
    src_html = r'c:\Users\elly\.antigravity\centrocarrelli\index.html'
    src_css = r'c:\Users\elly\.antigravity\centrocarrelli\style.css'
    src_js = r'c:\Users\elly\.antigravity\centrocarrelli\app.js'
    
    dest_html = r'c:\Users\elly\.antigravity\centrocarrelli\deploy\index.html'
    dest_css = r'c:\Users\elly\.antigravity\centrocarrelli\deploy\style.css'
    
    shutil.copy2(src_html, dest_html)
    shutil.copy2(src_css, dest_css)
    print("Successfully copied index.html and style.css to deploy/ directory!")

if __name__ == '__main__':
    deploy()
