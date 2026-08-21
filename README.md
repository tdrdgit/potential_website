# Potential — website

Sito Potential (*Every space. Delivered.*). Pagine HTML senza build e senza framework: nessuna
libreria, nessun bundler. **Autonome però non lo sono:** i loghi sì, sono SVG inline, ma il font
Plain e i frame dell'header vengono caricati da `assets/`, e una pagina separata da quella cartella
— o con il path scritto male — perde il font.

⚠️ **E dal 17.08.2026 non è più vero che non ci sono servizi esterni**, come diceva questa riga
fino a quel giorno: ogni pagina pubblica carica il beacon di **Cloudflare Web Analytics** da
`static.cloudflareinsights.com`. È una dipendenza sola, cookieless e asincrona, ma è una
dipendenza: chi progetta una pagina nuova non può più dare per scontato che il sito funzioni
offline o a CDN spento.

⚠️ **Il ripiego su Arial è silenzioso, e su un Mac che ha Plain installato nel sistema non si vede
proprio:** il browser pesca il font locale e la pagina sembra giusta a chi la pubblica. I path dei
font si controllano sull'URL vero (`curl -o /dev/null -w "%{http_code}"` sul `.woff2`) o in console
con `[...document.fonts].map(f=>f.family+' '+f.status)`. Le pagine in sottocartella vogliono
`../assets/fonts/`, la home `assets/fonts/`. L'11.08.2026 portfolio map e costellazione servivano
Arial e Helvetica Neue a tutti i visitatori, e dal Mac di casa sembravano perfette.

## Pagine

