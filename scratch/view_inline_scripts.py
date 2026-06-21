with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'finder-sidebar' in line or 'Filtri di Ricerca' in line:
        print(f"Line {i+1}: {line.strip()}")
        # print next 10 lines
        for k in range(1, 20):
            if i + k < len(lines):
                print(f"  +{k}: {lines[i+k].strip()}")
        print("-" * 50)
