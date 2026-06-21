import os
import re
from bs4 import BeautifulSoup

PRODUCTS_CODE = """const PRODUCTS = [
    // --- PROMOZIONI (TRANSPALLET NUOVI) ---
    {
        id: 'ech12c',
        name: 'STILL ECH 12 C',
        brand: 'Transpallet Elettrico',
        image: '/assets/ech12c_still.jpg',
        tag: 'Promo',
        tagClass: 'litio',
        link: '/ech12c.html',
        isOccasione: false,
        specs: {
            marca: 'STILL',
            modello: 'ECH 12 C',
            matricola: 'Promo',
            anno: '2026',
            alimentazione: 'Ioni di Litio',
            portata: '1200 kg',
            altezza: '115 mm',
            tipologia: 'transpallet'
        },
        description: 'Compatto e agile per corridoi stretti. Batteria Li-Ion estraibile a ricarica rapida. Ideale per negozi e magazzini.',
        price: '€ 1.150,00'
    },
    {
        id: 'ech15c',
        name: 'STILL ECH 15 C',
        brand: 'Transpallet Elettrico',
        image: '/assets/ech15c_still.jpg',
        tag: 'Promo',
        tagClass: 'litio',
        link: '/ech15c.html',
        isOccasione: false,
        specs: {
            marca: 'STILL',
            modello: 'ECH 15 C',
            matricola: 'Promo',
            anno: '2026',
            alimentazione: 'Ioni di Litio',
            portata: '1500 kg',
            altezza: '115 mm',
            tipologia: 'transpallet'
        },
        description: 'Portata maggiore per carichi più impegnativi. Batteria Li-Ion estraibile, perfetto per magazzini e centri logistici.',
        price: '€ 1.350,00'
    },
    {
        id: 'exh14c',
        name: 'STILL EXH 14 C',
        brand: 'Transpallet Elettrico',
        image: '/assets/exh14c_transpallet.png',
        tag: 'Nuovo',
        tagClass: 'litio',
        link: '/exh14c.html',
        isOccasione: false,
        specs: {
            marca: 'STILL',
            modello: 'EXH 14 C',
            matricola: 'Nuovo',
            anno: '2026',
            alimentazione: 'Ioni di Litio',
            portata: '1400 kg',
            altezza: '115 mm',
            tipologia: 'transpallet'
        },
        description: 'Transpallet compatto e maneggevole con timone STILL e display LED integrato. Batteria Li-Ion 48V ricaricabile ovunque.',
        price: '€ 1.890,00'
    },
    {
        id: 'ecu16',
        name: 'STILL ECU 16',
        brand: 'Transpallet Elettrico — Usato',
        image: '/assets/ecu16_usato.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: '/ecu16.html',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'ECU 16',
            matricola: 'Usato',
            anno: '2018',
            alimentazione: 'Elettrico',
            portata: '1600 kg',
            altezza: '115 mm',
            tipologia: 'transpallet'
        },
        description: 'Usato ricondizionato con batteria 24V/150Ah e caricabatterie incorporato. Revisionato e pronto alla consegna immediata.',
        price: '€ 1.200,00'
    },
    // --- CARRELLI FRONTALI ---
    {
        id: '51602312050',
        name: 'STILL R 60-25',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/CARRELLO-ELEVATORE-ELETTRICO-STILL-R-60-25-3.jpg',
        tag: 'Usato Garantito',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-r-60-25/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'R 60-25',
            matricola: '51602312050',
            anno: '2000',
            alimentazione: 'Elettrico',
            portata: '2500 kg',
            altezza: '4200 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello elevatore frontale elettrico STILL R 60-25, portata 2.5 t, altezza sollevamento 4.2 m. Affidabile ed economico.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516329X00218',
        name: 'STILL RX 60-50',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-60-50-3.jpg',
        tag: 'Grandi Carichi',
        tagClass: 'bestseller',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-60-50-3/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 60-50',
            matricola: '516329X00218',
            anno: '2020',
            alimentazione: 'Elettrico',
            portata: '5000 kg',
            altezza: '4630 mm',
            tipologia: 'frontali'
        },
        description: 'Potente carrello elettrico STILL RX 60-50 per carichi pesanti fino a 5 tonnellate. Modello recente del 2020 in ottime condizioni.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516308X00119',
        name: 'STILL RX 60-30 L/600',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-60-30L-600-3.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-still-rx-60-30-l-600/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 60-30 L / 600',
            matricola: '516308X00119',
            anno: '2020',
            alimentazione: 'Elettrico',
            portata: '3000 kg',
            altezza: '5540 mm',
            tipologia: 'frontali'
        },
        description: 'Versione con baricentro allungato a 600mm. Portata 3.0 t, sollevamento 5.5 m. Ideale per carichi voluminosi.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516353H00240',
        name: 'STILL RX 60-30',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-60-30-3.jpg',
        tag: 'Bestseller',
        tagClass: 'bestseller',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-still-rx-60-30/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 60-30',
            matricola: '516353H00240',
            anno: '2017',
            alimentazione: 'Elettrico',
            portata: '3000 kg',
            altezza: '4170 mm',
            tipologia: 'frontali'
        },
        description: 'Uno dei modelli più apprezzati della gamma STILL. Portata 3.0 t, altezza sollevamento 4.17 m. Perfetto bilanciamento tra potenza e agilità.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516301X00877',
        name: 'STILL RX 60-25',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-60-25-2.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-60-25-8/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 60-25',
            matricola: '516301X00877',
            anno: '2020',
            alimentazione: 'Elettrico',
            portata: '2500 kg',
            altezza: '4890 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello elevatore frontale elettrico STILL RX 60-25, portata 2.5 t, altezza sollevamento 4.89 m. Batteria efficiente.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516215H01190',
        name: 'STILL RX 20-20',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-20-20-3.jpg',
        tag: 'Agile',
        tagClass: 'bestseller',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-20-4/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 20-20',
            matricola: '516215H01190',
            anno: '2017',
            alimentazione: 'Elettrico',
            portata: '2000 kg',
            altezza: '4765 mm',
            tipologia: 'frontali'
        },
        description: 'Straordinariamente agile e compatto, ideale per lavorare in corsie e spazi ristretti con portata di 2.0 t.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516226X00036',
        name: 'STILL RX 20-18 P',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-18-P-3.jpg',
        tag: 'Nuovo Arrivo',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-18-p/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 20-18 P',
            matricola: '516226X00036',
            anno: '2020',
            alimentazione: 'Elettrico',
            portata: '1800 kg',
            altezza: '5070 mm',
            tipologia: 'frontali'
        },
        description: 'Modello a 4 ruote con ottima stabilità e precisione millimetrica. Portata 1.8 t, sollevamento 5.07 m.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516223V01032',
        name: 'STILL RX 20-18',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-18-4.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-18-13/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 20-18',
            matricola: '516223V01032',
            anno: '2019',
            alimentazione: 'Elettrico',
            portata: '1800 kg',
            altezza: '4770 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello frontale elettrico STILL RX 20-18, portata 1.8 t, altezza sollevamento 4.77 m, anno 2019.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516226Y00057',
        name: 'STILL RX 20-16 P',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-STILL-RX-20-26-P-2.jpg',
        tag: 'Compatto',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-16-p/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 20-16 P',
            matricola: '516226Y00057',
            anno: '2021',
            alimentazione: 'Elettrico',
            portata: '1600 kg',
            altezza: '4620 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello frontale a 4 ruote compatto STILL RX 20-16 P, anno 2021, portata 1.6 t. Ideale per carico/scarico merci.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '516220Y00150',
        name: 'STILL RX 20-16 C',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-STILL-RX-20-16-C-3.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-still-rx-20-16-c/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 20-16 C',
            matricola: '516220Y00150',
            anno: '2021',
            alimentazione: 'Elettrico',
            portata: '1600 kg',
            altezza: '5220 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello frontale a 3 ruote compatto STILL RX 20-16 C, portata 1.6 t, sollevamento 5.22 m.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '517395Y00166',
        name: 'STILL RX 70-25',
        brand: 'Carrello Elevatore Frontale Diesel',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-DIESEL-STILL-RX-70-25-2.jpg',
        tag: 'Diesel',
        tagClass: 'termico',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-diesel-still-rx-70-25-2/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'RX 70-25',
            matricola: '517395Y00166',
            anno: '2022',
            alimentazione: 'diesel',
            portata: '2500 kg',
            altezza: '7390 mm',
            tipologia: 'frontali'
        },
        description: 'Potente carrello frontale diesel del 2022. Portata 2.5 t, sollevamento eccezionale a 7.39 m per uso esterno.',
        price: 'Noleggio o Vendita'
    },
    {
        id: '5342201084',
        name: 'LUGLI ELX 30',
        brand: 'Carrello Elevatore Frontale',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/FRONTALE-ELETTRICO-LUGLI-ELX-30-3.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/frontale-elettrico-lugli-elx-30/',
        isOccasione: true,
        specs: {
            marca: 'LUGLI',
            modello: 'ELX 30',
            matricola: '5342201084',
            anno: '2002',
            alimentazione: 'Elettrico',
            portata: '3000 kg',
            altezza: '4000 mm',
            tipologia: 'frontali'
        },
        description: 'Carrello elevatore elettrico LUGLI ELX 30, robusto e affidabile, portata 3.0 t, altezza sollevamento 4.0 m.',
        price: 'Noleggio o Vendita'
    },
    // --- CARRELLI MAGAZZINO ---
    {
        id: 'F22551N01051',
        name: 'STILL EXV 20',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/04/SOLLEVATORE-ELETTRICO-STILL-EXV-20.jpg',
        tag: 'Alta Portata',
        tagClass: 'bestseller',
        link: 'https://www.centrocarrelli.net/carrelli/sollevatore-elettrico-still-exv-20/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 20',
            matricola: 'F22551N01051',
            anno: '2024',
            alimentazione: 'Elettrico',
            portata: '2000 kg',
            altezza: '3170 mm',
            tipologia: 'magazzino'
        },
        description: 'Sollevatore a timone STILL EXV 20, anno 2024, portata 2.0 t, sollevamento 3.17 m. Praticamente nuovo.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'F20272J01779',
        name: 'STILL EXV 12',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-ELETTRICO-STILL-EXV-12-3.jpg',
        tag: 'Compatto',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-12/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 12',
            matricola: 'F20272J01779',
            anno: '2018',
            alimentazione: 'Elettrico',
            portata: '1200 kg',
            altezza: '4386 mm',
            tipologia: 'magazzino'
        },
        description: 'Sollevatore a colonna compatto STILL EXV 12, portata 1.2 t, altezza sollevamento 4.38 m. Facile da manovrare.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'F20323H00792',
        name: 'STILL EXV 14',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-STILL-EXV-14-2-1.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-14-3/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 14',
            matricola: 'F20323H00792',
            anno: '2017',
            alimentazione: 'Elettrico',
            portata: '1400 kg',
            altezza: '4800 mm',
            tipologia: 'magazzino'
        },
        description: 'Stoccatore elettrico STILL EXV 14, portata 1.4 t, altezza sollevamento 4.8 m. Perfetto per magazzinaggio intensivo.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'F20323H00773',
        name: 'STILL EXV 14',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/SOLLEVATORE-STILL-EXV-14-3.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/stoccatore-elettrico-still-exv-14-2/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 14',
            matricola: 'F20323H00773',
            anno: '2017',
            alimentazione: 'Elettrico',
            portata: '1400 kg',
            altezza: '4350 mm',
            tipologia: 'magazzino'
        },
        description: 'Stoccatore elettrico STILL EXV 14, portata 1.4 t, altezza sollevamento 4.35 m.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'F20323H00763',
        name: 'STILL EXV 14',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2025/11/SOLLEVATORE-STILL-EXV-14-2.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/still-exv-14-sollevatore-a-colonna/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 14',
            matricola: 'F20323H00763',
            anno: '2017',
            alimentazione: 'Elettrico',
            portata: '1400 kg',
            altezza: '4266 mm',
            tipologia: 'magazzino'
        },
        description: 'Stoccatore elettrico STILL EXV 14, portata 1.4 t, altezza sollevamento 4.26 m.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'F20272V00365',
        name: 'STILL EXV 12',
        brand: 'Stoccatore Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2025/11/TRANSPALLET-STILL-EXV-12-2.jpg',
        tag: 'Usato',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/still-exv-12-transpallet-a-colonna/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXV 12',
            matricola: 'F20272V00365-V00387-V00399',
            anno: '2019',
            alimentazione: 'Elettrico',
            portata: '1200 kg',
            altezza: '4386 mm',
            tipologia: 'magazzino'
        },
        description: 'Stoccatore a colonna STILL EXV 12, portata 1.2 t, altezza sollevamento 4.38 m, anno 2019.',
        price: 'Noleggio o Vendita'
    },
    // --- TRANSPALLET ---
    {
        id: 'W42362X01206',
        name: 'STILL EXH SF 20',
        brand: 'Transpallet Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2026/03/TRANSPALLET-ELETTRICO-STILL-EXH-SF-20.webp',
        tag: 'Pedana Operatore',
        tagClass: 'bestseller',
        link: 'https://www.centrocarrelli.net/carrelli/transpallet-elettrico-still-exh-sf-20/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXH SF 20',
            matricola: 'W42362X01206',
            anno: '2020',
            alimentazione: 'Elettrico',
            portata: '2000 kg',
            altezza: '200 mm',
            tipologia: 'transpallet'
        },
        description: 'Transpallet elettrico STILL EXH SF 20 con pedana ribaltabile per operatore a bordo. Portata 2.0 t, perfetto per lunghi tragitti.',
        price: 'Noleggio o Vendita'
    },
    {
        id: 'W42031P00027',
        name: 'STILL EXH 16',
        brand: 'Transpallet Elettrico',
        image: 'https://www.centrocarrelli.net/wp-content/uploads/2025/11/STILL-EXH-16-2.jpg',
        tag: 'Usato Recente',
        tagClass: 'usato',
        link: 'https://www.centrocarrelli.net/carrelli/still-exh-16-transpallet-elettrico/',
        isOccasione: true,
        specs: {
            marca: 'STILL',
            modello: 'EXH 16',
            matricola: 'W42031P00027',
            anno: '2025',
            alimentazione: 'Elettrico',
            portata: '1600 kg',
            altezza: '200 mm',
            tipologia: 'transpallet'
        },
        description: 'Transpallet elettrico compatto STILL EXH 16, portata 1.6 t. Modello del 2025 in condizioni eccellenti.',
        price: 'Noleggio o Vendita'
    }
];"""

