# PT-GN-Report 2026.08.06 (SEO audit - Site current state)

Audit tecnico, contenuti, structured data e citabilità AI di **potential.contractors**.
Misurato il 6 agosto 2026 con il plugin `claude-seo` v2.2.4, 8 agenti specialistici in parallelo.

**Questo documento è l'input del passaggio 6 (A6 — Site Auditor) del panel descritto in
`PT-GN-Brief 2026.08.06 (SEO GEO research panel).md`.** Copre solo lo *stato attuale del
sito*. Non copre — e non deve coprire — la mappa di categoria (A1), il benchmark competitor
(A2), le buyer persona (A3), le query reali (A4) e la baseline di visibilità sui motori AI
(A5): quelli restano agli altri agenti del panel.

**Convenzione**: 🟠 marca un valore stimato, mai misurato. Ogni 🟠 porta accanto il
ragionamento che lo regge. Dove il dato non è ottenibile è scritto **dato mancante** con
l'elenco di cosa servirebbe per chiuderlo.

---

## SEO Health Score: 60/100

| Categoria | Peso | Punteggio | Nota in una riga |
|---|---|---|---|
| Technical SEO | 22% | 65 | Fondamenta pulite, ma l'italiano non è indicizzabile |
| Content Quality | 23% | 50 | ~670 parole per lingua, zero prove verificabili all'esterno |
| On-Page SEO | 20% | 55 | Metadati ottimi, above the fold vuoto, CTA a 15 schermate |
| Schema / Structured Data | 10% | 65 | JSON-LD valido, ma senza `sameAs`, logo, indirizzo |
| Performance (CWV) | 10% | 90 | Misurato: l'unica area davvero a posto |
| AI Search Readiness | 10% | 45 | Crawler ammessi, ma nessuna eco esterna da citare |
| Images | 5% | 70 | Una sola `<img>`, OG image corretta, pesi ragionevoli |

Il punteggio è la media pesata dei sette punteggi di categoria. I punteggi di categoria sono
🟠 **stime editoriali**, non output di un tool: nessuno strumento assegna un voto a "content
quality". Le *evidenze* sotto sono invece tutte misurate, e sono quelle che contano.

### La lettura in cinque righe

Il sito non ha problemi tecnici gravi. Il contenuto è statico, i crawler AI sono ammessi ed
entrano, le performance sono buone, i metadati sono curati meglio della media. Il problema è
un altro, ed è duplice: **above the fold il sito non dice cosa fa e non dà un modo per
contattarti**, e **fuori dal sito non esiste nulla che confermi che Potential esiste**. Il
primo è un problema di conversione, il secondo di credibilità. Nessuno dei due si risolve con
la SEO.

---

## 1. I sei finding che contano

Ordinati per impatto, non per categoria.

### 1.1 — Above the fold non c'è la value proposition. E non c'è un contatto. `CRITICAL`

**Evidenza — verificata di persona su screenshot mobile 390×844 e desktop 1440×900.**
Nella prima schermata si vede: il logo, il payoff *"Every space. Delivered."*, lo switch
lingua a 5 sigle, la scritta *SCROLL DOWN*. Nient'altro. Il payoff è un'immagine SVG, quindi
**non si traduce**: resta in inglese anche in italiano, cinese, russo e arabo.

La frase che spiega davvero il business — *"One single point of contact. All suppliers."* —
è l'H1 del documento, ma è misurata a **y = 900px su desktop e y = 844px su mobile**: esattamente
una schermata intera più in basso. Un development manager deve scrollare un viewport pieno
prima di leggere una parola che dica cosa fa Potential.

L'unico contatto del sito è il `mailto:info@potential.contractors`, nell'ultima sezione prima
del footer: **10.619 px dall'alto su desktop (11,8 schermate), 12.768 px su mobile (15,1
schermate)**. L'unico bottone che assomiglia a una CTA a metà pagina è *"Access Reserved"*,
che è l'area clienti protetta da password, non una richiesta di contatto.

**Perché conta.** Per un buyer che valuta in trenta secondi se scriverti, il sito oggi non
risponde né a "cosa fanno" né a "come li contatto". Questo è il finding a più alto ritorno
dell'intero audit e non richiede contenuto nuovo: il testo giusto esiste già, è solo nel
posto sbagliato.