| File | Descrizione |
|------|-------------|
| `index.html` | Landing. Header con **loop push-up** di 16 frame campagna (5s/frame, perpetuo). Multilingua EN/IT/中文/РУС/عربي. Area Riservata (password → portfolio map). |
| `potential-privacy-policy.html` | Privacy Policy (EN). Link di ritorno → `index.html`. |
| `404.html` | Pagina di errore. `noindex, follow`, due sole azioni: home e `mailto:` a info@potential.contractors. |
| `portfolio/potential-portfolio-map.html` | **La pagina dell'area riservata.** I clienti su un radar a 7 assi (i 6 ambiti della home più Office & Corporate). Distanza dal centro = fascia luxury del cliente (i pallini hanno tutti la stessa dimensione), pallino grigio se il lavoro è passato da un contractor. `noindex`, back → `../index.html`. |
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
- `assets/fonts/` — font **Plain (Optimo)**, pesi Thin/Light/Medium. Le pagine lo **caricano da qui** via `@font-face` (`.woff2`, con l'`.otf` come ripiego): non è incorporato in nessun HTML, quindi questa cartella serve al sito in esercizio, non è solo un archivio di sorgenti.

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
> `portfolio/potential-portfolio-map_ISTRUZIONI.md` — **sul Mac, non nel repo**
> (vedi «Cosa non sta su GitHub» in fondo).

I clienti della portfolio map vengono da **un solo file**: un Excel che vive **fuori da questo
repository**, sul Mac. Dove sta esattamente e come è fatto lo dicono le istruzioni della portfolio
map, che non sono pubblicate — vedi «Cosa non sta su GitHub» in fondo.

Entrano solo le righe con **`WEBSITE = x`**. Le righe **`RISERVATO`** (ville private) non escono da
quel file: lo script le scarta anche se qualcuno le flagga per sbaglio. Le righe ripetute per località
— Tiffany, Burberry, Hilton — si fondono in un cliente solo, con le località in fila.

```bash
python3 projects/suppliers-radar/scripts/build.py --check   # dice cosa cambierebbe, non tocca niente
python3 projects/suppliers-radar/scripts/build.py           # riscrive la pagina
```

Lo script scrive **solo** dentro il blocco `PORTFOLIO-DATA:START … END`: grafica, traduzioni e
motore del radar non li tocca.

⚠️ **La posizione di un cliente sul radar non la decide lo script.** Viene da un file di
configurazione che sta fuori dal repository, e il criterio è documentato nelle istruzioni, sul Mac.
Quando l'Excel porta un cliente nuovo, il build **si ferma e lo elenca**: il valore va assegnato a
mano, e solo dopo la pagina si rigenera.

Il colore del pallino invece è automatico: la colonna `CONTRACTOR` diventa il flag `v:1`, e quel
flag è ciò che rende il pallino grigio invece che rosso. **Il nome del contractor non esce dal
file Excel** — fino all'11.08.2026 finiva in coda al dettaglio come `· for …`.

## La costellazione (`costellazione/`)

> Procedura per esteso, con i casi in cui il build si ferma e cosa vuole:
> `projects/suppliers-costellazione/LEGGIMI-dataset.md` — **sul Mac, non nel repo**
> (vedi «Cosa non sta su GitHub» in fondo).

`costellazione/costellazione.html` è la mappa delle competenze della rete di fornitura, quella che
si vede a https://potential.contractors/costellazione/costellazione.html e, in iframe, nella
sezione nera della home. **Una sola pagina per due posti**: la home la incorpora con
`costellazione/costellazione.html?embed=1`, non ne tiene una copia.

⚠️ **I due file in `costellazione/` sono generati.** I sorgenti vivono fuori da questo
repository, e `publish.sh` sovrascrive questa
cartella a ogni pubblicazione ripartendo da `origin/main`: quello che si edita qui a mano sparisce
alla prima ripubblicazione, senza lasciare traccia. Vale anche per le favicon — vanno aggiunte al
sorgente nel Brain, non alla copia pubblicata.

Per cambiare i testi, aggiungere o togliere nodi si edita **un Excel**, che dall'11.08.2026 è la
fonte unica dello strato editoriale — struttura, settori, cartelle, testi nelle quattro lingue:

```
projects/suppliers-costellazione/dati/costellazione-dataset.xlsx     ← in .gitignore: è la fonte, non esce su GitHub
```

```bash
python3 projects/suppliers-costellazione/scripts/build_dataset.py --check   # dice cosa cambierebbe, non tocca niente
python3 projects/suppliers-costellazione/scripts/build_dataset.py           # riscrive i tre json nel Brain
sh "projects/suppliers_database/scripts/publish.sh"          # rigenera network.json, commit e push
git pull                                            # ⚠️ il repo resta indietro di un commit
```

`--status` dice dove si è fermata la catena. Non serve lanciarlo: un hook `SessionStart` lo
esegue a ogni apertura di Claude Code in questa cartella e **parla solo se qualcosa è
disallineato** — una modifica in Excel mai pubblicata non dà errore, dà un sito fermo.

⚠️ **L'Excel non decide la dimensione dei nodi**: il peso viene dal conteggio delle cartelle
dell'archivio fornitori, compresso in cinque gradini perché non sia leggibile a ritroso. E
**l'ordine delle righe è l'ordine dei nodi sul grafo** — la colonna `ord` serve a rimettere il
foglio com'era dopo averlo riordinato per lavorarci.

L'**editor visuale** in `projects/suppliers-costellazione/editor/` (gitignored, solo sul Mac) è ancora al suo
posto e scrive sugli stessi tre file. **Si usa uno solo dei due**: l'ultimo che salva cancella il
lavoro dell'altro senza dirlo. Finché l'Excel è in prova, la regola è l'Excel.

Lingue della mappa: **italiano e inglese**, con l'inglese come ripiego per le altre lingue del
sito. Islandese e arabo restano tradotti nei sorgenti ma non escono più nel file pubblico.

## Il modulo "prenota una call" si accende e si spegne

Sta in fondo alla sezione Profile di `index.html`, sopra il pulsante Access Reserved. Il pulsante
apre una finestra Potential che contiene **l'agenda di Google incorporata**: il visitatore prenota
senza uscire dal sito.

```html
<div class="book-cta" data-cta="on">     <!-- "on" acceso · "off" spento -->
```

È l'unica cosa da toccare. A `off` il blocco sparisce dal flusso, il markup resta in pagina e
**l'iframe non viene montato**: a modulo spento la home non chiama `calendar.google.com` e nessun
cookie Google parte.

| Cosa | Dove |
|---|---|
| Interruttore acceso/spento | attributo `data-cta` su `.book-cta` |
| Indirizzo del pulsante mail | `href` di `.bk-mail` — `info@potential.contractors` |
| Durata dichiarata nei testi | **nessuna**, per scelta dell'11.08.2026 — il meccanismo resta: `{min}` in una stringa, riempito da `window.CALL_MIN` |
| Taglio della testata di Google | `--bkcrop` su `.bk-frame` (172px sopra i 1000px di larghezza, 0 sotto) |
| Agenda incorporata | `data-src` dell'iframe `#bkFrame` |
| Link di scorta, si apre su Google | `href` di `.bk-alt` — `https://calendar.app.google/mrsYTpu4XFsmfZCm7` |

⚠️ **I testi non dicono quanto dura la call.** Lo slot su Google è da 60 minuti, ma nessuna stringa
lo dichiara. Chi la volesse dichiarare non scrive il numero nelle traduzioni: mette `{min}` nella
stringa e lo riempie `window.CALL_MIN`. E **`window.CALL_MIN` non cambia lo slot su Google** — la
durata vera si imposta in Google Calendar → Programmazione appuntamenti. Se le due cifre divergono,
il visitatore legge una durata e ne prenota un'altra.

⚠️ **Il taglio della testata di Google vale solo da 1000px in su.** Sopra quella soglia la finestra
mostra i soli orari; sul telefono si vede la testata di Google per intero, "Appuntamenti di 60"
compreso. Se la durata non deve comparire da nessuna parte, va cambiato lo slot su Google, non il
sito.

⚠️ **L'URL incorporato non è quello che si condivide.** Il link corto `calendar.app.google/…`
risponde `X-Frame-Options: SAMEORIGIN` e dentro una cornice resta bianco. Nell'iframe ci va la forma
lunga `calendar.google.com/calendar/appointments/schedules/<id>?gv=true` — è `?gv=true` che rende la
pagina incorporabile. Il link corto resta buono per il pulsante di scorta e per le mail.

⚠️ **Il contorno bianco dell'iframe è deliberato.** `#ffffff` è lo sfondo della pagina di Google
(verificato l'11.08.2026): l'avorio del sito (`--w`, `#f4f3ef`) a fianco si leggerebbe come una
cornice grigia. Se Google passa a un grigio Material, quel bianco va rifatto combaciare.

I nove testi nuovi (`stag-book`, `bk-*`) sono tradotti in tutte e cinque le lingue dentro `const T`
e sono **già nel foglio delle traduzioni**, in grigio: tradotti in automatico, non ancora riletti da
un revisore umano.

## Le traduzioni si tengono allineate, non si ricopiano

`index.html` e il **Google Sheet `Potential_Revisione_Traduzioni`** sono due fonti che devono dire
la stessa cosa. Chi le allinea è `sync_traduzioni.py`, e **lo stato sta nel colore del testo delle
celle**: verde = forzatura decisa da Carlo, grigio = traduzione automatica, rosso = da riallineare.

Il foglio si apre da `tools/revisore_traduzioni/Potential_Revisione_Traduzioni.gsheet`, che è il
segnalino che Drive tiene nella cartella. ⚠️ **Dal 20.08.2026 la fonte non è più un file `.xlsx`**:
l'Excel di prima sta in `tools/revisore_traduzioni/archivio_xlsx/`, congelato al giorno della
migrazione, e non è più la fonte di niente.

```bash
python3 tools/revisore_traduzioni/sync_traduzioni.py --check    # non scrive, elenca
python3 tools/revisore_traduzioni/sync_traduzioni.py --scrivi   # backup, poi scrive
```

⚠️ **Le regole non sono qui**: stanno in `tools/revisore_traduzioni/potential_revisore_traduzioni_rules.md`,
accanto al foglio, e vanno lette prima di toccare un testo. Quella cartella è in `.gitignore` — il
repository è pubblico — quindi né le regole né lo strumento sono in questo repository: vivono nella
cartella del progetto su Google Drive. **Il contenuto delle traduzioni non vive nemmeno lì**: sta nel
Google Sheet, e nella cartella c'è solo il segnalino che lo apre.

⚠️ **Dopo ogni modifica di testo sul sito va chiesto a Carlo se aggiornare il foglio.** Sempre, anche
per una parola. E se una frase cambia di *significato*, va segnalato anche quando le altre lingue
sono verdi: un concetto nuovo può rendere sbagliate le forzature fatte a mano.

## Anteprima locale

```bash
python3 -m http.server 8080
# apri http://localhost:8080/index.html
```

## ⚠️ `3f8ab961aeb54413a83faefa431e7f17.txt` — non cancellare

Sembra spazzatura e non lo è: è la **chiave IndexNow**, il protocollo con cui si notifica a Bing
(e quindi a **ChatGPT Search, Copilot, DuckDuckGo, Ecosia**, che condividono quell'indice) che un
URL è nuovo o è cambiato, invece di aspettare settimane che il crawler passi da solo.

Funziona così: il file contiene la chiave, il suo nome **è** la chiave, e la sua presenza in
radice è ciò che prova a Bing che chi notifica possiede il dominio. **Se il file scompare, le
notifiche vengono rifiutate** — silenziosamente, come sempre.

⚠️ **Deve stare in radice e deve essere raggiungibile pubblicamente.** Non è un segreto: è un
token di proprietà, e chiunque lo legga può al massimo notificare URL *di questo dominio*, che è
esattamente ciò che vogliamo. Per la specifica IndexNow la **cartella** in cui vive il file
delimita gli URL notificabili: in radice copre tutto il sito, in una sottocartella coprirebbe solo
quella. Per questo è l'unica eccezione alla regola «in radice solo `CLAUDE.md`, `INDEX.md`,
`README.md`».

**Non va in `.gitignore`.** Attivata il 17.08.2026.

```bash
# notificare un URL
curl -s "https://api.indexnow.org/indexnow?url=https%3A%2F%2Fpotential.contractors%2F&key=3f8ab961aeb54413a83faefa431e7f17"
```

📌 Da usare **quando si pubblica o si modifica una pagina**, non a ripetizione: un `429 Too Many
Requests` significa che siamo stati marcati come spam.

## Cosa non sta su GitHub

⚠️ **Un clone di questo repository non basta a rigenerare il sito.** Dal 17.08.2026 tutto `tools/`
è in `.gitignore`: gli script di build vivono **solo sul Mac**, con una copia di sicurezza in una
cartella interna.

Il motivo non è l'ordine. Questo repository è **pubblico** e GitHub Pages serve **tutto ciò che sta
nel repository**: fino a quel giorno gli script di build, i dati che usano e le procedure interne
erano scaricabili da chiunque sul dominio. Verificato con `curl`: HTTP 200 su sei file.

E il buco era doppio, perché `robots.txt` conteneva sette gruppi `User-agent` nominati (GPTBot,
ClaudeBot, PerplexityBot…) con solo `Allow: /`. Per la specifica REP un crawler applica **un solo
gruppo e ignora `*` interamente**: quei sette non vedevano `Disallow: /tools/` ed erano
formalmente autorizzati a ingerire i tier dei clienti. Il perché per esteso è dentro `robots.txt`,
scritto lì così chi lo riapre non li rimette.

**Cosa vive solo sul Mac:**

| Cartella | Cosa contiene |
|---|---|
| `projects/suppliers-radar/scripts/` | build della portfolio map e la sua configurazione |
| `tools/costellazione-data/` | build della costellazione + procedura |
| `tools/revisore_traduzioni/` | segnalino del Google Sheet delle traduzioni, regole, `sync_traduzioni.py`, `archivio_xlsx/` con l'Excel di prima |
| `projects/suppliers-costellazione/editor/` | editor visuale della costellazione |
| `tools/seo_optimization/` | audit SEO |
| `tools/build-header-frames.py` | build dei frame dell'header |
| `portfolio/…_ISTRUZIONI.md` | procedura dell'area riservata |

⚠️ **`portfolio/` non si può difendere con `robots.txt`**: la pagina dell'area riservata deve
restare scansionabile perché il suo `noindex` venga letto. Lì l'unica difesa è **non pubblicare il
file**, non vietarne la lettura.

⚠️ **La difesa vera è `.gitignore`, e regge solo finché resta lì.** Il backup automatico fa
`git add -A`: chi togliesse quelle righe rimetterebbe online i tier dei clienti al primo push,
senza che nessuno abbia deciso niente.

📌 **Resta aperto:** i file rimossi sono ancora nella **storia dei commit** di un repository
pubblico. Toglierli dal presente non li toglie dal passato — scelta deliberata del 17.08.2026,
perché l'alternativa (`git filter-repo`) riscrive commit già pubblicati.

## Deploy

Repo pubblico. Per pubblicare: `git push` (vedi nota auth sotto), poi eventualmente attivare
GitHub Pages (Settings → Pages → branch `main`).
