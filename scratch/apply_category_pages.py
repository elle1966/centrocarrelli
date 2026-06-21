import os
import re

FRONTALI_CARDS_HTML = """            <!-- STILL R 60-25 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-r-60-25/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/CARRELLO-ELEVATORE-ELETTRICO-STILL-R-60-25-3.jpg" alt="STILL R 60-25">
                <h3>STILL R 60-25</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>R 60-25</strong></li>
                    <li>Matricola: <strong>51602312050</strong></li>
                    <li>Anno: <strong>2000</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>2500 kg</strong></li>
                    <li>Sollevamento: <strong>4200 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 60-50 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-60-50-3/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-60-50-3.jpg" alt="STILL RX 60-50">
                <h3>STILL RX 60-50</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 60-50</strong></li>
                    <li>Matricola: <strong>516329X00218</strong></li>
                    <li>Anno: <strong>2020</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>5000 kg</strong></li>
                    <li>Sollevamento: <strong>4630 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 60-30 L/600 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-still-rx-60-30-l-600/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-60-30L-600-3.jpg" alt="STILL RX 60-30 L/600">
                <h3>STILL RX 60-30 L/600</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 60-30 L / 600</strong></li>
                    <li>Matricola: <strong>516308X00119</strong></li>
                    <li>Anno: <strong>2020</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>3000 kg</strong></li>
                    <li>Sollevamento: <strong>5540 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 60-30 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-still-rx-60-30/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-60-30-3.jpg" alt="STILL RX 60-30">
                <h3>STILL RX 60-30</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 60-30</strong></li>
                    <li>Matricola: <strong>516353H00240</strong></li>
                    <li>Anno: <strong>2017</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>3000 kg</strong></li>
                    <li>Sollevamento: <strong>4170 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 60-25 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-60-25-8/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-60-25-2.jpg" alt="STILL RX 60-25">
                <h3>STILL RX 60-25</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 60-25</strong></li>
                    <li>Matricola: <strong>516301X00877</strong></li>
                    <li>Anno: <strong>2020</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>2500 kg</strong></li>
                    <li>Sollevamento: <strong>4890 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 20-20 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-20-4/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-20-20-3.jpg" alt="STILL RX 20-20">
                <h3>STILL RX 20-20</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 20-20</strong></li>
                    <li>Matricola: <strong>516215H01190</strong></li>
                    <li>Anno: <strong>2017</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>2000 kg</strong></li>
                    <li>Sollevamento: <strong>4765 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 20-18 P -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-18-p/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-18-P-3.jpg" alt="STILL RX 20-18 P">
                <h3>STILL RX 20-18 P</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 20-18 P</strong></li>
                    <li>Matricola: <strong>516226X00036</strong></li>
                    <li>Anno: <strong>2020</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1800 kg</strong></li>
                    <li>Sollevamento: <strong>5070 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 20-18 -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-18-13/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-18-4.jpg" alt="STILL RX 20-18">
                <h3>STILL RX 20-18</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 20-18</strong></li>
                    <li>Matricola: <strong>516223V01032</strong></li>
                    <li>Anno: <strong>2019</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1800 kg</strong></li>
                    <li>Sollevamento: <strong>4770 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 20-16 P -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-16-p/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-26-P-2.jpg" alt="STILL RX 20-16 P">
                <h3>STILL RX 20-16 P</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 20-16 P</strong></li>
                    <li>Matricola: <strong>516226Y00057</strong></li>
                    <li>Anno: <strong>2021</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1600 kg</strong></li>
                    <li>Sollevamento: <strong>4620 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>

            <!-- STILL RX 20-16 C -->
            <a href="https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-16-c/" target="_blank" class="flotta-item">
                <span style="position:absolute;top:15px;right:15px;background:#F96815;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:3px 8px;z-index:2;">Elettrico</span>
                <img src="https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-20-16-C-3.jpg" alt="STILL RX 20-16 C">
                <h3>STILL RX 20-16 C</h3>
                <ul class="specs">
                    <li>Marca: <strong>STILL</strong></li>
                    <li>Modello: <strong>RX 20-16 C</strong></li>
                    <li>Matricola: <strong>516220Y00150</strong></li>
                    <li>Anno: <strong>2021</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1600 kg</strong></li>
                    <li>Sollevamento: <strong>5220 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>"""

MAGAZZINO_CARDS_HTML = """            <!-- STILL EXV 20 -->
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
                    <li>Matricola: <strong>F20272V00365-V00387-V00399</strong></li>
                    <li>Anno: <strong>2019</strong></li>
                    <li>Alimentazione: <strong>Elettrico</strong></li>
                    <li>Portata: <strong>1200 kg</strong></li>
                    <li>Sollevamento: <strong>4386 mm</strong></li>
                </ul>
                <div class="card-btn">Vedi Dettagli</div>
            </a>"""

