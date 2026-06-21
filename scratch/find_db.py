import os

def find_files(start_dir):
    extensions = ('.csv', '.xlsx', '.xls', '.db', '.sqlite', '.sql', '.json', '.xml')
    for root, dirs, files in os.walk(start_dir):
        # Skip some directories to be fast
        if any(skip in root for skip in ['.git', '.netlify', 'node_modules', '.agents']):
            continue
        for file in files:
            if file.endswith(extensions) or 'data' in file.lower() or 'prod' in file.lower() or 'db' in file.lower():
                full_path = os.path.join(root, file)
                print(f"File: {full_path} ({os.path.getsize(full_path)} bytes)")

if __name__ == '__main__':
    find_files(r'c:\Users\elly\.antigravity\centrocarrelli')
