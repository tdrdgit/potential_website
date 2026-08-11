# Aggiornare la lista clienti — carousel e portfolio map

Riguarda le due pagine di questa cartella: `potential-carousel.html` (griglia alfabetica) e
`potential-portfolio-map.html` (radar a 7 assi). **L'elenco clienti è generato**: quello che si
scrive a mano dentro il blocco sparisce alla prima rigenerazione, senza lasciare traccia.

La costellazione della home e di `/costellazione/` è un'altra catena, con un'altra fonte e altri
comandi: `tools/editor-costellazione/editor_costellazione_ISTRUZIONI.md`.

⚠️ I comandi qui sotto si lanciano **dalla radice del repo**, non da questa cartella.

⚠️ **Questo repository è pubblico.** I nomi dei fornitori e i clienti riservati non escono da
questa catena, ed è una proprietà dello script, non della buona volontà di chi lo lancia.

---

## La fonte, una sola

```
~/Dropbox/CARLO DOCUMENTI MAC/WORK - SUPPLIERS OFFERING/PT-SUPPLIERS PROJECTS LIST.xlsx
foglio: SUPPLIERS PROJECTS
```

Colonne che contano: `WEBSITE · RISERVATO · SECTOR · FORNITORE · CLIENT / PROJECT · LOCATION ·
CONTRACTOR`. Le due colonne di note non vengono lette.

| Colonna | Cosa fa sul sito |
|---|---|
| `WEBSITE = x` | **l'unico interruttore**: senza la x il cliente non esiste, per il sito |
| `RISERVATO` | riga esclusa **sempre**, anche se qualcuno la flagga per sbaglio |
| `SECTOR` | asse del radar + etichetta nel dettaglio |
| `CLIENT / PROJECT` | il nome mostrato |
| `LOCATION` | va in coda al dettaglio; più righe stesso cliente = più località in fila |
| `CONTRACTOR` | diventa `· for <nome>`, ed è **ciò che rende grigio il pallino** sulla mappa |
| `FORNITORE` | diventa una lettera (`Supplier A`, `B`…) nella riga di filtri della mappa |

Il nome vero del fornitore **non si salva da nessuna parte**: `A` va a chi ha più clienti, le
parità si sciolgono in ordine alfabetico, e la legenda lettera → nome si stampa a terminale e
muore lì. Un cliente senza `FORNITORE` in Excel resta fuori da ogni filtro fornitore. Sotto i due
fornitori la riga di filtri si nasconde da sola.

Righe ripetute per località — Tiffany, Burberry, Hilton — si fondono in **un cliente solo**.

## La procedura

```bash
# 1. l'Excel è già stato modificato e SALVATO (chiuderlo non serve, salvarlo sì)

python3 tools/portfolio-data/build.py --check    # non tocca niente, dice cosa cambierebbe
python3 tools/portfolio-data/build.py            # riscrive le due pagine

git diff                                         # deve toccare solo i blocchi PORTFOLIO-DATA
git add -A && git commit -m "..." && git push
```

Lo script scrive **solo** fra i marcatori `PORTFOLIO-DATA:START … END`. Grafica, traduzioni e
motore del radar non li vede nemmeno.

## Quando si ferma — e cosa vuole

- **Cliente nuovo senza fascia luxury.** Si ferma, lo elenca, e non riscrive niente. La fascia
  (1 mass market → 5 ultra luxury) va scritta in `tools/portfolio-data/tiers.json` e poi si
  rilancia. ⚠️ **La fascia è il posizionamento del marchio del cliente nel suo mercato**, non la
  dimensione della commessa: Chanel resta 5 anche se il progetto è il loro ufficio di Milano. La
  proposta la fa Claude, la conferma è di Carlo.
- **Nessuna riga con `WEBSITE = x`.** Si ferma invece di svuotare le pagine.
- **Marcatori spariti** da una delle due pagine. Si ferma: non sa dove scrivere.
- **Più di 26 fornitori.** Le lettere finiscono.

## Cosa segnala senza fermarsi — da leggere

- `! riga N: settore «...» sconosciuto — riga saltata` → il settore va aggiunto alla tabella
  `SECTORS` in `build.py`, altrimenti quel cliente **non esce e nessuno se ne accorge**.
- `! <cliente>: compare sia in X sia in Y` → doppio settore in Excel, tiene il primo.
- `fasce senza cliente in Excel` → righe orfane in `tiers.json`, di solito un cliente rinominato.
- `senza FORNITORE in Excel: ...` → quei clienti restano fuori dai filtri.

## Il tranello delle località

Lo stesso posto scritto in due modi (`Harrods, London` / `Harrods, Londra`, `Venezia Fondaco` /
`Venice Fondaco`, `Parigi` / `Paris`) comparirebbe due volte nella stessa riga. La tabella
`PLACES` in `build.py` li normalizza in lettura — **è una toppa**: la pulizia va fatta
nell'Excel, e finché non è fatta quella tabella va tenuta aggiornata.

---

**In una riga:** i clienti si cambiano nell'Excel, mai nell'HTML; poi `build.py`. Se lo script si
ferma ha ragione lui — forzare la mano significa pubblicare un dato che non doveva uscire.