PREMIUM_STYLE_CSS = """        .flotta-grid {
            max-width: 1100px; margin: 0 auto;
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;
        }
        .flotta-item {
            background: #fff; border: 1px solid var(--color-border); padding: 24px; text-align: left;
            transition: all 250ms ease-in-out;
            display: flex; flex-direction: column;
            text-decoration: none; color: inherit;
            position: relative;
        }
        .flotta-item:hover {
            transform: translateY(-4px);
            border-color: var(--color-orange);
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }
        .flotta-item img { width: 100%; height: 180px; object-fit: contain; margin-bottom: 20px; background: #F5F4F2; padding: 10px; }
        .flotta-item h3 { font-family: 'Archivo', sans-serif; font-size: 1.1rem; font-weight: 800; color: var(--color-ink); margin-bottom: 12px; line-height: 1.2; }
        .flotta-item ul.specs { list-style: none; padding: 0; margin: 0 0 20px 0; flex-grow: 1; }
        .flotta-item ul.specs li { font-size: 0.82rem; color: var(--color-body); padding: 6px 0; border-bottom: 1px solid #f2f1ef; }
        .flotta-item ul.specs li:last-child { border-bottom: none; }
        .flotta-item ul.specs li strong { color: var(--color-ink); float: right; }
        .flotta-item .card-btn {
            display: block; width: 100%; text-align: center; background: var(--color-orange); color: #fff;
            padding: 12px 0; font-family: 'Archivo', sans-serif; font-size: 0.82rem; font-weight: 700;
            text-transform: uppercase; letter-spacing: 0.5px; margin-top: auto; transition: background 150ms ease;
        }
        .flotta-item:hover .card-btn { background: #e25a0c; }"""

def update_frontali():
    path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\carrelli-frontali.html'
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    # Replace style blocks for flotta-grid and flotta-item
    # We find start of .flotta-grid and end of .flotta-item in the stylesheet
    pattern_style = r'\.flotta-grid\s*\{.*?\}\s*\.flotta-item\s*\{.*?\}\s*\.flotta-item img\s*\{.*?\}\s*\.flotta-item h4\s*\{.*?\}\s*\.flotta-item p\s*\{.*?\}'
    html = re.sub(pattern_style, PREMIUM_STYLE_CSS, html, flags=re.DOTALL)
    
    # Let's verify if style was replaced. If not, we can replace the entire block of CSS under /* Flotta */
    if PREMIUM_STYLE_CSS not in html:
        # Fallback regex replacing everything from /* Flotta */ to .cta-band
        flotta_style_pattern = r'/\*\s*Flotta\s*\*/.*?(?=\.cta-band)'
        html = re.sub(flotta_style_pattern, '/* Flotta */\n' + PREMIUM_STYLE_CSS + '\n\n        ', html, flags=re.DOTALL)
        
    # Replace flotta-section content
    # Find start and end of flotta-section
    start_tag = '<!-- Flotta disponibile -->'
    start_idx = html.find(start_tag)
    if start_idx != -1:
        end_idx = html.find('<!-- CTA -->', start_idx)
        if end_idx != -1:
            new_section = """<!-- Flotta disponibile -->
    <div class="flotta-section" id="catalogo-frontali">
        <div class="flotta-header">
            <h2>Carrelli frontali usati disponibili</h2>
            <p>Una selezione di carrelli frontali STILL e Lugli ricondizionati e garantiti, pronti per la consegna.</p>
        </div>
        <div class="flotta-grid">
""" + FRONTALI_CARDS_HTML + """
        </div>
    </div>

    """
            html = html[:start_idx] + new_section + html[end_idx:]
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated Frontali: {path}")

def update_magazzino():
    path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\carrelli-magazzino.html'
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    # Replace style blocks for flotta-grid and flotta-item
    flotta_style_pattern = r'/\*\s*Flotta\s*\*/.*?(?=\.cta-band)'
    html = re.sub(flotta_style_pattern, '/* Flotta */\n' + PREMIUM_STYLE_CSS + '\n\n        ', html, flags=re.DOTALL)
        
    # Replace flotta-section content
    start_tag = '<!-- Flotta disponibile -->'
    start_idx = html.find(start_tag)
    if start_idx != -1:
        end_idx = html.find('<!-- CTA -->', start_idx)
        if end_idx != -1:
            new_section = """<!-- Flotta disponibile -->
    <div class="flotta-section" id="catalogo-magazzino">
        <div class="flotta-header">
            <h2>Carrelli da magazzino usati disponibili</h2>
            <p>Una selezione di sollevatori e stoccatori STILL ricondizionati e garantiti, pronti per la consegna.</p>
        </div>
        <div class="flotta-grid">
""" + MAGAZZINO_CARDS_HTML + """
        </div>
    </div>

    """
            html = html[:start_idx] + new_section + html[end_idx:]
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated Magazzino: {path}")

if __name__ == '__main__':
    update_frontali()
    update_magazzino()
