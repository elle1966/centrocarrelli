import os
import re

def clean_file():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_dir, "clean_body.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strip the specific text blocks at the end
    patterns_to_remove = [
        r'WordPress / Oxygen Simulator Styles',
        r'WordPress / Oxygen Simulator Panel',
        r'Notification Toast',
        r'WordPress Customizer JS Controller'
    ]
    
    cleaned = content
    for pattern in patterns_to_remove:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
    # Remove empty lines at the end
    cleaned = re.sub(r'\n\s*\n', '\n', cleaned)
    cleaned = cleaned.strip()
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(cleaned)
        
    print("clean_body.html cleaned successfully!")

if __name__ == "__main__":
    clean_file()
