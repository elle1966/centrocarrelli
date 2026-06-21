import os
import re
import subprocess

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Extract script tag content
    scripts = re.findall(r'<script.*?>\s*(.*?)\s*</script>', html, re.DOTALL)
    for i, script_content in enumerate(scripts):
        if 'initForkliftFinder' in script_content:
            temp_path = f'scratch_temp_script_{i}.js'
            with open(temp_path, 'w', encoding='utf-8') as tf:
                tf.write(script_content)
            
            print(f"Checking script index {i}...")
            # Run node -c
            res = subprocess.run(['node', '-c', temp_path], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"Script index {i} is syntactically CORRECT.")
            else:
                print(f"Script index {i} has SYNTAX ERROR:")
                print(res.stderr)
            
            # Clean up
            os.remove(temp_path)
else:
    print('homepage.html not found')
