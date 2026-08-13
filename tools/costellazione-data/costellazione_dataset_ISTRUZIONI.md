# La costellazione si edita in Excel

Riguarda `costellazione/costellazione.html` e `costellazione/network.json`, cioè la mappa delle
competenze della rete di fornitura. Dall'11.08.2026 la fonte è **un Excel**:

```
costellazione/costellazione-dataset.xlsx
```

Sta accanto ai file che genera ma **non è uno di quelli**: è la fonte, ed è in `.gitignore` —
non esce su GitHub, vive su questo Mac e si sincronizza con Dropbox.

> **Sistema parallelo.** L'editor visuale in `tools/editor-costellazione/` è ancora al suo posto e
> funziona. I due scrivono sugli stessi tre file: **si usa uno solo**, o l'ultimo che salva
> cancella il lavoro dell'altro senza dirlo. Finché l'Excel è in prova, la regola è l'Excel.

---

## I tre comandi

```bash
python3 tools/costellazione-data/build.py --check   # dice cosa cambierebbe, non tocca niente
python3 tools/costellazione-data/build.py           # riscrive i tre json nel Brain
sh "…/suppliers database/scripts/publish.sh"        # rigenera network.json e pubblica
git pull                                            # ⚠️ il repo resta indietro di un commit
```

Più due che servono di rado:

```bash
python3 tools/costellazione-data/build.py --status   # dove si è fermata la catena
python3 tools/costellazione-data/build.py --outline  # rimette la struttura a livelli
```

## Chi si ricorda di pubblicare

`--status` risponde a tre domande: l'Excel è avanti sui json? i json sono avanti su
`network.json`? quello che sta sul sito è quello che abbiamo generato?

Non serve ricordarsi di lanciarlo. Un hook `SessionStart` in `.claude/settings.local.json` lo
esegue con `--hook` a ogni apertura di Claude Code in questa cartella, e in quella modalità
**parla solo se qualcosa è disallineato**. Il resto del tempo tace di proposito: un avviso che
compare sempre viene ignorato sempre.

⚠️ Il caso pericoloso non è quello che si rompe, è quello che tace. Una modifica fatta in Excel e
mai pubblicata non dà nessun errore: dà un sito fermo a due settimane fa, e ci si accorge
guardando una data.

⚠️ `settings.local.json` è in `.gitignore` — vive su questo Mac e su Dropbox, non su GitHub. Su un
computer nuovo si recupera da Dropbox insieme al resto del repo, non con un `git clone`.

Il quarto comando non è opzionale: `publish.sh` committa e pusha da una copia di lavoro sua,
quindi il repo locale resta indietro e il push successivo va in conflitto.

Il primo comando è quello da prendere per abitudine. `--check` legge, valida, confronta e dice
quali file cambierebbero, senza scrivere niente.

## Cosa c'è nei quattro fogli

**`NODI`** — una riga per nodo, 90 righe: 9 macro-ambiti e 81 sotto-ambiti.

| Colonna | Cosa ci va |
|---|---|
| `ord` | Il numero d'ordine. Serve a poter riordinare il foglio e rimetterlo com'era |
| `macro` | L'id del macro-ambito di appartenenza. **Se è uguale a `id`, quella riga *è* il macro-ambito** |
| `id` | L'identificatore del nodo. Non si traduce e non si vede: è la chiave che tiene insieme i tre file |
| `sectors` | Quali dei sette settori serve, separati da `;` |
| `sources` | Le cartelle dell'archivio fornitori che stanno dietro al nodo, **una per riga** dentro la cella (alt-invio) |
| `label_*` | Il nome del nodo |
| `blurb_*` | La riga di descrizione che si legge aprendolo |
| `scope_*` | **Quattro voci separate da `;`** — cosa si può chiedere a quel nodo |

Le colonne `_is` e `_ar` hanno l'intestazione più chiara: islandese e arabo sono tradotti per
intero ma **non escono nel file pubblico** dal 2026-08-10. Restano scritti perché riaverli
costerebbe una giornata.

Le righe dei macro-ambiti hanno lo sfondo grigio e **non portano né settori né cartelle**: i
settori di un macro sono l'unione di quelli dei suoi figli, e li calcola `build_public.py`.

