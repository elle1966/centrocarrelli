# Skill: Fix Accessibilità e Touch Targets (Oxygen Builder + Lighthouse)

Questa skill documenta la soluzione definitiva per risolvere gli errori Lighthouse di accessibilità sui siti costruiti con Oxygen Builder. 

## Il Problema
Oxygen Builder spesso utilizza regole inline con ID specifici e librerie JS (come per slider e paginazioni) che applicano `overflow: hidden` o dimensioni rigide, troncando o nascondendo le hitbox dei link. 
Lighthouse Mobile penalizza pesantemente queste limitazioni (errore: "I touch target non hanno dimensioni o spaziatura sufficienti").
L'approccio tradizionale basato sugli pseudo-elementi (`::after`) spesso fallisce se i contenitori padri hanno `overflow: hidden`.

## La Soluzione Definitiva
L'approccio più sicuro, garantito per essere riconosciuto da Lighthouse PageSpeed, è l'utilizzo di dimensioni fisiche reali combinate con il padding e `box-sizing: border-box !important`, scavalcando i layout di Oxygen.

Inoltre, per risolvere gli errori di Contrasto Cromatico, è necessario mappare gli ID esatti che Oxygen inietta in pagina, poiché hanno una priorità (specificity) maggiore rispetto alle classi generiche come `.cta-button`.

### Codice CSS Universale da Applicare

Da inserire preferibilmente in **WordPress > Aspetto > Personalizza > CSS Aggiuntivo** (per bypassare eventuali blocchi della cache di Oxygen o conflitti con Breeze/Autoptimize).

```css
/* ==========================================================
   FIX ACCESSIBILITÀ: CONTRASTO CROMATICO (Lighthouse)
   ========================================================== */
/* Pulsanti principali e CTA: testo bianco su sfondo accessibile WCAG */
.cta-button,
.ct-link-button.main-button,
#link_button-72-2009,
#link_button-2191-2009,
#link_button-2193-2009 {
    color: #ffffff !important; 
    background-color: #9E5E00 !important;
    font-weight: bold !important;
}

.cta-button:hover,
.ct-link-button.main-button:hover,
#link_button-72-2009:hover,
#link_button-2191-2009:hover,
#link_button-2193-2009:hover {
    background-color: #7A4900 !important;
    text-decoration: none;
}

/* Paginazione: scurire i link solitamente grigio chiaro */
.page-numbers {
    color: #1a1a1a !important;
    font-weight: 600 !important;
}

.page-numbers:hover {
    color: #9E5E00 !important;
    text-decoration: underline;
}

/* Link nei testi e nei titoli delle sezioni */
.ct-section a,
.ct-headline a,
#section-91-2009 a,
#headline-2576-2009-1,
#headline-2576-2009-2,
#headline-2576-2009-3,
#headline-2576-2009-1 a,
#headline-2576-2009-2 a,
#headline-2576-2009-3 a {
    color: #222222 !important;
    font-weight: 600 !important;
    text-decoration: underline;
}

.ct-section a:hover,
.ct-headline a:hover,
#section-91-2009 a:hover {
    color: #9E5E00 !important; 
}

/* ==========================================================
   FIX ACCESSIBILITÀ: TOUCH TARGETS (min 48x48px reali)
   Approccio: padding diretto sull'elemento — Lighthouse
   riconosce solo dimensioni/padding reali, non ::after.
   ========================================================== */

/* --- Link icone e social (desktop + mobile) --- */
#link-678-14992,
#link-964-14992,
.oxy-social-icons-facebook,
.oxy-social-icons-wrapper a,
.ou-ha-button {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-width: 48px !important;
    min-height: 48px !important;
    padding: 10px !important;
    margin: 4px !important;
    box-sizing: border-box !important;
}

/* --- Paginazione --- */
.page-numbers {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-width: 48px !important;
    min-height: 48px !important;
    padding: 10px !important;
    margin: 4px !important;
    box-sizing: border-box !important;
}

/* --- Pallini slider --- */
button[aria-label^="Vai alla slide"] {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-width: 48px !important;
    min-height: 48px !important;
    padding: 14px !important;
    margin: 4px !important;
    box-sizing: border-box !important;
    background-clip: content-box !important;
    cursor: pointer !important;
}
```
