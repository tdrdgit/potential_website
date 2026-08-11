# Potential — website

Sito Potential (*Every space. Delivered.*). Pagine HTML **autonome**: font Plain e loghi sono
incorporati nell'HTML (base64 / SVG inline), quindi ogni pagina funziona da sola, senza dipendenze esterne.

## Pagine

| File | Descrizione |
|------|-------------|
| `index.html` | Landing. Header con **loop push-up** di 16 frame campagna (5s/frame, perpetuo). Multilingua EN/IT/中文/РУС/عربي. Area Riservata (password → portfolio map). |
| `potential-privacy-policy.html` | Privacy Policy (EN). Link di ritorno → `index.html`. |
| `404.html` | Pagina di errore. `noindex, follow`, due sole azioni: home e `mailto:` a info@potential.contractors. |
| `portfolio/potential-portfolio-map.html` | **La pagina dell'area riservata.** I clienti su un radar a 7 assi (i 6 ambiti della home più Office & Corporate). Raggio = fascia luxury del cliente, pallino grigio se il lavoro è passato da un contractor. `noindex`, back → `../index.html`. |
| `costellazione/costellazione.html` | La mappa delle competenze della rete. Generata, vedi sotto. |

La pagina dell'area riservata sta in **`portfolio/`**, la costellazione in **`costellazione/`**:
i link fra loro sono relativi, quindi ogni cartella si sposta **intera** o si rompe. Gli asset
condivisi — favicon, manifest, font, loghi — sono richiamati con path **assoluti** (`/favicon.ico`),
e restano validi a qualsiasi profondità. Per GitHub Pages la home è già `index.html`.

⚠️ `costellazione/` non contiene un `index.html`: l'indirizzo buono è
`/costellazione/costellazione.html` per esteso, e la cartella da sola dà 404. Chi cambia questo
nome deve cambiarlo in tre punti — `publish.sh` nel Brain, l'iframe della home, il link sotto.

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

## L'elenco clienti si rigenera, non si scrive a mano

> Procedura per esteso, con i casi in cui lo script si ferma e cosa vuole:
> [`portfolio/potential-portfolio-map_ISTRUZIONI.md`](portfolio/potential-portfolio-map_ISTRUZIONI.md).

I clienti della portfolio map vengono da **un solo file**:

```
~/Dropbox/CARLO DOCUMENTI MAC/WORK - SUPPLIERS OFFERING/PT-SUPPLIERS PROJECTS LIST.xlsx
foglio "SUPPLIERS PROJECTS"
```

Entrano solo le righe con **`WEBSITE = x`**. Le righe **`RISERVATO`** (ville private) non escono da
quel file: lo script le scarta anche se qualcuno le flagga per sbaglio. Le righe ripetute per località
— Tiffany, Burberry, Hilton — si fondono in un cliente solo, con le località in fila.

```bash
python3 tools/portfolio-data/build.py --check   # dice cosa cambierebbe, non tocca niente
python3 tools/portfolio-data/build.py           # riscrive la pagina
```

Lo script scrive **solo** dentro il blocco `PORTFOLIO-DATA:START … END`: grafica, traduzioni e
motore del radar non li tocca.

⚠️ **La fascia luxury non la decide lo script.** Sta in `tools/portfolio-data/tiers.json` (1 mass
market → 5 ultra luxury) e vale il posizionamento del *marchio del cliente*, non la dimensione della
commessa. Quando l'Excel porta un cliente nuovo, il build **si ferma e lo elenca**: la fascia va
assegnata a mano, e solo dopo la pagina si rigenera.

Il colore del pallino invece è automatico: la colonna `CONTRACTOR` diventa il `· for …` in coda al
dettaglio, e quel `for` è ciò che rende il pallino grigio invece che rosso.

## La costellazione (`costellazione/`)

> Procedura per esteso in `tools/editor-costellazione/editor_costellazione_ISTRUZIONI.md`, che
> sta accanto all'editor e quindi — come l'editor — **non è in questo repository**: è sul Mac di
> Carlo, in Dropbox.

`costellazione/costellazione.html` è la mappa delle competenze della rete di fornitura, quella che
si vede a https://potential.contractors/costellazione/costellazione.html e, in iframe, nella
sezione nera della home. **Una sola pagina per due posti**: la home la incorpora con
`costellazione/costellazione.html?embed=1`, non ne tiene una copia.

⚠️ **I due file in `costellazione/` sono generati.** I sorgenti vivono nel Brain, in
`COMPANY BRAIN/POTENTIAL BRAIN/suppliers database/public/`, e `publish.sh` sovrascrive questa
cartella a ogni pubblicazione ripartendo da `origin/main`: quello che si edita qui a mano sparisce
alla prima ripubblicazione, senza lasciare traccia. Vale anche per le favicon — vanno aggiunte al
sorgente nel Brain, non alla copia pubblicata.

Per cambiare i testi, aggiungere o togliere nodi si usa l'**editor**, che sta in
`tools/editor-costellazione/` e non è in questo repo perché è uno strumento interno (è in
`.gitignore`, sta solo sul Mac). In `costellazione/` resta solo quello che il sito pubblica:

```bash
open tools/editor-costellazione/apri-editor.command     # doppio click dal Finder
```

Scrive su `suppliers database/taxonomy/`. Poi, per portare online:

```bash
python3 "suppliers database/scripts/refresh.py"    # rigenera public/network.json
sh "suppliers database/scripts/publish.sh"         # commit e push su questo repo
```

Lingue della mappa: **italiano e inglese**, con l'inglese come ripiego per le altre lingue del
sito. Islandese e arabo restano tradotti nei sorgenti ma non escono più nel file pubblico.

## Anteprima locale

```bash
python3 -m http.server 8080
# apri http://localhost:8080/index.html
```

## Deploy

Repo pubblico. Per pubblicare: `git push` (vedi nota auth sotto), poi eventualmente attivare
GitHub Pages (Settings → Pages → branch `main`).
