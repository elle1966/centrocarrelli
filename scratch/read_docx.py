import zipfile
import xml.etree.ElementTree as ET
import os

def read_docx(file_path):
    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # Namespace for wordprocessingml
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            texts = []
            for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                p_text = "".join(node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
                if p_text.strip():
                    texts.append(p_text)
            return "\n".join(texts)
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def search_docx_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(directory):
            if any(skip in root for skip in ['.git', '.netlify', 'node_modules', '.agents']):
                continue
            for file in files:
                if file.endswith('.docx'):
                    path = os.path.join(root, file)
                    out.write(f"\n=========================================\n")
                    out.write(f"FILE: {path}\n")
                    out.write(f"=========================================\n")
                    text = read_docx(path)
                    out.write(text)
                    out.write("\n\n")

if __name__ == '__main__':
    search_docx_files(r'c:\Users\elly\.antigravity\centrocarrelli', r'c:\Users\elly\.antigravity\centrocarrelli\scratch\extracted_docx_text.txt')
    print("Done! Extracted text to scratch/extracted_docx_text.txt")
