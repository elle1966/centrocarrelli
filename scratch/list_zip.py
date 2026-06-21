import zipfile
import os

def list_zip(file_path):
    print(f"\nListing ZIP: {file_path}")
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            names = zip_ref.namelist()
            print(f"Total files: {len(names)}")
            # Show first 30 files
            for name in names[:30]:
                print(f"  {name}")
            if len(names) > 30:
                print("  ...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_zip(r'c:\Users\elly\.antigravity\centrocarrelli\centro2026.zip')
    list_zip(r'c:\Users\elly\.antigravity\centrocarrelli\deploy_centrocarrelli.zip')
