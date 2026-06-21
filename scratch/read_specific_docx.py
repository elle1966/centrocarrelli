import sys
sys.stdout.reconfigure(encoding='utf-8')
import zipfile
import xml.etree.ElementTree as ET

def read_docx(file_path):
    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            texts = []
            for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                p_text = "".join(node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
                if p_text.strip():
                    texts.append(p_text)
            return "\n".join(texts)
    except Exception as e:
        return f"Error: {e}"

print("=== Specifiche_Tecniche_AGENZIA_Centrocarrelli.docx ===")
print(read_docx(r'c:\Users\elly\.antigravity\centrocarrelli\centrocarrelli seo 2025 LOGO 2026\Specifiche_Tecniche_AGENZIA_Centrocarrelli.docx'))
print("\n=== CentroCarrelli_Analisi_Cliente.docx ===")
print(read_docx(r'c:\Users\elly\.antigravity\centrocarrelli\centrocarrelli seo 2025 LOGO 2026\CentroCarrelli_Analisi_Cliente.docx'))
