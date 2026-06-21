import os

# New flotta grid section HTML code
FLOTTA_HTML = """    <!-- Flotta disponibile -->
    <div class="flotta-section" id="catalogo-transpallet">
        <div class="flotta-header">
            <h2>Gamma transpallet e sollevatori disponibili</h2>
            <p>I transpallet elettrici e stoccatori STILL disponibili per vendita e noleggio immediato.</p>
        </div>
        <div class="flotta-grid">
            <!-- STILL EXV 20 -->
            <a href="https://www.centrocarrelli.net/carrelli/sollevatore-elettrico-still-exv-20/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/04/SOLLEVATORE-ELETTRICO-STILL-EXV-20.jpg" alt="STILL EXV 20">
                <h3>STILL EXV 20</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 20</strong></li>
                    <li>Matricola: <strong>F22551N01051</strong></li>
                    <li>Anno: <strong>2024</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>2000 kg</strong></li>
                    <li>Sollevamento: <strong>3170 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXH SF 20 -->
            <a href="https://www.centrocarrelli.net/carrelli/transpallet-elettrico-still-exh-sf-20/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/TRANSPALLET-ELETTRICO-STILL-EXH-SF-20.webp" alt="STILL EXH SF 20">
                <h3>STILL EXH SF 20</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXH SF 20</strong></li>
                    <li>Matricola: <strong>W42362X01206</strong></li>
                    <li>Anno: <strong>2020</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>2000 kg</strong></li>
                    <li>Sollevamento: <strong>N/D</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXV 12 -->
            <a href="https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-12/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-ELETTRICO-STILL-EXV-12-3.jpg" alt="STILL EXV 12">
                <h3>STILL EXV 12</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 12</strong></li>
                    <li>Matricola: <strong>F20272J01779</strong></li>
                    <li>Anno: <strong>2018</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1200 kg</strong></li>
                    <li>Sollevamento: <strong>4386 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXV 14 (4800 mm) -->
            <a href="https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-14-3/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-STILL-EXV-14-2-1.jpg" alt="STILL EXV 14">
                <h3>STILL EXV 14</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 14</strong></li>
                    <li>Matricola: <strong>F20323H00792</strong></li>
                    <li>Anno: <strong>2017</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1400 kg</strong></li>
                    <li>Sollevamento: <strong>4800 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXV 14 (4350 mm) -->
            <a href="https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-14-2/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-STILL-EXV-14-3.jpg" alt="STILL EXV 14">
                <h3>STILL EXV 14</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 14</strong></li>
                    <li>Matricola: <strong>F20323H00773</strong></li>
                    <li>Anno: <strong>2017</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1400 kg</strong></li>
                    <li>Sollevamento: <strong>4350 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXH 16 -->
            <a href="https://www.centrocarrelli.net/carrelli/still-exh-16-transpallet-elettrico/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2025/11/STILL-EXH-16-2.jpg" alt="STILL EXH 16">
                <h3>STILL EXH 16</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXH 16</strong></li>
                    <li>Matricola: <strong>W42031P00027</strong></li>
                    <li>Anno: <strong>2025</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1600 kg</strong></li>
                    <li>Sollevamento: <strong>N/D</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXV 14 (4266 mm) -->
            <a href="https://www.centrocarrelli.net/carrelli/still-exv-14-sollevatore-a-colonna/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2025/11/SOLLEVATORE-STILL-EXV-14-2.jpg" alt="STILL EXV 14">
                <h3>STILL EXV 14</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 14</strong></li>
                    <li>Matricola: <strong>F20323H00763</strong></li>
                    <li>Anno: <strong>2017</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1400 kg</strong></li>
                    <li>Sollevamento: <strong>4266 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL EXV 12 (Transpallet a colonna) -->
            <a href="https://www.centrocarrelli.net/carrelli/still-exv-12-transpallet-a-colonna/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2025/11/TRANSPALLET-STILL-EXV-12-2.jpg" alt="STILL EXV 12">
                <h3>STILL EXV 12</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>EXV 12</strong></li>
                    <li>Matricola: <strong>F20272V...</strong></li>
                    <li>Anno: <strong>2019</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1200 kg</strong></li>
                    <li>Sollevamento: <strong>4386 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL ECH 15 C -->
            <a href="/ech15c.html" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Promo Litio</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2025/10/STILL-ECH-15C-e1760452876241.webp" alt="STILL ECH 15 C">
                <h3>STILL ECH 15 C</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>ECH 15 C</strong></li>
                    <li>Matricola: <strong>Promo</strong></li>
                    <li>Anno: <strong>2026</strong></li>
                    <li>Alimentazione: <strong>Ioni di Litio</strong></li>
                    <li>Portata: <strong>1500 kg</strong></li>
                    <li>Sollevamento: <strong>115 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL ECH 12 C -->
            <a href="/ech12c.html" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Promo Litio</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2025/10/STILL-ECH-12C-e1760452027521.webp" alt="STILL ECH 12 C">
                <h3>STILL ECH 12 C</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>ECH 12 C</strong></li>
                    <li>Matricola: <strong>Promo</strong></li>
                    <li>Anno: <strong>2026</strong></li>
                    <li>Alimentazione: <strong>Ioni di Litio</strong></li>
                    <li>Portata: <strong>1200 kg</strong></li>
                    <li>Sollevamento: <strong>115 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>
        </div>
    </div>"""

def update_file(path):
    if not os.path.exists(path):
        print(f'File not found: {path}')
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    # Find start and end of flotta-section
    start_tag = '<div class="flotta-section">'
    end_tag = '</div>'
    
    start_idx = html.find(start_tag, html.find('<!-- Flotta disponibile -->'))
    if start_idx == -1:
        # Fallback to general find
        start_idx = html.find('<!-- Flotta disponibile -->')
        if start_idx != -1:
            # Look for the next div
            start_idx = html.find('<div class="flotta-section"', start_idx)
            
    if start_idx != -1:
        # Find closing tag
        # We need to find the matching closing div for flotta-section
        # Since it contains exactly 1 sub grid div, it is the second </div> after flotta-section
        grid_idx = html.find('<div class="flotta-grid"', start_idx)
        if grid_idx != -1:
            first_close = html.find('</div>', grid_idx)
            if first_close != -1:
                second_close = html.find('</div>', first_close + 6)
                if second_close != -1:
                    # The second </div> is the closing tag of flotta-section
                    end_idx = second_close + 6
                    new_html = html[:start_idx] + FLOTTA_HTML + html[end_idx:]
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_html)
                    print(f'Successfully updated transpallet catalog in: {path}')
                    return
    print(f'Error locating flotta-section in: {path}')

if __name__ == '__main__':
    update_file(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\transpallet.html')
    # Copy or update workspace files if we want them in sync
