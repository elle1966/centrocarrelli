import os
import re
from bs4 import BeautifulSoup

# Premium styling for the new selects (restored dark styled premium look)
SELECTS_CSS = """
/* --- Dropdown Finder Select Styles --- */
.finder-sidebar {
    background-color: var(--color-graphite) !important;
    color: #FFFFFF !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
    padding: 40px 28px !important;
}
.finder-select {
    display: block;
    width: 100%;
    padding: 12px 14px;
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
    font-size: 0.9rem;
    font-family: 'Archivo', sans-serif;
    border-radius: var(--radius-sm, 4px);
    margin-bottom: 14px;
    transition: all 150ms ease;
    cursor: pointer;
    outline: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 14px center;
    background-size: 14px;
    padding-right: 40px;
}
.finder-select:hover {
    background-color: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.25);
}
.finder-select:focus {
    border-color: var(--color-orange, #F96815);
    box-shadow: 0 0 0 2px rgba(249, 104, 21, 0.25);
}
.finder-select option {
    background-color: #1E293B; /* Slate 800 */
    color: #FFFFFF;
}
#btn-finder-cerca {
    display: inline-block;
    width: 100%;
    padding: 12px 14px;
    background-color: var(--color-orange, #F96815);
    color: #0F172A;
    border: none;
    border-radius: var(--radius-sm, 4px);
    font-size: 0.95rem;
    font-family: 'Archivo', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    text-align: center;
    cursor: pointer;
    transition: all 150ms ease;
    box-shadow: 0 2px 4px rgba(249, 104, 21, 0.2);
}
#btn-finder-cerca:hover {
    background-color: #E25D0E;
    box-shadow: 0 4px 8px rgba(249, 104, 21, 0.3);
}
.screen-reader-text {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}
"""

SIDEBAR_HTML_CODE = """<div class="finder-sidebar">
    <div class="filter-header" style="text-align: center; margin-bottom: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#F96815" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 8px;">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            <line x1="11" y1="8" x2="11" y2="14"></line>
            <line x1="8" y1="11" x2="14" y2="11"></line>
        </svg>
        <h3 style="color:#FFF; font-family:'Archivo',sans-serif; font-weight:800; font-size:1.2rem; text-transform:uppercase; letter-spacing:1px; margin:0; border-bottom: none; padding-bottom: 0;">CERCA CARRELLI</h3>
    </div>
    
    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-categoria" class="screen-reader-text">Categoria</label>
        <select id="filter-categoria" name="categoria" class="finder-select">
            <option value="">Tutti i prodotti</option>
            <option value="frontali">Carrelli Frontali</option>
            <option value="magazzino">Carrelli magazzino</option>
            <option value="transpallet">Transpallet</option>
            <option value="occasioni">Occasioni</option>
        </select>
    </div>

    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-anno" class="screen-reader-text">Anno</label>
        <select id="filter-anno" name="anno" class="finder-select">
            <option value="">Anno</option>
            <option value="2026">2026</option>
            <option value="2025">2025</option>
            <option value="2024">2024</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
            <option value="2017">2017</option>
            <option value="2006">2006</option>
            <option value="2002">2002</option>
            <option value="2000">2000</option>
            <option value="1996">1996</option>
            <option value="1989">1989</option>
        </select>
    </div>

    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-alimentazione" class="screen-reader-text">Alimentazione</label>
        <select id="filter-alimentazione" name="alimentazione" class="finder-select">
            <option value="">Tutte le alimentazioni</option>
            <option value="Elettrico">Elettrico</option>
            <option value="diesel">Diesel / GPL</option>
            <option value="Manuale">Manuale</option>
        </select>
    </div>

    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-portata" class="screen-reader-text">Portata Kg.</label>
        <select id="filter-portata" name="portata" class="finder-select">
            <option value="">Portata Kg.</option>
            <option value="1000-2000">1000 - 2000</option>
            <option value="2000-3000">2000 - 3000</option>
            <option value="3000-4000">3000 - 4000</option>
            <option value="4000-5000">4000 - 5000</option>
            <option value="5000-6000">5000 - 6000</option>
            <option value="6000-7000">6000 - 7000</option>
            <option value="7000-8000">7000 - 8000</option>
            <option value="8000-9000">8000 - 9000</option>
        </select>
    </div>

    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-sollevamento" class="screen-reader-text">Sollevamento mm.</label>
        <select id="filter-sollevamento" name="sollevamento" class="finder-select">
            <option value="">Sollevamento mm.</option>
            <option value="0-2000">0 - 2000 mm</option>
            <option value="2200-2700">2200 - 2700 mm</option>
            <option value="2700-3200">2700 - 3200 mm</option>
            <option value="3200-3700">3200 - 3700 mm</option>
            <option value="3700-4200">3700 - 4200 mm</option>
            <option value="4200-4700">4200 - 4700 mm</option>
            <option value="4700-5200">4700 - 5200 mm</option>
            <option value="5200-5700">5200 - 5700 mm</option>
            <option value="5700-6200">5700 - 6200 mm</option>
            <option value="6200-6700">6200 - 6700 mm</option>
            <option value="6700-7200">6700 - 7200 mm</option>
            <option value="7200-7700">7200 - 7700 mm</option>
            <option value="7700-8200">7700 - 8200 mm</option>
        </select>
    </div>

    <div class="filter-group" style="margin-bottom: 12px;">
        <label for="filter-marca" class="screen-reader-text">Marca</label>
        <select id="filter-marca" name="marca" class="finder-select">
            <option value="">Tutte le marche</option>
            <option value="STILL">STILL</option>
            <option value="OM">OM</option>
            <option value="LUGLI">LUGLI</option>
            <option value="LINDE">LINDE</option>
            <option value="CESAB">CESAB</option>
            <option value="CARER">CARER</option>
        </select>
    </div>

    <button id="btn-finder-cerca">Cerca</button>
</div>"""

