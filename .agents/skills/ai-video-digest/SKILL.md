---
name: ai-video-digest
description: >-
  Crea un AI Video Digest giornaliero: cerca i migliori video YouTube su AI,
  agenti autonomi e coding tools, li analizza con spirito critico e pubblica
  un Google Doc formattato con grassetti e link cliccabili.
  Attivare ogni mattina o quando l'utente chiede il digest AI.
---

# AI Video Digest — Workflow

## Obiettivo

Produrre un digest giornaliero dei video YouTube più rilevanti su AI, agenti autonomi e coding tools. Il documento deve essere utile, critico e leggibile.

## Regole di contenuto

### Quantità
- Cercare almeno **12 video**, presentarne almeno **10**
- Dividere in: ⭐ DA GUARDARE (consigliati) e ⏩ MENZIONABILI (non prioritari)

### Filtro qualità
- Preferire video con **>1K views** o da canali verificati/autorevoli
- Video sotto 50 views: includere solo se il contenuto tecnico è eccezionale
- Segnalare sempre le views per dare contesto

### Tono e stile
- **Opinioni dirette**: "da guardare" / "skip" / "interessante ma non verificato"
- **Mai prolisso**: max 5-6 righe per video + bullet points
- **Niente linguaggio corporate vuoto**: no "democratizza", no "importanza strategica critica"
- **Segnalare fatti vs speculazioni**: dire chiaramente cosa è confermato e cosa no
- **Accorpare** video sullo stesso tema in una sola voce

### Struttura per ogni video
1. **Titolo** (grassetto, font 13pt)
2. Canale | durata | views | data
3. 🔗 Link YouTube (cliccabile)
4. 3-5 bullet point con i fatti chiave
5. **"Cosa cambia per te"**: 1 riga concreta e azionabile
6. **Affidabilità**: Alta / Media / Bassa con motivazione

### Sezioni obbligatorie
1. Intestazione con data, numero video, autore
2. Panoramica "Chi comanda" (prospettiva: gli USA sono avanti sull'ecosistema)
3. ⭐ DA GUARDARE (video consigliati con dettagli)
4. ⏩ MENZIONABILI (1-2 righe ciascuno)
5. MAPPA DEL POTERE AI (🇺🇸 USA / 🇨🇳 Cina / 🇪🇺 Europa)
6. AZIONI CONCRETE per la settimana (5 punti max)

## Pubblicazione

### Google Doc
- Creare con `createGoogleDoc` o aggiornare con `updateGoogleDoc`
- ID documento esistente: `1bUQNwyN75hQccfXDQArjObu9Sy4KBo5lVXAF0M0smIg`
- Nome: "AI Video Digest — YYYY-MM-DD"

### Formattazione obbligatoria (dopo la scrittura)
Usare `formatGoogleDocText` per:
- **Titolo principale**: bold, fontSize 20
- **Titoli sezione** (CHI COMANDA, DA GUARDARE, ecc.): bold, fontSize 14
- **Titoli video** (1. Nome video): bold, fontSize 13
- **Link YouTube**: foregroundColor "#1155CC", underline true, linkUrl con URL corretto

### Ricerca video
Fare 2-3 ricerche web con query diverse:
1. `YouTube AI coding agents tools update June YYYY`
2. `YouTube AI news Claude Cursor Devin Codex GPT update new features June YYYY`
3. `YouTube AI video Gemini OpenAI Google Apple agent autonomous latest YYYY`

## Errori da evitare

1. ❌ Muro di testo — max 5-6 righe per video
2. ❌ Tutti i video uguali — filtrare e dare priorità
3. ❌ Link non cliccabili — usare sempre formatGoogleDocText con linkUrl
4. ❌ Niente grassetti — formattare sempre titoli e sezioni
5. ❌ Linguaggio AI generico — essere diretti e concreti
6. ❌ Ignorare le views — sono un indicatore di rilevanza
7. ❌ Trattare speculazioni come fatti — segnalare sempre