JS_LOGIC_CODE = """
function initForkliftFinder() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const resultsGrid = document.getElementById('results-grid');
    const resultsCount = document.getElementById('results-count');

    if (!resultsGrid) return;

    // Track active filters
    const activeFilters = {
        tipologia: 'tutti',
        portata: 'tutti',
        alimentazione: 'tutti'
    };

    // Filter button click handler
    filterButtons.forEach(button => {
        const input = button.querySelector('input');
        if (!input) return;
        
        button.addEventListener('click', function(e) {
            const group = input.name; // 'tipologia', 'portata', 'alimentazione'
            const value = input.value;

            // Remove active class from sibling buttons in this group
            document.querySelectorAll(`.filter-btn input[name="${group}"]`).forEach(siblingInput => {
                siblingInput.parentElement.classList.remove('active');
            });

            // Set active class and value
            this.classList.add('active');
            input.checked = true;
            activeFilters[group] = value;

            // Render filtered products
            renderProducts();
        });
    });

    // Initial render
    renderProducts();

    function renderProducts() {
        // Filter products logic
        const filtered = PRODUCTS.filter(prod => {
            // Match tipologia
            let matchTipologia = false;
            if (activeFilters.tipologia === 'tutti') {
                matchTipologia = true;
            } else if (activeFilters.tipologia === 'occasioni') {
                matchTipologia = prod.isOccasione === true;
            } else {
                matchTipologia = prod.specs.tipologia === activeFilters.tipologia;
            }
            
            // Match portata
            let matchPortata = true;
            if (activeFilters.portata !== 'tutti') {
                const portataVal = parseFloat(prod.specs.portata);
                if (activeFilters.portata === '1500') {
                    matchPortata = portataVal <= 1500;
                } else if (activeFilters.portata === '2500') {
                    matchPortata = portataVal > 1500 && portataVal <= 2500;
                } else if (activeFilters.portata === 'grandi') {
                    matchPortata = portataVal > 2500;
                }
            }

            // Match alimentazione
            let matchAlimentazione = true;
            if (activeFilters.alimentazione !== 'tutti') {
                const alim = prod.specs.alimentazione.toLowerCase();
                if (activeFilters.alimentazione === 'diesel') {
                    matchAlimentazione = alim === 'diesel' || alim === 'gpl';
                } else if (activeFilters.alimentazione === 'elettrico') {
                    matchAlimentazione = alim === 'elettrico' || alim.includes('litio');
                }
            }

            return matchTipologia && matchPortata && matchAlimentazione;
        });

        // Update count text
        resultsCount.textContent = `${filtered.length} Carrell${filtered.length === 1 ? 'o Trovato' : 'i Trovati'}`;

        // Clear grid
        resultsGrid.innerHTML = '';

        if (filtered.length === 0) {
            resultsGrid.innerHTML = `
                <div class="empty-state">
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
            
            // Generate specifications HTML list dynamically
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
                        <a href="${prod.link || '#contatti'}" class="product-btn" aria-label="${prod.link ? 'Vedi dettagli' : 'Richiedi informazioni'} per ${prod.name}">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                        </a>
                    </div>
                </div>
            `;
            resultsGrid.appendChild(card);
        });
    }

    // Expose reset filters globally
    window.resetFilters = function() {
        const defaults = {
            tipologia: 'tutti',
            portata: 'tutti',
            alimentazione: 'tutti'
        };

        Object.keys(defaults).forEach(group => {
            const val = defaults[group];
            const btn = document.querySelector(`.filter-btn input[name="${group}"][value="${val}"]`).parentElement;
            
            document.querySelectorAll(`.filter-btn input[name="${group}"]`).forEach(sib => {
                sib.parentElement.classList.remove('active');
            });
            
            btn.classList.add('active');
            btn.querySelector('input').checked = true;
            activeFilters[group] = val;
        });

        renderProducts();
    };
}
"""