JS_CONTROLLER_CODE = r"""function initForkliftFinder() {
    const resultsGrid = document.getElementById('results-grid');
    const resultsCount = document.getElementById('results-count');
    const selectCategoria = document.getElementById('filter-categoria');
    const selectAnno = document.getElementById('filter-anno');
    const selectAlimentazione = document.getElementById('filter-alimentazione');
    const selectPortata = document.getElementById('filter-portata');
    const selectSollevamento = document.getElementById('filter-sollevamento');
    const selectMarca = document.getElementById('filter-marca');
    const btnCerca = document.getElementById('btn-finder-cerca');

    if (!resultsGrid) return;

    // Dynamically calculate and set counts in category select options
    function updateCategoryCounts() {
        if (!selectCategoria) return;
        const counts = {
            tutti: PRODUCTS.length,
            frontali: PRODUCTS.filter(p => p.specs.tipologia === 'frontali').length,
            magazzino: PRODUCTS.filter(p => p.specs.tipologia === 'magazzino').length,
            transpallet: PRODUCTS.filter(p => p.specs.tipologia === 'transpallet').length,
            occasioni: PRODUCTS.filter(p => p.isOccasione).length
        };
        
        for (let i = 0; i < selectCategoria.options.length; i++) {
            const opt = selectCategoria.options[i];
            if (opt.value === '') {
                opt.textContent = `Tutti i prodotti (${counts.tutti})`;
            } else if (opt.value === 'frontali') {
                opt.textContent = `Carrelli Frontali (${counts.frontali})`;
            } else if (opt.value === 'magazzino') {
                opt.textContent = `Carrelli magazzino (${counts.magazzino})`;
            } else if (opt.value === 'transpallet') {
                opt.textContent = `Transpallet (${counts.transpallet})`;
            } else if (opt.value === 'occasioni') {
                opt.textContent = `Occasioni (${counts.occasioni})`;
            }
        }
    }

    function parseVal(val) {
        if (!val) return 0;
        const clean = val.toString().replace(/\D/g, '');
        return clean ? parseInt(clean, 10) : 0;
    }

    function renderProducts() {
        const cat = selectCategoria ? selectCategoria.value : '';
        const anno = selectAnno ? selectAnno.value : '';
        const alim = selectAlimentazione ? selectAlimentazione.value : '';
        const portata = selectPortata ? selectPortata.value : '';
        const sollevamento = selectSollevamento ? selectSollevamento.value : '';
        const marca = selectMarca ? selectMarca.value : '';

        // Check if any filters are active
        const hasActiveFilters = !!(cat || anno || alim || portata || sollevamento || marca);

        const filtered = PRODUCTS.filter(prod => {
            // 1. Categoria
            let matchCat = false;
            if (!cat) {
                matchCat = true;
            } else if (cat === 'occasioni') {
                matchCat = prod.isOccasione === true;
            } else {
                matchCat = prod.specs.tipologia === cat;
            }

            // 2. Anno
            let matchAnno = true;
            if (anno) {
                matchAnno = prod.specs.anno === anno;
            }

            // 3. Alimentazione
            let matchAlim = true;
            if (alim) {
                const prodAlim = prod.specs.alimentazione.toLowerCase();
                if (alim === 'diesel') {
                    matchAlim = prodAlim === 'diesel' || prodAlim === 'gpl';
                } else if (alim === 'Elettrico') {
                    matchAlim = prodAlim === 'elettrico' || prodAlim.includes('litio');
                } else if (alim === 'Manuale') {
                    matchAlim = prodAlim === 'manuale';
                }
            }

            // 4. Portata
            let matchPortata = true;
            if (portata) {
                const parts = portata.split('-');
                const min = parseInt(parts[0], 10);
                const max = parseInt(parts[1], 10);
                const pVal = parseVal(prod.specs.portata);
                matchPortata = pVal >= min && pVal <= max;
            }

            // 5. Sollevamento
            let matchSollevamento = true;
            if (sollevamento) {
                const parts = sollevamento.split('-');
                const min = parseInt(parts[0], 10);
                const max = parseInt(parts[1], 10);
                const sVal = parseVal(prod.specs.altezza);
                matchSollevamento = sVal >= min && sVal <= max;
            }

            // 6. Marca
            let matchMarca = true;
            if (marca) {
                matchMarca = prod.specs.marca.toUpperCase() === marca.toUpperCase();
            }

            return matchCat && matchAnno && matchAlim && matchPortata && matchSollevamento && matchMarca;
        });

        // Sort by year descending (newest first) to show "Ultimi Inseriti" first
        filtered.sort((a, b) => {
            const yearA = parseInt(a.specs.anno || 0, 10);
            const yearB = parseInt(b.specs.anno || 0, 10);
            return yearB - yearA;
        });

        // Update count text or display "Ultimi Inseriti" when no filters are active
        if (resultsCount) {
            if (hasActiveFilters) {
                resultsCount.textContent = `${filtered.length} Carrelli Trovati`;
            } else {
                resultsCount.textContent = `Ultimi Inseriti (${filtered.length} Carrelli)`;
            }
        }

        // Clear grid
        resultsGrid.innerHTML = '';

        if (filtered.length === 0) {
            resultsGrid.innerHTML = `
                <div class="empty-state" style="grid-column: 1 / -1; text-align: center; padding: 40px; background: #fff; border: 1px solid var(--color-border);">
                    <h3>Nessun carrello corrisponde ai filtri selezionati</h3>
                    <p>Prova a modificare i filtri per visualizzare altre soluzioni, oppure contattaci direttamente per una consulenza su misura.</p>
                    <button class="btn btn-primary" style="margin-top: 20px;" onclick="resetFilters()">Ripristina Filtri</button>
                </div>
            `;
            return;
        }

        // Add cards to grid
        filtered.forEach(prod => {
            const card = document.createElement('div');
            card.className = 'product-card';
            
            let specsHtml = '';
            if (prod.specs.marca) specsHtml += `<li>Marca: <strong>${prod.specs.marca}</strong></li>`;
            if (prod.specs.modello) specsHtml += `<li>Modello: <strong>${prod.specs.modello}</strong></li>`;
            if (prod.specs.matricola) specsHtml += `<li>Matricola: <strong>${prod.specs.matricola}</strong></li>`;
            if (prod.specs.anno) specsHtml += `<li>Anno: <strong>${prod.specs.anno}</strong></li>`;
            if (prod.specs.alimentazione) {
                specsHtml += `<li>Alimentazione: <strong style="text-transform: capitalize;">${prod.specs.alimentazione}</strong></li>`;
            }
            if (prod.specs.portata) specsHtml += `<li>Portata: <strong>${prod.specs.portata}</strong></li>`;
            if (prod.specs.altezza) specsHtml += `<li>Sollevamento: <strong>${prod.specs.altezza}</strong></li>`;

            card.innerHTML = `
                <div class="product-img">
                    <span class="product-tag ${prod.tagClass}">${prod.tag}</span>
                    <img src="${prod.image}" alt="${prod.name}">
                </div>
                <div class="product-info">
                    <span class="product-brand">${prod.brand}</span>
                    <h3 class="product-name">${prod.name}</h3>
                    <ul class="product-specs">
                        ${specsHtml}
                    </ul>
                    <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 20px; line-height: 1.4;">${prod.description}</p>
                    <div class="product-footer">
                        <div>
                            <span class="product-price-label">Soluzione Consigliata</span>
                            <div class="product-price">${prod.price}</div>
                        </div>
                        <a href="${prod.link || '#contatti'}" class="product-btn" aria-label="Vedi dettagli per ${prod.name}">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                        </a>
                    </div>
                </div>
            `;
            resultsGrid.appendChild(card);
        });
    }

    // Trigger filter update on change of any select
    [selectCategoria, selectAnno, selectAlimentazione, selectPortata, selectSollevamento, selectMarca].forEach(select => {
        if (select) {
            select.addEventListener('change', renderProducts);
        }
    });

    if (btnCerca) {
        btnCerca.addEventListener('click', function(e) {
            e.preventDefault();
            renderProducts();
        });
    }

    // Setup initial state
    updateCategoryCounts();
    renderProducts();

    // Expose reset filters globally
    window.resetFilters = function() {
        if (selectCategoria) selectCategoria.value = '';
        if (selectAnno) selectAnno.value = '';
        if (selectAlimentazione) selectAlimentazione.value = '';
        if (selectPortata) selectPortata.value = '';
        if (selectSollevamento) selectSollevamento.value = '';
        if (selectMarca) selectMarca.value = '';
        renderProducts();
    };
}"""