### La struttura a livelli

Il foglio è raggruppato: i sotto-ambiti stanno **dentro** il loro macro-ambito, e a sinistra
compaiono il `+/−` di ogni ramo e i numeri **1** e **2** in alto, che chiudono e aprono tutto.
Con `1` restano i nove macro-ambiti, ed è la vista in cui si ragiona sulla struttura; con `2`
tornano tutte le 90 righe.

Stessa cosa in orizzontale: le **sei colonne di islandese e arabo** sono un gruppo a sé, e il
`+/−` sopra la barra delle colonne le chiude in blocco. Sono lingue che non escono nel file
pubblico: chiuse, il foglio sta molto meglio in uno schermo.

Il raggruppamento si ricalcola dalla colonna `macro`, non dalla posizione. Se aggiungi righe in
mezzo a un ramo Excel le assorbe da solo; se le aggiungi **in fondo al foglio** restano fuori dal
gruppo, e si rimette tutto a posto con:

```bash
python3 tools/costellazione-data/build.py --outline
```

⚠️ Va lanciato a **file chiuso**: se l'Excel è aperto, il salvataggio si scontra con la copia che
Excel tiene in memoria e vince l'ultimo che scrive.

**`UI`** — le 17 stringhe dell'interfaccia della pagina: titolo, password, "Cerca", il footer.
**`SETTORI`** — le etichette tradotte dei sette Coverage Areas.
**`CONFIG`** — `version`, `languages` (le lingue che escono), `rtl`.

## Le tre cose che l'Excel non decide

1. **La dimensione dei nodi sul grafo.** Il peso viene dal conteggio delle cartelle
   dell'archivio `WORK - DATABASE/DATABASE FORNITORI`, compresso in cinque gradini perché non sia
   leggibile a ritroso. Se lo si potesse scrivere a mano smetterebbe di dire qualcosa.
2. **Quali sono i sette settori.** Sono le categorie del sito e stanno in
   `taxonomy/build_taxonomy.py`. Il foglio `SETTORI` ne governa le sole etichette: se ne aggiungi
   uno lì, il build si ferma. Aggiungere un settore vuol dire cambiare il sito.
3. **L'ordine dei nodi sul grafo**, che è l'ordine delle righe. La colonna `ord` esiste per
   renderlo esplicito: se riordini il foglio per lavorarci, **riordina per `ord` prima di
   salvare**, o la costellazione cambia disposizione senza che nessuno l'abbia deciso.

## Quando si ferma — e cosa vuole

Il build raccoglie **tutti** i problemi e li elenca in un colpo, con il numero di riga di Excel.
Non scrive niente finché non sono risolti tutti.

- **Settore sconosciuto.** Un refuso in `sectors`: elenca i sette validi.
- **Cartella assegnata a due nodi.** Una cartella dell'archivio sta sotto un nodo solo.
- **Sotto-ambito senza cartelle o senza settori.** Sarebbe un nodo sul grafo senza niente dietro.
- **Traduzione mancante in italiano o inglese.** Una lingua su due rompe il selettore. Le lingue
  non pubblicate mancanti danno un avviso, non un blocco.
- **`macro` che non esiste.** Un macro-ambito è una riga in cui `macro` e `id` sono uguali.
- **Fogli o colonne rinominati.** Si leggono per nome, non per posizione.

Avvisi che **non** fermano niente ma vanno letti: uno `scope` con un numero di voci diverso da
quattro (di solito il separatore: è il punto e virgola, non la virgola), e una cartella dichiarata
che non risulta nell'archivio scansionato.

Prima di sovrascrivere, ogni giro lascia una copia dei tre json in `taxonomy/.backup/<data_ora>/`.

## Se qualcosa va storto

L'Excel si può sempre ricreare dai json:

```bash
python3 tools/costellazione-data/build.py --bootstrap --force
```

⚠️ Questo **riscrive l'Excel con il contenuto del Brain**: tutto quello che è nel foglio e non è
ancora stato rigenerato si perde. Serve per ripartire, non per allinearsi.

---

**In una riga:** si edita `costellazione-dataset.xlsx`, poi `build.py`, poi `publish.sh`, poi
`git pull`. I file in `costellazione/` non si toccano mai a mano.