SIDEBAR_HTML_CODE = """<div class="finder-sidebar">
<h3>Filtri di Ricerca</h3>
<p>Modifica le impostazioni per filtrare i mezzi consigliati.</p>
<div class="filter-group">
<span class="filter-label">1. Tipologia di Mezzo</span>
<div class="filter-options">
<label class="filter-btn active">
<input checked="" name="tipologia" type="radio" value="tutti"/>
                                Tutti i Mezzi
                            </label>
<label class="filter-btn">
<input name="tipologia" type="radio" value="frontali"/>
                                Carrelli Frontali
                            </label>
<label class="filter-btn">
<input name="tipologia" type="radio" value="magazzino"/>
                                Carrelli Magazzino
                            </label>
<label class="filter-btn">
<input name="tipologia" type="radio" value="transpallet"/>
                                Transpallet
                            </label>
<label class="filter-btn">
<input name="tipologia" type="radio" value="occasioni"/>
                                Occasioni
                            </label>
</div>
</div>
<div class="filter-group">
<span class="filter-label">2. Portata Massima</span>
<div class="filter-options">
<label class="filter-btn active">
<input checked="" name="portata" type="radio" value="tutti"/>
                                Tutte le Portate
                            </label>
<label class="filter-btn">
<input name="portata" type="radio" value="1500"/>
                                Fino a 1.500 kg
                            </label>
<label class="filter-btn">
<input name="portata" type="radio" value="2500"/>
                                Da 1.500 a 2.500 kg
                            </label>
<label class="filter-btn">
<input name="portata" type="radio" value="grandi"/>
                                Oltre 2.500 kg
                            </label>
</div>
</div>
<div class="filter-group">
<span class="filter-label">3. Alimentazione</span>
<div class="filter-options">
<label class="filter-btn active">
<input checked="" name="alimentazione" type="radio" value="tutti"/>
                                Tutte
                            </label>
<label class="filter-btn">
<input name="alimentazione" type="radio" value="elettrico"/>
                                Elettrico (Standard / Litio)
                            </label>
<label class="filter-btn">
<input name="alimentazione" type="radio" value="diesel"/>
                                Diesel / GPL
                            </label>
</div>
</div>
</div>"""

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
            
        # Replace PRODUCTS array
        content = re.sub(r'const PRODUCTS = \[.*?\];', PRODUCTS_CODE, content, flags=re.DOTALL)
        
        # Replace initForkliftFinder function
        start_idx = content.find('function initForkliftFinder()')
        if start_idx != -1:
            end_idx = content.find('function initScrollAnimations()')
            if end_idx != -1:
                content = content[:start_idx] + JS_LOGIC_CODE + '\n\n' + content[end_idx:]
                
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated JS: {path}")

def update_html_files():
    html_files = [
        r'c:\Users\elly\.antigravity\centrocarrelli\centro2026\index.html',
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
            
        # Also replace the inline script block
        scripts = soup.find_all('script')
        for s in scripts:
            if s.string and 'initForkliftFinder' in s.string:
                script_text = s.string
                script_text = re.sub(r'const PRODUCTS = \[.*?\];', PRODUCTS_CODE, script_text, flags=re.DOTALL)
                
                start_idx = script_text.find('function initForkliftFinder()')
                if start_idx != -1:
                    end_idx = script_text.find('function initScrollAnimations()')
                    if end_idx != -1:
                        script_text = script_text[:start_idx] + JS_LOGIC_CODE + '\n\n' + script_text[end_idx:]
                s.string = script_text
                
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated HTML: {path}")

if __name__ == '__main__':
    update_js_files()
    update_html_files()