def replace_js_function(content, func_name, new_func_code):
    pattern = r'function\s+' + func_name + r'\s*\('
    match = re.search(pattern, content)
    if not match:
        return content
    
    start_idx = match.start()
    brace_idx = content.find('{', start_idx)
    if brace_idx == -1:
        return content
    
    count = 1
    i = brace_idx + 1
    while count > 0 and i < len(content):
        if content[i] == '{':
            count += 1
        elif content[i] == '}':
            count -= 1
        i += 1
        
    if count == 0:
        return content[:start_idx] + new_func_code + content[i:]
    return content

def update_css():
    paths = [
        r'C:\Users\elly\Local Sites\centrocarrelli\app\public\style.css',
        r'c:\Users\elly\.antigravity\centrocarrelli\style.css'
    ]
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if '/* --- Dropdown Finder Select Styles --- */' in content:
            # Replace existing styles to keep it clean
            pattern = r'/\* --- Dropdown Finder Select Styles ---\s*\*/.*'
            content = re.sub(pattern, SELECTS_CSS.strip(), content, flags=re.DOTALL)
        else:
            content += "\n" + SELECTS_CSS.strip()
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated style.css at {path}")

def update_js_files():
    paths = [
        r'c:\Users\elly\.antigravity\centrocarrelli\app.js',
        r'c:\Users\elly\.antigravity\centrocarrelli\clean_script.js'
    ]
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        content = replace_js_function(content, 'initForkliftFinder', JS_CONTROLLER_CODE)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated JS: {path}")

def update_html_files():
    html_files = [
        r'c:\Users\elly\.antigravity\centrocarrelli\centro2026\index.html',
        r'c:\Users\elly\.antigravity\centrocarrelli\index.html',
        r'c:\Users\elly\.antigravity\centrocarrelli\deploy\index.html',
        r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
    ]
    for path in html_files:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Replace finder-sidebar div
        sidebar = soup.find('div', class_='finder-sidebar')
        if sidebar:
            new_sidebar = BeautifulSoup(SIDEBAR_HTML_CODE, 'html.parser')
            sidebar.replace_with(new_sidebar)
            
        html = str(soup)
        
        # Replace inline initForkliftFinder JS in HTML if present
        html = replace_js_function(html, 'initForkliftFinder', JS_CONTROLLER_CODE)
                
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated HTML: {path}")

if __name__ == '__main__':
    update_css()
    update_js_files()
    update_html_files()
