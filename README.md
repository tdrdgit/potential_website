# Potential — website

Sito Potential (*Every space. Delivered.*). Tre pagine HTML **autonome**: font Plain e loghi sono
incorporati nell'HTML (base64 / SVG inline), quindi ogni pagina funziona da sola, senza dipendenze esterne.

## Pagine

| File | Descrizione |
|------|-------------|
| `index.html` | Landing. Header con **loop push-up** di 16 frame campagna (5s/frame, perpetuo). Multilingua EN/IT/中文/РУС/عربي. Area Riservata (password → carousel). |
| `potential-privacy-policy.html` | Privacy Policy (EN). Link di ritorno → `index.html`. |
| `potential-carousel.html` | Carousel area riservata. Back → `index.html` (relativo). |

I link interni sono **relativi**, quindi le tre pagine vanno tenute nella stessa cartella sul server.
Per GitHub Pages la home è già `index.html`.

## Sorgenti (`assets/`)

- `assets/logos/` — loghi ufficiali Potential (SVG, non modificare).
- `assets/header/` — i 16 frame dell'header `CAMP_00..15.svg` (850×551). Sequenza: **logo · claim · claim** che si ripete; i frame 00/03/06/09/12/15 sono il logo.
- `assets/fonts/` — font **Plain (Optimo)**, pesi Thin/Light/Medium. È incorporato nell'HTML per il rendering; i `.otf` sono inclusi qui come sorgente.

> **Nota licenza font:** Plain (Optimo) è un font commerciale su licenza. I `.otf` sono inclusi nel repo
> su scelta esplicita del titolare del progetto, che si assume la responsabilità della distribuzione.

## Rigenerare i frame dell'header

Se aggiorni gli SVG in `assets/header/` (stessi nomi `CAMP_XX.svg`):

```bash
python3 tools/build-header-frames.py
```

Lo script re-incorpora i frame (base64) dentro `index.html`. Le slide restano identiche: cambia solo
cosa mostra il loop. Timing (5s) e transizione (push-up) sono nel motore `HEADER LOOP` in fondo a `index.html`.

## Anteprima locale

```bash
python3 -m http.server 8080
# apri http://localhost:8080/index.html
```

## Deploy

Repo pubblico. Per pubblicare: `git push` (vedi nota auth sotto), poi eventualmente attivare
GitHub Pages (Settings → Pages → branch `main`).
