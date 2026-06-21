## Navigation Rules
- **Never add a "Home" link in the navigation menu.** The logo already links to the homepage. Adding a Home link is redundant.

## Footer Rules
- **Always use this exact footer structure with all 7 links, in this order:** News, Newsletter, Privacy, Mappa sito, Cookie, Contatti, Lavora con noi.
- Footer links: `/news/`, `/newsletter/`, `/privacy-policy/`, `/mappa-sito/`, `/cookie-policy/`, `/contatti/`, `/lavora-con-noi/`

## Data Integrity Rules
- **Never invent product data, technical specifications, serial numbers, or product listings.**
- Always extract and display real product listings and real attributes from the official database or website (e.g. Marca, Modello, Matricola, Anno fabbricazione, Alimentazione, Portata, Sollevamento mm).

## YouTube Automation Rules (Garden Friends)
- **Script base path**: `D:\video_progetti\execution\`
- **Profilo Chrome persistente**: `C:\Users\elly\.antigravity\agente magico\yt_user_profile`
- **Prima di qualsiasi operazione YouTube**, verifica che la sessione Google sia valida. Se scaduta, chiedi all'utente di lanciare `D:\video_progetti\00_EFFETTUA_LOGIN_YOUTUBE.bat` (login interattivo con 2FA).
- **Canale**: Garden Friends (`UCOq2OCN5tRi5ujvG6QjNaaw`). Usa sempre `channel_guard.verify_garden_friends_or_die()` ma cattura `SystemExit` per non bloccare il processo.
- **Autopubblicazione YouTube**: I video da caricare vanno in `D:\video_progetti\output\autopubblicazione youtube\`. Dopo il caricamento, spostarli in `caricati\`.
- **Dirette programmate**: Stato in `execution\stato_programmazione_30g.json`. Attivare sempre **Avvio automatico** e **Interruzione automatica** su ogni diretta. Script: `fix_all_upcoming_lives.py`.
- **Cat TV upload**: Script `carica_cat_tv_youtube.py`. Batch: `CARICA_CAT_TV_*.bat`.
- **Programmazione video**: 3-4 video/giorno, orari ~12:00, ~16:00, ~20:00. Log in `LOG_UPLOAD_PROGRAMMATI.txt`.
- **Avvisare l'utente** quando i contenuti programmati stanno per finire (meno di 3 giorni di scorta).

---

## Centro Carrelli — Stato Progetto (aggiornato 21/06/2026 ore 01:34)

### Deployment
- **URL preview**: https://centrocarrelli-preview-435.netlify.app
- **Deploy comando**: `npx -y netlify-cli deploy --prod --dir="."` dalla cartella `c:\Users\elly\.antigravity\centrocarrelli\`
- **Netlify account**: `6a3182ad90f37aa75fba0211`

### File principali
- `index.html` — struttura pagina, nav, hero, info-strip, finder widget, footer
- `style.css` — design system, CSS tokens, layout
- `app.js` — logica finder, filtri, ricerca libera, animazioni scroll, modal prodotti
- `assets/` — tutte le immagini locali (NON usare URL esterne da centrocarrelli.net → bloccano il hotlinking)
- `centro2026.zip` — ZIP di riferimento con assets originali

### Architettura CSS / Animazioni — CRITICO
- `animate-on-scroll` e `reveal-section` partono con `opacity:0` via JS dinamico.
- C'è un override **in fondo a `style.css`** che forza tutto a `opacity:1 !important`. **NON RIMUOVERE MAI questo override** o la pagina diventa bianca al 100% zoom.
- `scroll-padding-top: 90px` su `html` — compensa l'header fisso per anchor links (#finder etc.)
- Hero: `min-height: auto` — NON usare `100vh` (coprirebbe tutto lo schermo)
- Finder section: `padding: 50px 0`
- IntersectionObserver threshold: `0.02` (era 0.15, troppo alto)

### Nav Menu — Funzionamento
- Carrelli Frontali → `href="#finder" data-categoria="frontali"` — filtra finder + scroll
- Carrelli Magazzino → `href="#finder" data-categoria="magazzino"` — filtra finder + scroll
- Transpallet → `href="#finder" data-categoria="transpallet"` — filtra finder + scroll
- Occasioni → `href="#finder" data-categoria="occasioni"` — filtra finder + scroll
- Noleggio, Azienda, Assistenza, Contatti → `href="https://www.centrocarrelli.net/..."` con `target="_blank" rel="noopener"`
- **NON aggiungere "Home"** — il logo collega già alla home
- **La sezione "Promozioni" è stata ELIMINATA** — non ripristinarla

### Finder / Ricerca Libera
- Campo: `input#filter-search` in `index.html` riga ~127
- Listener: `input` + `keyup` con debounce 250ms → chiama `renderProducts()`
- Cerca in: name, brand, description, specs.marca, specs.modello, specs.matricola
- Reset filtri: `window.resetFilters()` — resetta anche il campo ricerca libera

### Immagini Prodotti — TUTTE LOCALI in `/assets/`
| File locale | Prodotto |
|---|---|
| `ech12c_still.jpg` | STILL ECH 12 C |
| `ech15c_still.jpg` | STILL ECH 15 C |
| `exh14c_transpallet.png` | STILL EXH 14 C |
| `ecu16_usato.jpg` | STILL ECU 16 |
| `still_rx6050.jpg` | STILL RX 60-50 + **STILL RX 70-25** (fallback, 404) |
| `still_rx6030.jpg` | STILL RX 60-30 + **LUGLI ELX 30** (fallback, 404) |
| `still_rx6030l.jpg` | STILL RX 60-30 L/600 |
| `still_rx6025.jpg` | STILL RX 60-25 |
| `still_rx2020.jpg` | STILL RX 20-20 |
| `still_rx2018.jpg` | STILL RX 20-18 |
| `still_rx2018p.jpg` | STILL RX 20-18 P |
| `still_rx2016p.jpg` | STILL RX 20-16 P |
| `still_rx2016c.jpg` | STILL RX 20-16 C |
| `still_r6025.jpg` | STILL R 60-25 |
| `still_exv20.jpg` | STILL EXV 20 |
| `still_exv12a.jpg` | STILL EXV 12 (2018) |
| `still_exv12b.jpg` | STILL EXV 12 (2019) |
| `still_exv14a.jpg` | STILL EXV 14 (prima) |
| `still_exv14b.jpg` | STILL EXV 14 (seconda) |
| `still_exv14c.jpg` | STILL EXV 14 (terza) |
| `still_exhsf20.webp` | STILL EXH SF 20 |
| `still_exh16.jpg` | STILL EXH 16 |
| `service_van.png` | Furgone hero (v1 — sede rosa, furgone bianco Centro Carrelli) |
| `hero_forklift.png` | Carrello STILL arancione hero |

### Backlog da fare
- [ ] Trovare URL immagini corrette per LUGLI ELX 30 e STILL RX 70-25 su centrocarrelli.net
- [ ] Verificare dove `service_van.png` viene referenziato in `index.html`
- [ ] Richiesta "ristrutturare il muretto dietro al camion" — pendente