**Fix.** Portare la headline esplicativa dentro il primo viewport (o subito sotto il logo,
riducendo l'hero da 100vh) e aggiungere una CTA persistente in nav. **Effort: 5-7h**
(design + implementazione + replica nelle 5 lingue).

---

### 1.2 — Fuori dal sito, Potential non esiste. `CRITICAL`

**Evidenza.**
- Dominio registrato il **13 giugno 2026** (RDAP Identity Digital): ha **54 giorni**.
- Common Crawl: `in_crawl: false`, `in_rankings: false`. Ma la release interrogata
  (`cc-main-2026-jan-feb-mar`) copre una finestra **precedente alla registrazione del
  dominio**: è impossibile che lo contenga. Non è un dato negativo, è un dato non applicabile.
- Nessun `sameAs` in tutto il JSON-LD: né su `Organization` né su `Person`.
- Nessun link social in tutta la pagina: zero occorrenze di "linkedin", "instagram",
  "facebook", "twitter" fuori dal meta tag Twitter Card (che è un formato di preview, non un
  link).
- L'unico portfolio è dietro password (*"Access Reserved"*).
- DuckDuckGo, 6 agosto 2026, query `"potential.contractors"` e `"Carlo Casagrande" "Potential"
  FF&E`, **una sola interrogazione ciascuna, nessuna geolocalizzazione**: nessun risultato.
  ⚠️ L'indice DDG è molto più piccolo di quello Google: "zero su DDG" **non** equivale a
  "zero su Google". Query non ripetuta: da rifare secondo il protocollo del brief.

**Perché conta.** Se un buyer chiede a ChatGPT o Perplexity *"chi è Potential contractors, è
affidabile?"*, il modello nel caso migliore ripete quello che dice il sito — che per
definizione non è una verifica indipendente. Nel caso peggiore non trova l'entità e risponde
sulla locuzione comune (vedi 1.3).

**Fix.** LinkedIn Company Page + `Person.sameAs` verso il profilo personale di Carlo. È la
leva singola a più alto impatto sul GEO, e non è un intervento sul sito.
**Effort: 2-4h** di setup, poi manutenzione.

---

### 1.3 — Il nome è ambiguo per un LLM. `HIGH`

Il brand si presenta ovunque — `<title>`, OG tag, `schema.org name`, footer — semplicemente
come **"Potential"**. Mai "Potential Contractors", mai una ragione sociale. Il `.contractors`
vive solo nell'URL.

Il problema è che *"potential contractors"* è una **locuzione di uso comunissimo** nel
linguaggio di gara e capitolato in inglese, con significato di "elenco di appaltatori
candidati". Un LLM che riceve "who is Potential contractors" ha due letture in competizione, e
oggi non ha **nessun** segnale esterno che lo spinga verso l'entità-azienda invece che verso
la frase comune.

**Fix.** Uso coerente di un nome esteso univoco — 🟠 es. *"Potential — FF&E Procurement"* —
in title, schema, LinkedIn, firma email. 🟠 È una **decisione di naming che spetta a te**, non
un dato tecnico: qui è marcata come ipotesi, non come raccomandazione chiusa.
**Effort: 1-2h di decisione + ~2h di propagazione.**

---

### 1.4 — "Our Numbers" attribuisce a Potential il curriculum personale di Carlo. `HIGH`

**Evidenza.** La sezione *"Our numbers — Scale, quality and track record by the numbers"*
espone *"50+ Top-tier global clients"* e *"40+ International awards"*. Poche righe sotto, nella
bio del founder, compaiono **gli stessi due numeri**, seguiti dall'elenco nominativo: PepsiCo,
3M, ABB, Unilever, Intel, Amplifon, Adidas, Trenitalia Frecciarossa, Durex, Illy, B&B Italia,
Flos, Fendi Casa e altri.

Quei marchi sono clienti di brand experience e design, non commesse FF&E chiuse da Potential.
Un procurement manager che legge "Our Numbers" prima di arrivare alla bio attribuisce quei
nomi a Potential-procurement — e scopre il contrario in call, cioè nel momento peggiore.

**Nessuna frase del sito viola letteralmente la regola** "i lavori li realizzano i partner
della rete": la ricerca su tutte le 140 chiavi del dizionario EN+IT per "we built / we deliver
/ abbiamo realizzato / realizziamo" non ha prodotto occorrenze. Il rischio è di collocazione,
non di formulazione — ma è lo stesso meccanismo, e per questo lo tengo in HIGH.

**Fix.** O etichettare esplicitamente quei due dati come *"Founder's track record"*, o
spostarli dentro la bio lasciando in "Our Numbers" solo le tre metriche davvero FF&E (savings
documentati, % di risparmio a gara). **Effort: 1h.**

🟠 **Dato mancante**: se *"10+ anni di esperienza"* si riferisce a Potential o alla carriera
di Carlo. Va chiarito, perché ha lo stesso problema di attribuzione.

---

### 1.5 — La versione italiana non è indicizzabile. `HIGH`

**Evidenza.** `grep -c hreflang index.html` → **0**. `<html lang="en">` è statico; la lingua
cambia solo via JS (`document.documentElement.lang = lang`, riga 1197), a partire da
`localStorage` / `navigator.language`. Le stringhe IT/ZH/RU/AR vivono solo dentro l'oggetto JS
`const T = {…}` (riga 1135, **38.463 byte, il 37% dell'HTML**). Verificato live: `/it`, `/it/`,
`/en`, `/en/` restituiscono tutti **404**. La sitemap dichiara 2 URL, entrambi inglesi.

Conseguenza: Google e i crawler AI vedono **una sola pagina, in inglese, per sempre**. Tutto
il lavoro di traduzione italiana ha valore SEO zero — non perché sia scritto male, ma perché
non ha un indirizzo.

**Il giudizio onesto, però, è che questo non sia urgente.** Se la lettura che governa il piano
è il credibility layer (verifica dopo il primo contatto, non intercettazione di domanda a
freddo), l'italiano indicizzabile serve poco: la verifica avviene su ricerca brandizzata e su
LinkedIn, non su query generiche in italiano. **La decisione spetta alla Fase 0 del panel, non
a questo audit.** Se invece emerge che il mercato domestico va presidiato con ricerca organica,
questo diventa il primo lavoro tecnico da fare.

**Fix.** Pre-generare varianti statiche per lingua (`/it/`, `/en/`) dalla stessa fonte di
stringhe già usata dal motore JS, con `hreflang` reciproci, `x-default`, canonical distinti e
`<html lang>` per variante. È un lavoro di build, non una toppa sulla sitemap.
**Effort: 8-16h.**

---

### 1.6 — La privacy policy non dice chi è l'azienda. `HIGH`

**Evidenza —** `potential-privacy-policy.html`, riga 178, testuale:

> *"Company (referred to as either 'the Company', 'We', 'Us' or 'Our' in this Privacy Policy)
> refers to **Partita Iva**, via Ornato 140, 20162 Milano."*

Il segnaposto del generatore non è mai stato sostituito con la ragione sociale e il numero.
Nessun'altra pagina del sito riporta ragione sociale o P.IVA.

**Perché conta.** È esattamente il documento che un procurement manager apre in due diligence
prima di un NDA, ed è l'unico posto del sito dove ci si aspetta rigore legale. Trovarlo rotto
è un fallimento diretto e verificabile dell'ipotesi credibility layer — non un'inferenza.

**Fix. Effort: 15 minuti.** Serve solo il dato.

---

## 2. Il resto dei finding, per area

### 2.1 Technical — 65/100

| # | Finding | Sev. | Evidenza | Effort |
|---|---|---|---|---|
| T1 | Conflitto robots/noindex su `/network/` | Medium | `robots.txt` fa `Disallow: /network/`, ma `index.html:771` la linka con `<a href="network/">` e `network/index.html:6` ha già `noindex, nofollow`. Bloccata da robots, Googlebot non può *leggere* il noindex: l'URL può restare indicizzato "nudo" | 0,5h |
| T2 | Nessun security header | Medium | `curl -sI` → nessun HSTS, CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy. Limite di GitHub Pages. HTTPS forzato e redirect www/non-www puliti, quello sì | 2-4h (serve Cloudflare davanti) |
| T3 | IndexNow non implementato | Medium | `grep -ri indexnow` → nessun risultato. Con commit quasi giornalieri, Bing e Yandex aspettano il loro ciclo di crawl | 1h, poi automatizzabile |
| T4 | Dizionario 5 lingue inline | Medium | 38.463 byte scaricati e parsati da ogni visitatore per 4 lingue che non userà. Vedi 1.5 | 3-5h |
| T5 | 16 SVG header precaricati subito | Medium | `index.html:1044` — `FRAMES.forEach(… new Image())` scarica tutti i 16 frame (99,7 KB) al load per un'animazione decorativa | 2-3h |
| T6 | `lastmod` disallineato di un giorno | Low | Sitemap dice `2026-08-04`, header live dice `05 Aug 2026` | 0,5h |
| T7 | `/index.html` risponde 200 accanto a `/` | Low | Default GitHub Pages. Canonical già corretto, rischio duplicati neutralizzato. Solo da sapere | — |

**Confermato a posto**, e vale la pena dirlo: nessuna divergenza fra repo locale e sito live
(md5 identici su 4 file), redirect in un solo hop, gzip attivo, **e soprattutto il contenuto è
nel DOM statico**. Verificato di persona: 5.324 caratteri di testo leggibile senza eseguire una
riga di JavaScript. La paura che i crawler AI non vedano nulla è infondata.

### 2.2 Content — 50/100

**Volume.** ~670 parole per lingua totali, di cui 🟠 **~316 EN / ~292 IT** di prosa vera
(escluse liste ed etichette). 🟠 Conteggio fatto separando a mano i paragrafi discorsivi dalle
liste: è una stima di composizione, non una misura di tool.

**Disallineamenti IT/EN.** Cinque, tutti nella stessa direzione — l'italiano è più corto:

| Chiave | EN | IT | Cosa manca |
|---|---|---|---|
| `prob-txt2` | *"…average 4–6 months of slippage — directly eroding pre-opening revenues."* | *"…in media 4–6 mesi di ritardo."* | L'erosione dei ricavi pre-apertura |
| `prob-txt3` | *"…rarely share a single source of truth — creating costly misalignments throughout delivery."* | *"…raramente condividono una sola fonte di verità."* | La seconda clausola |
| `wc-b1` | *"…One control point. Everything converges."* | *"…Un punto di controllo."* | La chiusa |
| `wc-b2` | *"…no surprises"* | — | Assente |
| `wc-b4` | *"…Change orders managed before they become problems."* | — | Assente |
| `s02-title` | "Residential & Private" | "Residenziale" | "& Private" |

**Effort per chiudere tutti: ~1h.**

⚠️ **Il sesto caso è diverso e non va trattato come una svista.** `problem-big` dice in EN
*"Great design loses its value the moment it enters an unmanaged supply chain"* e in IT
*"Un ottimo design preserva il suo valore con una supply chain all'altezza"*: framing opposto,
perdita contro conservazione. **È voluto** — commit `a3f84c0` del 1 agosto, *"Site: IT problem
statement → positive framing"*. La domanda non è "riallinea l'italiano", è **quale dei due
framing vuoi**, e poi allinea l'altro. La regola sul bilingue allineato vale comunque: due
lingue non possono dire il contrario l'una dell'altra sul claim centrale della sezione.

**Statistiche senza fonte.** *"Hospitality fitouts exceed budget on 7 out of 10 projects"* e
*"interior projects average 4–6 months of slippage"* sono numeri precisi senza attribuzione.
Non è chiaro se siano dati di settore o stime tue. Un LLM che li cita li presenta come fatto
verificato: è un rischio reputazionale, non solo SEO. **Fix: o citi la fonte, o riformuli in
prima persona** (*"In our experience…"*), che è difendibile senza fonte esterna. **30 min.**

**Digital Layer.** La card 07 vive nella griglia "Coverage Areas" alla pari delle sei aree
FF&E, con `grid-column: span 2` — **doppio peso visivo** — e nessuna frase di raccordo. I
metadati fanno la cosa giusta (`Organization.description` dice *"plus a Digital Layer service
line"*), ma la gerarchia si perde nella UI, proprio nel primo blocco dove un buyer si forma
l'idea di chi sei. **Fix: riga di raccordo + togliere lo span doppio. 1-2h.**

**Il registro, invece, regge.** "Why it works", "What we do" e "Process" restano nel
vocabolario procurement e construction — RFI, Schedule of Values, value engineering, MEP
coordination, punch-list, O&M manuals — senza mai scivolare su tono da agenzia o da
rivenditore. Il sito non oscilla nel linguaggio: oscilla nella gerarchia visiva.

### 2.3 On-Page — 55/100

Metadati **sopra la media**: title descrittivo, meta description da 26 parole che è la frase
con la migliore probabilità di citazione diretta, canonical self-referenziale, OG e Twitter
Card completi con dimensioni dichiarate, `theme-color`, manifest, favicon SVG + ICO.

Il problema è la struttura dei heading: **1 H1 e 5 H2, nessun H3**. Le sezioni "Why it works",
"The problem" e **"The Founder" non hanno alcun heading** — sono div stilizzati. Il passaggio
più citabile del sito (la bio) non è annunciato da nulla. Nessun H2 è formulato come domanda:
sono tutti claim di brand (*"From vision to delivery."*, *"Scale, quality and track record by
the numbers."*).

### 2.4 Schema — 65/100

JSON-LD valido, parsa senza errori, `@graph` coerente con `Organization`, `WebSite`, `Person`,
`ItemList` di 7 `Service`. `Organization` è il tipo **giusto**: non `LocalBusiness` né
`ProfessionalService`, che implicano una sede fisica che riceve clienti.

Manca quello che serve a un LLM per credere che l'entità sia reale: **`sameAs`** (su
Organization e su Person — il singolo intervento più prezioso), `logo` (esiste già
`favicon.svg`, quadrato 100×100, mai usato in schema), `address`, `telephone`, `contactPoint`,
`vatID`, `foundingDate`. `ItemList` è un nodo isolato: nessun `makesOffer` lo richiama da
`Organization`, e i sette `Service` non hanno `@id` propri.

Il blocco JSON-LD completo e pronto da incollare, con i placeholder espliciti, è nel report
dell'agente schema (agentId `a315598536c3791c0`) — **non l'ho incollato qui perché contiene
sette PLACEHOLDER che vanno riempiti con dati che solo tu hai** (vedi §5).

### 2.5 Performance — 90/100. Misurato.

Lighthouse 13.4.1 locale, 3 run mobile (moto g power, RTT 150ms, CPU ×4) + 3 run desktop.
**Dati di laboratorio, non di campo** — nessuna credenziale Google, quindi niente CrUX.

| Metrica | Soglia | Mobile | Desktop | Verdetto |
|---|---|---|---|---|
| LCP | ≤2,5s | **1.651 ms** (media 3 run, spread ~10%) | **423 ms** | Good |
| CLS | ≤0,1 | **0** su 6/6 run | **0** | Good |
| INP | ≤200ms | dato mancante | dato mancante | Non misurabile in lab |

226,5 KB su 21 richieste. **Zero risorse render-blocking.** L'OTF non viene mai scaricato (il
browser si ferma al woff2, dichiarato per primo): il doppio `src` è ridondanza di codice, non
spreco di banda. Plain-Thin non viene scaricato affatto — nessun elemento usa `font-weight:100`.

L'unico collo di bottiglia vero: **l'element render delay è 860 ms, il 46-58% dell'LCP
mobile.** L'immagine LCP (`CAMP_00.svg`) è preloadata correttamente e arriva in ~200 ms, poi
**resta inutilizzata per 750-900 ms** perché l'`<img>` che la ospita viene creata via
`innerHTML` da uno script a fine `<body>` (righe 1013-1066): il browser deve parsare tutto il
documento prima di poter dipingere il byte che ha già in cache. **Fix: mettere l'`<img>`
nell'HTML statico dentro `#hlA` e lasciare allo script solo l'animazione successiva. 2-3h**,
più `fetchpriority="high"` sul preload (15 min).

### 2.6 AI Search Readiness — 45/100

**Il buono.** Il contenuto è statico e leggibile senza JS (693 parole estratte
boilerplate-stripped). `robots.txt` allowa GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot,
PerplexityBot, Google-Extended e CCBot su record dedicati — e i record specifici **non**
ereditano i `Disallow` del wildcard, quindi l'allow è effettivo. `llms.txt` è scritto bene e
onesto: dichiara *"These are the company's own published figures, not independently audited"*.
Raro, e giusto.

**Il ridimensionamento doveroso su llms.txt**: è uno standard non ufficiale, che **nessun
motore importante dichiara di usare** come segnale — Google Search lo ignora. Tienilo, costa
poco, ma non contarlo come leva.

**Il problema.** La citabilità a livello di passaggio è bassa. Un solo blocco si avvicina al
range utile: la bio del founder, 126 parole, densa e con clienti nominati. Tutto il resto è o
tagline (*"Every space. Delivered."*, *"One single point of contact. All suppliers."* — 7
parole, nessun verbo, non citabile) o frammento numerico isolato. E i passaggi che *sarebbero*
citabili sono quelli senza fonte del §2.2.

### 2.7 Images — 70/100

Una sola `<img>` in tutto il documento, con `alt=""` — corretto, è decorativa. OG image
1200×630 dichiarata, 54 KB. Font 556 KB su disco ma solo 91 KB serviti. Header SVG 296 KB su
16 file: 🟠 accorpabili in uno sprite, stima 2-3h, priorità bassa.

Nota non ovvia: **il messaggio di brand principale della pagina è un'immagine SVG senza
alternativa testuale.** "Every space. Delivered." non esiste come testo per un crawler, e non
si traduce in nessuna delle 5 lingue.

---

## 3. Il piano, separando SEO classico e GEO

L'errore da non fare è mescolarli: agiscono su meccanismi diversi e su tempi diversi.

### Interventi GEO — servono a farti trovare *credibile* quando qualcuno ti verifica

| # | Azione | Impatto | Effort |
|---|---|---|---|
| G1 | LinkedIn Company Page + profilo personale, con nome esteso coerente | Altissimo | 2-4h |
| G2 | `sameAs` su `Organization` e `Person` nel JSON-LD (dipende da G1) | Alto | 1h |
| G3 | Correggere il placeholder P.IVA nella privacy policy | Alto | 15 min |
| G4 | Attribuire o riformulare le statistiche senza fonte | Medio-alto | 1h |
| G5 | Heading in forma di domanda + portare la bio a un blocco autosufficiente annunciato da un H2 | Alto | 3-4h |
| G6 | Completare `Organization`: logo, address, vatID, foundingDate, contactPoint | Medio | 1h |
| G7 | Decisione di naming sul brand esteso | Alto, strutturale | 1-2h + 2h |

### Interventi SEO classico — servono a farti trovare da chi non ti conosce

| # | Azione | Impatto | Effort |
|---|---|---|---|
| S1 | Value proposition above the fold + CTA persistente | Altissimo (conversione, non ranking) | 5-7h |
| S2 | Spostare l'`<img>` LCP nell'HTML statico + `fetchpriority` | Medio | 2-3h |
| S3 | Risolvere il conflitto robots/noindex su `/network/` | Medio | 0,5h |
| S4 | IndexNow + rigenerazione `lastmod` al deploy | Medio | 1,5h |
| S5 | URL propri per lingua + hreflang + sitemap multilingua | Alto **se** il piano sceglie il mercato domestico organico | 8-16h |
| S6 | Security header via Cloudflare | Medio | 2-4h |
| S7 | Lazy loading dei 16 frame SVG | Basso-medio | 2-3h |

**Nota di realtà, come da vincolo del brief**: nessuna di queste voci richiede una redazione o
pubblicazione continuativa. Sono tutti interventi una-tantum. L'unica cosa che richiederebbe
mantenimento — un piano editoriale — **non è in questo elenco di proposito**: la decisione se
serve, e in che forma minima sostenibile, è materia della Fase 2-4 del panel.

---

## 4. Le prime tre azioni di questa settimana

1. **Correggere la privacy policy** (15 min). È il fix con il rapporto impatto/tempo più alto
   dell'intero documento, e ti serve solo aprire il file. Serve la ragione sociale e la P.IVA.
2. **Aprire o collegare LinkedIn** e metterlo in `sameAs` su `Person` e `Organization` (3-5h).
   È l'unica leva che disambigua l'entità e l'unica che dà a un LLM qualcosa di esterno da
   citare. Tutto il resto del GEO dipende da questa.
3. **Portare la value proposition sopra la piega e mettere una CTA in nav** (5-7h). Il testo
   esiste già, va solo spostato. Oggi chi arriva non sa cosa fai e non sa come scriverti.

Totale: **9-13 ore.** Poi si riapre il panel.

---

## 5. Dati che servono e che solo tu hai

- **Ragione sociale legale e numero di P.IVA** — blocca il fix della privacy policy e il campo
  `vatID` dello schema.
- **Indirizzo completo** — 🟠 dedotto "via Ornato 140, 20162 Milano" dalla privacy policy e
  "Based in Milan, Italy" dal sito, ma la fonte è proprio il file che contiene il placeholder
  rotto: **da confermare, non da assumere.**
- **URL LinkedIn personale di Carlo** e, se esiste, della pagina aziendale.
- **Telefono** — oggi non compare da nessuna parte sul sito.
- **Data di fondazione di Potential** come entità (diversa dall'anzianità professionale).
- **Chiarimento su "10+ anni"**: riferito a Potential o alla tua carriera.
- **Foto di Carlo** utilizzabile pubblicamente, per `Person.image` (opzionale).
- 🟠 **Decisione sul framing del problem statement**: perdita (EN) o conservazione (IT).

---

## 6. Baseline riproducibile — punto zero al 2026-08-06

Da rimisurare con gli stessi comandi fra 3 e 6 mesi (novembre 2026 - febbraio 2027).

```
Data misura:  2026-08-06
Dominio:      potential.contractors
Registrato:   2026-06-13 (età: 54 giorni)
Tier backlink: 0 (Moz e Bing non configurati)

claude-seo run commoncrawl_graph.py potential.contractors --json
  → in_crawl=false, in_rankings=false, release=cc-main-2026-jan-feb-mar
     (release antecedente alla registrazione: non applicabile, non negativa)

curl https://rdap.identitydigital.services/rdap/domain/potential.contractors
  → registration=2026-06-13

npx lighthouse https://potential.contractors/ --preset=perf --form-factor=mobile
  → LCP 1651ms (media 3 run), CLS 0, TBT 0ms

Contenuto statico senza JS: 5.324 caratteri (fetch raw), 693 parole boilerplate-stripped
Heading: 1 H1, 5 H2, 0 H3
Sitemap: 2 URL
hreflang: 0
sameAs: 0
```

Alla rimisurazione, un `in_crawl: false` avrà un significato diverso e più preoccupante di
oggi: la release di Common Crawl coprirà un periodo successivo alla registrazione.

---

## 7. Cosa NON è stato testato

Dichiarato per intero, come da failure condition del brief. Nessuna di queste voci è stata
colmata con una risposta plausibile.

- **Google AI Overviews, ChatGPT, Perplexity, Bing Copilot**: nessuna query diretta. Nessun
  tool disponibile in questo ambiente. **È il lavoro dell'agente A5, con il protocollo del
  brief — sessioni pulite, 3 ripetizioni minime, localizzazione dichiarata.**
- **Google Search**: non interrogato. Solo DuckDuckGo, una volta, indice non comparabile.
- **LinkedIn**: servizio autenticato, non verificabile. Non so se la pagina esista.
- **Google Search Console e CrUX**: nessuna credenziale configurata. Niente dati di campo su
  LCP/INP/CLS, niente stato di indicizzazione reale, niente report link.
- **INP reale**: non misurabile in laboratorio, richiede interazione utente vera.
- **Moz, Bing Webmaster, DataForSEO**: non configurati. DA/PA, domini referenti e anchor text
  sono **dato mancante**, non "zero".
- **Common Crawl indice mensile** (più fresco del grafo trimestrale): tentato su
  `CC-MAIN-2026-30` e `CC-MAIN-2026-25`, **504 Gateway Timeout** su entrambi anche dopo retry.
  Tentativo fallito, non assenza confermata.
- **Registro Imprese**: non testabile senza la ragione sociale reale, che il sito non dichiara.
- **Log del server**: nessun accesso, quindi nessuna conferma che GPTBot o ClaudeBot siano
  passati davvero. So che *possono*, non che *lo fanno*.
- **Touch target su device fisico**: valutati da CSS e da emulazione, non su hardware reale.

---

*Audit eseguito con `claude-seo` v2.2.4 — agenti: technical, content, schema, sitemap,
performance, visual, geo, backlinks. Screenshot e report Lighthouse grezzi nello scratchpad di
sessione, non versionati.*
