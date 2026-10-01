"""
Contenuti approfonditi ArchEsame — versione 2.
Teoria estesa (focus URBANISTICA), quesiti ampliati, quesiti di progettazione,
flashcard aggiuntive. Basato sul riassunto Ceccarelli e sulle tracce IUAV 2024.

Nota: sintesi di studio. Verifica sempre la normativa vigente sulle fonti ufficiali.
"""

import seed_data

CONTENT_VERSION = 3

CATEGORIES = seed_data.CATEGORIES

# =============================================================================
# TOPICS — teoria approfondita
# =============================================================================
TOPICS = [
    # ------------------------------------------------------------------ URBANISTICA
    {
        "slug": "urbanistica-fondamenti",
        "category": "urbanistica",
        "title": "Fondamenti di urbanistica e livelli di pianificazione",
        "subtitle": "Dalla L. 1150/1942 al governo del territorio Stato–Regioni",
        "read_minutes": 9,
        "key_points": [
            "Legge urbanistica fondamentale: L. 1150/1942, più volte modificata.",
            "Dopo la riforma del Titolo V (2001) la materia è 'governo del territorio', competenza concorrente Stato–Regioni.",
            "Pianificazione gerarchica a cascata: territoriale (PTR/PTCP) → comunale (PRG/PGT) → attuativa (piani esecutivi).",
            "Il DM 1444/1968 fissa zone omogenee, standard e limiti inderogabili.",
        ],
        "content": """## Che cos'è l'urbanistica

L'urbanistica è la disciplina che studia e regola l'**uso e la trasformazione del territorio** per fini collettivi: organizza gli insediamenti, le infrastrutture, i servizi e la tutela delle risorse. Il suo scopo è conciliare l'iniziativa privata (lo *ius aedificandi*, il diritto di costruire connesso alla proprietà) con l'**interesse pubblico** (ordinato sviluppo, dotazioni, ambiente).

## L'evoluzione storica

- **Legge 25 giugno 1865, n. 2359** (espropriazioni per pubblica utilità e piani regolatori delle grandi città): primo riferimento sistematico.
- **Legge 17 agosto 1942, n. 1150** – *Legge Urbanistica Fondamentale (LUF)*: introduce il sistema dei piani (PRG, piani particolareggiati) e il principio della pianificazione a scala comunale e sovracomunale. È tuttora la legge base, più volte modificata.
- **Legge 6 agosto 1967, n. 765** (*legge ponte*): rende obbligatorio il PRG, introduce la licenza edilizia e rinvia agli standard.
- **DM 2 aprile 1968, n. 1444**: zone omogenee, standard urbanistici, limiti di densità, altezza e distanza.
- **Legge 28 gennaio 1977, n. 10** (*legge Bucalossi*): l'edificazione è onerosa (contributo di costruzione); separa *ius aedificandi* e proprietà.
- **Legge 5 agosto 1978, n. 457** (recupero del patrimonio edilizio: piani di recupero, categorie di intervento).

## Il riparto delle competenze

La riforma del **Titolo V della Costituzione (L. cost. 3/2001)** ha sostituito la voce "urbanistica" con **"governo del territorio"**, materia di **legislazione concorrente** (art. 117 Cost.): lo **Stato** detta i *principi fondamentali*, le **Regioni** legiferano nel dettaglio. Ne deriva una forte diversificazione regionale (es. PGT in Lombardia, PSC/POC/RUE in Emilia-Romagna, PSC-POC in Toscana).

## Il sistema gerarchico dei piani

La pianificazione è **a cascata**: ogni livello è vincolante per quello inferiore.

- **Livello regionale/territoriale**: *Piano Territoriale Regionale (PTR)*, *Piano Territoriale di Coordinamento Provinciale (PTCP)*, piani di settore (paesaggistici, di bacino, dei parchi). Fissano tutele, grandi infrastrutture e indirizzi.
- **Livello comunale**: il *Piano Regolatore Generale (PRG)*, nelle leggi recenti sdoppiato in una **componente strutturale** (strategica, non conformativa della proprietà, a tempo indeterminato) e una **componente operativa** (conformativa, a termine quinquennale). Disciplina l'intero territorio comunale.
- **Livello attuativo/esecutivo**: piani particolareggiati, piani di lottizzazione, PEEP, PIP, piani di recupero. Attuano il PRG su ambiti definiti.

## Contenuti e allegati del PRG

Il PRG **azzona** il territorio, assegna indici e parametri (indice di edificabilità, altezze, distanze, rapporto di copertura), individua servizi, vincoli e infrastrutture. È corredato dalle **Norme Tecniche di Attuazione (NTA)**, dal **Regolamento Edilizio** e dagli elaborati cartografici. La sua formazione prevede adozione, pubblicazione, **osservazioni**, controdeduzioni e approvazione (con verifica di compatibilità coi piani sovraordinati) e la **VAS** (Valutazione Ambientale Strategica).

## Vincoli e loro decadenza

I vincoli preordinati all'esproprio (es. aree destinate a servizi pubblici) hanno durata **quinquennale**: se non attuati **decadono** e l'area diventa "zona bianca" da ridisciplinare (Corte Cost. 179/1999 sull'indennizzo dei vincoli reiterati).
""",
    },
    {
        "slug": "zone-omogenee-standard",
        "category": "urbanistica",
        "title": "Zone omogenee (DM 1444/68) e standard urbanistici",
        "subtitle": "Zone A–F, dotazioni minime e limiti inderogabili",
        "read_minutes": 9,
        "key_points": [
            "Zone: A storico, B completamento, C espansione, D produttive, E agricole, F attrezzature generali.",
            "Standard residenziale: 18 mq/abitante di spazi pubblici (4,5+2+9+2,5).",
            "Distanza minima tra pareti finestrate antistanti: 10 m; in zona C distacchi legati all'altezza.",
            "Densità e altezze massime differenziate per zona.",
        ],
        "content": """## Perché le zone omogenee

Il **DM 2 aprile 1968, n. 1444** (emanato in attuazione della legge ponte) serve a garantire uno **sviluppo ordinato e dotazioni minime uniformi** su tutto il territorio nazionale. Introduce le **zone territoriali omogenee** e gli **standard**, con valori **inderogabili** (prevalgono anche su previsioni comunali difformi).

## Le zone (art. 2)

- **Zona A** – agglomerati di **interesse storico, artistico e ambientale** (centri storici e nuclei di pregio). Prevalgono conservazione e restauro.
- **Zona B** – parti del territorio **già edificate** anche parzialmente, diverse dalla A: è di *completamento* (si considera edificata quando la superficie coperta esistente è ≥ 1/8 della superficie fondiaria e la densità territoriale supera 1,5 mc/mq).
- **Zona C** – parti **inedificate o scarsamente edificate** destinate a **nuova espansione**.
- **Zona D** – parti per **insediamenti produttivi** (industriali, artigianali, commerciali).
- **Zona E** – parti a uso **agricolo**.
- **Zona F** – parti per **attrezzature e impianti di interesse generale** (ospedali, università, grandi parchi).

## Gli standard urbanistici (art. 3)

Lo **standard** è la **dotazione minima di aree pubbliche per abitante insediato**. Per la **residenza**: minimo **18 mq/abitante**, così ripartiti:

| Destinazione | mq/ab |
|---|---|
| Istruzione (materne, obbligo) | 4,5 |
| Attrezzature di interesse comune | 2,0 |
| Verde attrezzato, gioco e sport | 9,0 |
| Parcheggi pubblici | 2,5 |

Per **insediamenti direzionali e commerciali**: **80 mq ogni 100 mq di superficie lorda di pavimento** (di cui almeno metà a parcheggi). Per le **industrie (zona D)**: almeno **10%** della superficie destinata a spazi pubblici. Nei **centri storici (A)** e nelle **zone C** sopra certe soglie si aggiungono aree per attrezzature di livello superiore (*standard urbanistici generali*, fino a ulteriori mq/ab).

Il calcolo degli **abitanti insediabili** si fa di norma con il parametro **1 abitante = 80–100 mc** (o 25–33 mq di SLP), secondo il regolamento locale.

## Limiti inderogabili (artt. 7–9)

- **Densità edilizia**: massimi differenziati (es. zona B non oltre densità preesistenti; zona C indici stabiliti dal piano).
- **Altezza massima** degli edifici: in zona A non superiore agli edifici circostanti preesistenti; nelle altre zone secondo il piano.
- **Distanze**: distanza minima **10 m tra pareti finestrate** e pareti di edifici antistanti; in **zona C**, se l'altezza supera i 10 m, il distacco tra pareti finestrate dev'essere **almeno pari all'altezza** del fabbricato più alto. Distanza dai confini e dalle strade secondo il piano/Codice della strada.

## Opere di urbanizzazione

Gli standard si realizzano con le **opere di urbanizzazione primaria** (strade, fognature, acqua, energia, illuminazione, parcheggi, verde di quartiere) e **secondaria** (scuole, chiese, impianti sportivi, centri sociali, mercati). Sono il presupposto dell'edificabilità.
""",
    },
    {
        "slug": "piani-attuativi",
        "category": "urbanistica",
        "title": "Piani attuativi ed esecutivi",
        "subtitle": "Dal PRG alla trasformazione: PP, PdL, PEEP, PIP, PdR, PII",
        "read_minutes": 8,
        "key_points": [
            "I piani attuativi danno esecuzione alle previsioni del PRG su ambiti definiti.",
            "Piano Particolareggiato (di iniziativa pubblica) e Piano di Lottizzazione (di iniziativa privata, con convenzione).",
            "PEEP (edilizia economica e popolare) e PIP (insediamenti produttivi) sono piani 'per zone'.",
            "I Programmi Integrati di Intervento (PII) introducono complessità funzionale e negoziazione.",
        ],
        "content": """## Funzione dei piani attuativi

Il PRG è in gran parte **non immediatamente operativo** nelle zone di trasformazione: rinvia a **piani attuativi (o esecutivi)** che, su ambiti delimitati, definiscono l'assetto di dettaglio (lotti, allineamenti, aree per standard, opere di urbanizzazione, tempi e modalità). Solo dopo l'approvazione del piano attuativo si può edificare in tali ambiti.

## I principali strumenti

- **Piano Particolareggiato (PP)** – *iniziativa pubblica* (L. 1150/42, art. 13): lo strumento classico di dettaglio; può comportare **esproprio** delle aree. Ha efficacia a termine (di norma 10 anni).
- **Piano di Lottizzazione (PdL)** – *iniziativa privata* (art. 28), con **convenzione** che regola cessione di aree per standard, realizzazione delle opere di urbanizzazione a carico del lottizzante e relative garanzie (fideiussione). È l'alternativa privata al PP.
- **Piano per l'Edilizia Economica e Popolare (PEEP)** – L. 167/1962: individua aree per edilizia sociale, con possibilità di esproprio e assegnazione (in proprietà o diritto di superficie).
- **Piano per gli Insediamenti Produttivi (PIP)** – L. 865/1971, art. 27: analogo al PEEP ma per attività produttive.
- **Piano di Recupero (PdR)** – L. 457/1978: per il recupero del patrimonio edilizio e urbanistico esistente nelle zone di recupero.
- **Programma Integrato di Intervento (PII / PRU / PRUSST)** – L. 179/1992 e successive: strumenti **complessi** che mescolano funzioni (residenza, servizi, attività) e soggetti pubblici/privati, con logica **negoziale** e perequativa.

## Contenuti tipici

Un piano attuativo comprende: **planimetria di zonizzazione di dettaglio**, sedime degli edifici e allineamenti, aree per **urbanizzazione e standard**, profili e sezioni, **norme tecniche**, **relazione**, **computo** delle opere e **schema di convenzione**. Deve rispettare gli **indici e le prescrizioni del PRG** e gli standard del DM 1444/68.

## La convenzione urbanistica

Nei piani di iniziativa privata la **convenzione** (atto pubblico) disciplina: cessione gratuita delle aree per opere di urbanizzazione primaria e secondaria, **esecuzione diretta** delle opere di urbanizzazione (scomputabili dagli oneri), tempi di attuazione, **garanzie finanziarie**, obblighi di manutenzione fino alla presa in carico dal Comune.

## Comparti e attuazione unitaria

Il **comparto edificatorio** consente l'attuazione **unitaria** di un ambito con più proprietari, favorendo la **perequazione** (equa distribuzione di diritti edificatori e oneri). Chi non aderisce può essere espropriato o "riequilibrato" con meccanismi consortili.
""",
    },
    {
        "slug": "opere-urbanizzazione-oneri",
        "category": "urbanistica",
        "title": "Opere di urbanizzazione e contributo di costruzione",
        "subtitle": "Oneri di urbanizzazione, costo di costruzione, Legge Tognoli",
        "read_minutes": 7,
        "key_points": [
            "Urbanizzazione primaria (strade, reti, parcheggi) e secondaria (scuole, chiese, sport).",
            "Il contributo di costruzione = oneri di urbanizzazione + costo di costruzione (L. 10/1977).",
            "Le opere di urbanizzazione realizzate direttamente sono scomputabili dagli oneri.",
            "Legge Tognoli 122/1989: 1 mq di parcheggio ogni 10 mc di costruzione.",
        ],
        "content": """## Le opere di urbanizzazione

Sono le infrastrutture che rendono un'area **effettivamente edificabile e vivibile**.

- **Urbanizzazione primaria**: strade residenziali, spazi di sosta e **parcheggi**, **fognature**, rete idrica, rete di distribuzione di energia elettrica e gas, pubblica illuminazione, spazi di verde attrezzato, infrastrutture di comunicazione.
- **Urbanizzazione secondaria**: asili e scuole dell'obbligo, mercati di quartiere, delegazioni comunali, chiese e edifici religiosi, impianti sportivi di quartiere, centri sociali e attrezzature culturali/sanitarie, aree verdi di quartiere.

## Il contributo di costruzione

Con la **Legge 28 gennaio 1977, n. 10 (Bucalossi)** l'attività edificatoria è **onerosa** (oggi art. 16 DPR 380/2001). Il **contributo di costruzione** è composto da:

1. **Oneri di urbanizzazione** (primaria + secondaria): commisurati al **carico urbanistico** indotto, secondo tabelle parametriche regionali/comunali aggiornate periodicamente.
2. **Costo di costruzione**: quota percentuale del costo dell'intervento (per la residenza) o dell'incidenza per usi diversi.

## Scomputo e realizzazione diretta

Il titolare del permesso può **realizzare direttamente** le opere di urbanizzazione (specie nei piani attuativi), **scomputando** il relativo importo dagli oneri dovuti; le opere vengono poi **cedute** al Comune. Sopra soglia, la realizzazione segue regole del Codice dei contratti.

## Casi di gratuità / riduzione

Alcuni interventi possono essere **gratuiti o ridotti**: opere pubbliche o di interesse generale, edilizia con finalità sociali in certi casi, manutenzione straordinaria in edilizia libera, interventi di riuso/rigenerazione incentivati dalle leggi regionali.

## Standard privati: i parcheggi pertinenziali

- **Legge 6 agosto 1967 n.765 (art. 41-sexies L.1150/42)**: dotazione di parcheggi nelle nuove costruzioni.
- **Legge 24 marzo 1989 n. 122 (Tognoli)**: eleva la dotazione a **1 mq ogni 10 mc** di costruzione (≈ oggi il riferimento comune), consentendo parcheggi pertinenziali anche nel sottosuolo e in deroga agli strumenti urbanistici. Questi parcheggi **pertinenziali** non possono essere ceduti separatamente dall'unità immobiliare.
""",
    },
    {
        "slug": "perequazione-compensazione",
        "category": "urbanistica",
        "title": "Perequazione, compensazione e premialità",
        "subtitle": "Diritti edificatori, crediti e incentivi nella pianificazione moderna",
        "read_minutes": 7,
        "key_points": [
            "La perequazione distribuisce equamente diritti edificatori e oneri tra i proprietari.",
            "La compensazione attribuisce crediti edificatori in cambio di aree o rinunce.",
            "La premialità concede incentivi volumetrici a fronte di qualità/interesse pubblico.",
            "Strumenti nati per superare la disparità di trattamento della zonizzazione tradizionale.",
        ],
        "content": """## Il limite della zonizzazione tradizionale

La zonizzazione classica genera **disparità**: il proprietario di un lotto edificabile si arricchisce, quello la cui area è destinata a standard (verde, servizi) subisce un vincolo ablatorio. Per correggere questa iniquità la pianificazione contemporanea usa **perequazione, compensazione e premialità**, spesso disciplinate dalle leggi regionali.

## Perequazione urbanistica

La **perequazione** attribuisce a tutte le aree di un ambito un **indice di edificabilità uniforme** (o differenziato per stato di fatto/di diritto), indipendentemente dalla destinazione specifica. I proprietari **concentrano** la volumetria sulle aree edificabili (*lotti di atterraggio*) e **cedono** al Comune, in cambio, le aree destinate a servizi e standard. Tutti partecipano in proporzione sia ai **vantaggi** (diritti edificatori) sia agli **oneri** (cessioni, opere). Richiede spesso l'attuazione per **comparti**.

## Compensazione

La **compensazione** riconosce al proprietario, in luogo dell'esproprio o a fronte della cessione di un'area, un **credito edificatorio** (una volumetria) spendibile altrove nel territorio comunale. È utile per acquisire aree per opere pubbliche **senza esborso monetario**, "pagando" in diritti edificatori. I **crediti edificatori** sono trasferibili e commerciabili (registrati in appositi registri).

## Premialità (incentivazione)

La **premialità** concede **bonus volumetrici** a fronte di prestazioni di **interesse pubblico**: efficienza energetica elevata, edilizia sociale, riqualificazione, demolizione e ricostruzione, cessione di aree, rimozione di elementi incongrui. È il motore di molte politiche di **rigenerazione urbana**.

## Riferimenti

Questi istituti trovano fondamento nelle **leggi regionali** e in norme statali sui diritti edificatori (l'art. 2643 c.c. n. 2-bis riconosce la trascrivibilità dei contratti che trasferiscono diritti edificatori). La giurisprudenza ne ha confermato la legittimità purché fondati su **accordi** e non su imposizioni unilaterali prive di base legale.
""",
    },
    {
        "slug": "vincoli-esproprio",
        "category": "urbanistica",
        "title": "Vincoli urbanistici ed espropriazione",
        "subtitle": "Vincoli conformativi ed espropriativi, decadenza e indennità (DPR 327/2001)",
        "read_minutes": 7,
        "key_points": [
            "Vincoli conformativi (regolano l'uso) vs espropriativi (preordinati all'esproprio).",
            "I vincoli espropriativi durano 5 anni: se non attuati decadono (zona bianca).",
            "Il Testo Unico espropri è il DPR 327/2001.",
            "L'indennità di esproprio deve essere 'seria e congrua' (giurisprudenza CEDU/Corte Cost.).",
        ],
        "content": """## Tipi di vincolo

- **Vincoli conformativi**: definiscono in modo generale e astratto il **regime d'uso** dei suoli (destinazioni di zona, indici, altezze). Non danno diritto a indennizzo perché conformano la proprietà per categorie.
- **Vincoli espropriativi (ablatori)**: incidono su **beni determinati** svuotandone il contenuto economico in vista di un'opera pubblica (es. area destinata a scuola). Sono **preordinati all'esproprio** e soggetti a decadenza.

## Decadenza dei vincoli

I vincoli preordinati all'esproprio (e quelli che comportano inedificabilità sostanziale) hanno efficacia **quinquennale**: se entro 5 anni **non interviene** la dichiarazione di pubblica utilità (o il piano attuativo), il vincolo **decade**. L'area diventa **"zona bianca"** (priva di disciplina), da ripianificare. La **Corte Costituzionale (sent. 179/1999)** ha stabilito che la **reiterazione** di tali vincoli, se azzera il valore del bene, richiede **indennizzo**.

## Il Testo Unico sull'espropriazione

Il **DPR 8 giugno 2001, n. 327** disciplina l'espropriazione per pubblica utilità. Fasi principali:

1. **Apposizione del vincolo** preordinato all'esproprio (tramite il piano).
2. **Dichiarazione di pubblica utilità** (di norma coincide con l'approvazione del progetto dell'opera).
3. **Determinazione dell'indennità** provvisoria e definitiva.
4. **Decreto di esproprio** e immissione in possesso.

## L'indennità di esproprio

Dopo le pronunce della **Corte EDU** e della **Corte Costituzionale (sent. 348 e 349/2007)**, l'indennità per le aree edificabili non può essere irrisoria: deve tendere al **valore venale** del bene (serio ristoro), superando i vecchi criteri riduttivi. Per i suoli agricoli valgono criteri specifici. È prevista la **cessione volontaria** con maggiorazione dell'indennità.

## Occupazione e retrocessione

Sono disciplinate l'**occupazione d'urgenza**, il rischio della vecchia "occupazione acquisitiva" (superata) e la **retrocessione** (il bene può tornare all'espropriato se l'opera non è realizzata o l'area non è utilizzata).
""",
    },
    {
        "slug": "rigenerazione-consumo-suolo",
        "category": "urbanistica",
        "title": "Rigenerazione urbana e consumo di suolo",
        "subtitle": "Riuso, densificazione e limite al consumo di suolo",
        "read_minutes": 6,
        "key_points": [
            "La rigenerazione urbana promuove riuso e riqualificazione del costruito esistente.",
            "Obiettivo UE/nazionale: consumo di suolo netto pari a zero (tendenziale).",
            "Strumenti: premialità, semplificazioni, demolizione e ricostruzione.",
            "Legata a efficienza energetica, sicurezza sismica e qualità urbana.",
        ],
        "content": """## Dal consumo di suolo al riuso

Per decenni l'urbanistica ha governato l'**espansione**. Oggi il paradigma è il **contenimento del consumo di suolo** e la **rigenerazione** della città esistente. L'Unione Europea indica il traguardo del **consumo di suolo netto pari a zero** (tendenzialmente entro il 2050); molte **leggi regionali** fissano limiti quantitativi al nuovo consumo e incentivano il riuso.

## Che cos'è la rigenerazione urbana

È l'insieme di interventi **integrati** (urbanistici, edilizi, sociali, ambientali, economici) volti a **riqualificare ambiti degradati o dismessi** senza nuovo consumo di suolo: recupero di aree industriali dismesse (*brownfield*), densificazione intelligente, miglioramento dello spazio pubblico, mixité funzionale, riqualificazione energetica e sismica del patrimonio.

## Strumenti e leve

- **Premialità volumetriche** per demolizione e ricostruzione con miglioramento prestazionale (energetico, sismico, di qualità architettonica).
- **Semplificazioni procedurali** per gli interventi di riuso.
- **Perequazione e crediti edificatori** per trasferire volumetrie e liberare suoli.
- Coordinamento con il **Superbonus/bonus edilizi** e con i piani di resilienza (PNRR).

## Riferimenti edilizi utili

Il **DPR 380/2001**, modificato nel tempo (es. *decreto Semplificazioni* 76/2020), favorisce il riuso: ammette la **ristrutturazione edilizia** con demolizione e ricostruzione anche con diversa sagoma e sedime (fuori dai centri storici e salvo vincoli), e introduce la **tolleranza costruttiva** e lo **stato legittimo** dell'immobile. Le leggi regionali sulla rigenerazione completano il quadro con incentivi e deroghe mirate.

## Qualità e sostenibilità

La rigenerazione si misura su **qualità urbana** (spazi pubblici, verde, accessibilità), **sostenibilità ambientale** (permeabilità dei suoli, invarianza idraulica, isole di calore) e **inclusione sociale** (housing sociale, servizi di prossimità).
""",
    },
    {
        "slug": "parametri-edilizi-urbanistici",
        "category": "urbanistica",
        "title": "Parametri e indici urbanistico-edilizi",
        "subtitle": "Superfici, volumi, indici di edificabilità, rapporto di copertura",
        "read_minutes": 7,
        "key_points": [
            "Indice territoriale (IT) si applica alla superficie territoriale; fondiario (IF) alla fondiaria.",
            "Superficie territoriale = fondiaria + aree per urbanizzazione.",
            "Rapporto di copertura RC = superficie coperta / superficie fondiaria.",
            "Il Regolamento Edilizio Tipo (RET 2016) ha uniformato molte definizioni.",
        ],
        "content": """## Perché i parametri contano

Gran parte dei **quesiti di progettazione** e delle verifiche urbanistiche ruota attorno a **indici e parametri**: sapere cosa si applica e a quale superficie è essenziale. Le **definizioni uniformi** sono state fissate dal **Regolamento Edilizio Tipo (Intesa Stato-Regioni 2016)**, recepito dalle Regioni.

## Le superfici di riferimento

- **Superficie Territoriale (ST)**: l'intera area interessata da un piano attuativo, comprensiva delle aree per urbanizzazione e standard.
- **Superficie Fondiaria (SF)**: la ST **al netto** delle aree per opere di urbanizzazione; è la parte effettivamente edificabile.
- **Superficie Coperta (SC)**: proiezione a terra dell'ingombro dell'edificio (esclusi aggetti minori).
- **Superficie Utile (SU)** e **Superficie Lorda (SL/SLP)**: superficie dei pavimenti, netta o lorda dei muri, usata per calcolare capacità edificatoria e oneri.

## Gli indici di edificabilità

- **Indice di edificabilità territoriale (IT)** [mc/mq o mq/mq]: si applica alla **ST**; esprime la capacità edificatoria complessiva dell'ambito.
- **Indice di edificabilità fondiaria (IF)** [mc/mq o mq/mq]: si applica alla **SF**; è più alto dell'IT perché riferito alla sola area edificabile.

Esempio: SF = 1.000 mq, IF = 1,5 mc/mq → **Volume edificabile = 1.500 mc**. Con 100 mc/abitante → 15 abitanti insediabili.

## Rapporto di copertura e altre grandezze

- **Rapporto di Copertura (RC)** = **SC / SF** (spesso espresso in %). Esempio: SF = 800 mq, RC = 40% → SC max = 320 mq.
- **Altezza (H)**: dell'edificio e dei fronti; regola distanze e rispetto degli allineamenti.
- **Distanze**: dai confini, tra edifici (≥10 m tra pareti finestrate, DM 1444), dalle strade (Codice della strada e fasce di rispetto).
- **Volume (V)**: prodotto di SLP per altezza virtuale o somma dei volumi dei piani; base per oneri e abitanti.

## Vincoli e fasce di rispetto

Nel dimensionamento vanno considerati **vincoli** (paesaggistici, idrogeologici, cimiteriali, stradali, ferroviari, elettrodotti) e le relative **fasce di rispetto**, che riducono la superficie utile del lotto.
""",
    },
    # ------------------------------------------------------------------ EDILIZIA
    {
        "slug": "titoli-abilitativi",
        "category": "edilizia",
        "title": "Titoli abilitativi: PdC, SCIA, CILA, edilizia libera",
        "subtitle": "Il DPR 380/2001 (Testo Unico dell'Edilizia)",
        "read_minutes": 9,
        "key_points": [
            "Testo Unico dell'Edilizia: DPR 380/2001.",
            "Categorie di intervento (art. 3): MO, MS, restauro/risanamento, ristrutturazione, nuova costruzione, ristrutturazione urbanistica.",
            "Titoli: Permesso di Costruire, SCIA (e super-SCIA), CILA; edilizia libera senza titolo.",
            "Abuso edilizio: sanzioni pecuniarie o demolizione; fiscalizzazione solo se la demolizione pregiudica il legittimo.",
        ],
        "content": """## Il Testo Unico dell'Edilizia

Il **DPR 6 giugno 2001, n. 380** raccoglie e coordina la disciplina dell'attività edilizia. Distingue le **categorie di intervento** (art. 3) e i **titoli abilitativi** necessari.

## Le categorie di intervento (art. 3)

- **Manutenzione ordinaria (MO)**: riparazione, rinnovo e sostituzione di finiture; integrazione/mantenimento degli impianti.
- **Manutenzione straordinaria (MS)**: opere per rinnovare o sostituire parti anche **strutturali**, realizzare/integrare servizi, **senza** aumento di volume complessivo né mutamento di destinazione d'uso. Include il frazionamento/accorpamento con opere se non muta la volumetria complessiva.
- **Restauro e risanamento conservativo**: conservano l'organismo edilizio assicurandone la funzionalità nel rispetto degli elementi tipologici, formali e strutturali.
- **Ristrutturazione edilizia**: interventi volti a trasformare l'organismo edilizio, anche con **demolizione e ricostruzione** (con la disciplina vigente su sagoma/sedime e vincoli). Può essere "leggera" o "pesante".
- **Nuova costruzione**: trasformazione edilizia e urbanistica del territorio non rientrante nelle precedenti (nuovi edifici, ampliamenti, infrastrutture, depositi, ecc.).
- **Ristrutturazione urbanistica**: sostituzione del tessuto urbanistico-edilizio con modifica di lotti, isolati e rete stradale.

## I titoli abilitativi

- **Permesso di Costruire (PdC)** – art. 10: per **nuova costruzione**, **ristrutturazione urbanistica** e **ristrutturazione edilizia "pesante"** (che porti a organismo diverso con aumento di unità, modifiche di volume/sagoma o, in zona vincolata, dei prospetti). È **oneroso**.
- **SCIA** – *Segnalazione Certificata di Inizio Attività* (artt. 22-23): per MS strutturale, restauro/risanamento, ristrutturazione "leggera". Si **inizia subito** con asseverazione del tecnico. La **SCIA alternativa al PdC** ("super-SCIA") copre gli interventi che potrebbero richiedere PdC nei casi individuati dalla legge.
- **CILA** – *Comunicazione Inizio Lavori Asseverata* (art. 6-bis): regime **residuale** per gli interventi non riconducibili all'edilizia libera né agli altri titoli; tipicamente MS **non strutturale** e opere interne.
- **Edilizia libera** – art. 6: MO, opere temporanee, pompe di calore, pannelli solari, ecc., **senza titolo** (fatte salve altre autorizzazioni, es. paesaggistica).

Il **Glossario dell'edilizia libera** (DM 2018) elenca le opere realizzabili liberamente.

## Agibilità e stato legittimo

La fine lavori è seguita dalla **segnalazione certificata di agibilità** (art. 24). Lo **stato legittimo** dell'immobile (titolo che ne ha consentito la costruzione + titoli successivi) è oggi condizione per molti interventi e per la commerciabilità.

## Abuso edilizio e sanzioni

Gli abusi sono graduati: **assenza/difformità totale** dal PdC → **demolizione** e acquisizione al patrimonio comunale; **difformità parziale** → demolizione o, se pregiudica la parte legittima, **sanzione pecuniaria** (*fiscalizzazione*); interventi senza SCIA/CILA → sanzioni pecuniarie. In zona vincolata le sanzioni sono più severe. Il **condono edilizio** è misura eccezionale e straordinaria (leggi ad hoc del 1985, 1994, 2003), distinto dalla **sanatoria** ordinaria (art. 36, doppia conformità).
""",
    },
    # ------------------------------------------------------------------ STRUTTURE
    {
        "slug": "ntc-2018-stati-limite",
        "category": "strutture",
        "title": "NTC 2018: stati limite e azioni sulle costruzioni",
        "subtitle": "Metodo semiprobabilistico agli stati limite (SLU/SLE)",
        "read_minutes": 8,
        "key_points": [
            "NTC 2018 = DM 17/01/2018; metodo semiprobabilistico agli stati limite.",
            "SLU: sicurezza/collasso; SLE: esercizio (deformazioni, fessurazione, comfort).",
            "Verifica: E_d ≤ R_d con coefficienti parziali su azioni (γ_F) e materiali (γ_M).",
            "Vita nominale, classe d'uso e periodo di riferimento V_R = V_N·C_U governano il sisma.",
        ],
        "content": """## Il quadro normativo

Le **Norme Tecniche per le Costruzioni (DM 17 gennaio 2018)**, con la **Circolare esplicativa 7/2019**, disciplinano progettazione, esecuzione e collaudo. Adottano il **metodo semiprobabilistico agli stati limite** con **coefficienti parziali di sicurezza**.

## Il principio di verifica

La sicurezza si esprime confrontando **domanda e capacità**:

> **E_d ≤ R_d**

dove **E_d** è l'effetto delle azioni di progetto (amplificate da γ_F) e **R_d** la resistenza di progetto (materiali ridotti da γ_M). Il metodo "semiprobabilistico" usa **valori caratteristici** (frattili) e coefficienti che tengono conto delle incertezze.

## Stati limite

- **SLU – Stati Limite Ultimi**: riguardano la **sicurezza** (perdita di equilibrio EQU, resistenza STR, geotecnica GEO, fatica, instabilità). Il superamento comporta crolli o danni gravi.
- **SLE – Stati Limite di Esercizio**: riguardano la **funzionalità e la durabilità** in condizioni d'uso (deformazioni e frecce, ampiezza delle fessure, vibrazioni e comfort, tenuta).

## Le azioni

Classificate in **permanenti (G1 strutturali, G2 non strutturali)**, **variabili (Q)** (di esercizio, neve, vento, temperatura), **eccezionali (A)** (urti, esplosioni, incendio) e **sismiche (E)**. Ogni azione ha un **valore caratteristico** e valori ridotti tramite i coefficienti **ψ0, ψ1, ψ2**.

## Le combinazioni

- **Fondamentale (SLU)**: γ_G1·G1 + γ_G2·G2 + γ_Q1·Q_k1 + Σ γ_Qi·ψ_0i·Q_ki.
- **Caratteristica (rara), frequente, quasi permanente (SLE)**: con ψ crescenti di riduzione.
- **Sismica**: E + G1 + G2 + Σ ψ_2i·Q_ki (le variabili entrano col valore quasi permanente).

## Sicurezza nel tempo

- **Vita Nominale di progetto (V_N)**: ≥10, ≥50, ≥100 anni secondo il tipo di opera.
- **Classe d'uso (I–IV)**: in funzione dell'affollamento e della strategicità (C_U = 0,7 / 1,0 / 1,5 / 2,0).
- **Periodo di riferimento**: **V_R = V_N · C_U**, da cui si ricavano le azioni sismiche (probabilità di superamento negli stati limite SLO, SLD, SLV, SLC).

## Metodi di analisi

Analisi **statica lineare**, **dinamica modale**, **statica non lineare (pushover)** e **dinamica non lineare**, scelte in base a regolarità e importanza dell'opera.
""",
    },
    {
        "slug": "materiali-predimensionamento",
        "category": "strutture",
        "title": "Materiali strutturali e predimensionamento",
        "subtitle": "Calcestruzzo armato, acciaio, legno, muratura",
        "read_minutes": 7,
        "key_points": [
            "Il c.a. abbina calcestruzzo (compressione) e acciaio (trazione); classi es. C25/30, B450C.",
            "Acciaio (S235/S275/S355): duttile, attenzione a instabilità e collegamenti.",
            "Regole: trave h≈L/10, solaio h≈L/25, sbalzo h≈L/8.",
            "La muratura resiste a compressione; in sisma ordinaria o armata.",
        ],
        "content": """## Calcestruzzo armato (c.a.)

Materiale composito: il **calcestruzzo** resiste bene a **compressione**, l'**acciaio** delle armature alla **trazione** (e integra la compressione). Classe indicata come **C25/30** (resistenza caratteristica cilindrica/cubica in MPa); acciaio da c.a. tipico **B450C** (f_yk = 450 MPa, duttile). Il **copriferro** (regolato in base a classe di esposizione e durabilità) protegge le armature da **corrosione** e **fuoco**. Il c.a. ha buona **resistenza al fuoco** e massa (utile in acustica), ma peso elevato.

## Acciaio

Ottimo rapporto resistenza/peso, **duttile**, adatto a grandi luci e prefabbricazione. Gradi comuni **S235, S275, S355**. Criticità: **instabilità** delle aste compresse (verifiche di svergolamento e carico di punta), **collegamenti** (bullonati o saldati) e **protezione al fuoco** (vernici intumescenti, rivestimenti) e alla corrosione.

## Legno

Leggero, rinnovabile, buone prestazioni; **massiccio** o **lamellare incollato (glulam)**, oltre a X-Lam (CLT) per pannelli. Va controllata l'**umidità** e la **durabilità**; il comportamento al fuoco è governato dalla **velocità di carbonizzazione** (lo strato carbonizzato protegge il nucleo, consentendo un dimensionamento prevedibile).

## Muratura

Resiste soprattutto a **compressione**, poco a trazione e taglio. Fondamentale nell'esistente e nei centri storici. In zona sismica si distinguono **muratura ordinaria** e **muratura armata**; importanti la **qualità della muratura** e i **collegamenti** (cordoli, catene) per evitare meccanismi di ribaltamento.

## Regole di predimensionamento (valori di primo tentativo)

- **Trave in c.a.**: h ≈ **L/10 ÷ L/12**; base b ≈ h/2.
- **Solaio** latero-cementizio: h ≈ **L/25** (≈ 20–30 cm per luci correnti), con soletta 4–5 cm.
- **Sbalzo/mensola**: h ≈ **L/8** (più rigido per contenere le frecce).
- **Pilastro**: dimensionato allo **sforzo normale** N con tensione di lavoro ammissibile del cls e controllo di **snellezza** (λ) per l'instabilità.
- **Travi in acciaio**: h ≈ **L/18 ÷ L/20** (profili IPE/HE).

Il predimensionamento fornisce dimensioni iniziali da **verificare** poi agli SLU e SLE (frecce, fessurazione).
""",
    },
    # ------------------------------------------------------------------ SISMICA
    {
        "slug": "criteri-antisismici",
        "category": "sismica",
        "title": "Progettazione in zona sismica",
        "subtitle": "Classificazione, spettri, duttilità, gerarchia delle resistenze",
        "read_minutes": 8,
        "key_points": [
            "OPCM 3274/2003: 4 zone sismiche su tutto il territorio.",
            "L'azione sismica dipende da a_g, categoria di sottosuolo e topografia (spettri).",
            "Capacity design: attivare i meccanismi duttili prima dei fragili.",
            "Regolarità in pianta/elevazione e interventi su esistente (adeguamento/miglioramento/locale).",
        ],
        "content": """## Classificazione sismica

Con l'**OPCM 3274/2003** l'intero territorio è stato suddiviso in **4 zone sismiche** (1 = pericolosità massima → 4 = minima). Le NTC 2018 definiscono l'azione non più solo per "zona" ma in funzione della **pericolosità del sito** (reticolo di riferimento), della **categoria di sottosuolo (A–E)** e delle **condizioni topografiche (T1–T4)**.

## L'azione sismica e gli spettri

L'azione è descritta da **spettri di risposta** in accelerazione, funzione di:
- **a_g**: accelerazione orizzontale massima attesa al suolo rigido;
- **periodo di riferimento V_R** e **stato limite** considerato (SLO, SLD di esercizio; SLV, SLC ultimi), ciascuno con una **probabilità di superamento**;
- amplificazione **stratigrafica (S_S)** e **topografica (S_T)**.

## Comportamento dissipativo e fattore di comportamento

Un edificio ben concepito **dissipa energia** deformandosi in campo plastico. Il **fattore di comportamento q** riduce le forze elastiche in funzione della capacità dissipativa: **CD"A" (alta duttilità)** e **CD"B" (media duttilità)**. A maggiore q corrisponde una progettazione più curata dei dettagli duttili.

## Gerarchia delle resistenze (capacity design)

Principio cardine: **garantire che i meccanismi duttili precedano quelli fragili**. Si progetta "**trave debole – pilastro forte**", si sovradimensiona il **taglio** rispetto alla flessione e si proteggono i **nodi**, per evitare collassi improvvisi e il temuto **piano soffice** (piano debole con pilastri che collassano).

## Regolarità strutturale

- **In pianta**: forma compatta e simmetrica, distribuzione uniforme di masse e rigidezze, **baricentro delle masse vicino al centro delle rigidezze** (riduce la **torsione**).
- **In elevazione**: continuità di masse, rigidezze e resistenze lungo l'altezza, senza bruschi restringimenti o interruzioni di elementi sismoresistenti.

Elementi utili: **giunti sismici** tra corpi di fabbrica, **controventi**, **setti** in c.a., dettagli costruttivi duttili (staffe fitte nelle zone critiche).

## Interventi sull'esistente

Le NTC distinguono:
- **Adeguamento**: riportare l'edificio ai **livelli di sicurezza** richiesti dalla norma (obbligatorio in casi definiti: sopraelevazioni, ampliamenti, cambi d'uso gravosi, interventi che aumentano i carichi >10%).
- **Miglioramento**: aumentare la sicurezza **senza** raggiungere il pieno adeguamento (tipico per i beni tutelati).
- **Riparazione/intervento locale**: interessa singoli elementi senza modificare il comportamento globale.

La **valutazione della sicurezza** quantifica il rapporto tra capacità e domanda (indicatori ζ_E).
""",
    },
    # ------------------------------------------------------------------ INCENDI
    {
        "slug": "prevenzione-incendi",
        "category": "incendi",
        "title": "Prevenzione incendi: principi e Codice PI",
        "subtitle": "Strategia antincendio, resistenza al fuoco (REI), esodo",
        "read_minutes": 7,
        "key_points": [
            "Codice di Prevenzione Incendi: DM 3 agosto 2015 (approccio prestazionale).",
            "REI: R stabilità, E tenuta, I isolamento; il numero = minuti.",
            "Strategia: reazione/resistenza al fuoco, compartimentazione, esodo, rivelazione, controllo fumi.",
            "Attività soggette elencate nel DPR 151/2011 (cat. A, B, C).",
        ],
        "content": """## Obiettivi e approccio

La prevenzione incendi tutela la **sicurezza delle persone** e limita i danni a beni e ambiente. Il **DM 3 agosto 2015 – Codice di Prevenzione Incendi (RTO, Regola Tecnica Orizzontale)** ha introdotto un metodo **prestazionale e flessibile**, alternativo alle vecchie regole prescrittive, applicabile alle attività con specifiche **regole tecniche verticali (RTV)**.

## La valutazione del rischio e il profilo

Si valuta il rischio in base a: **profilo di rischio vita (R_vita)** (in funzione di occupanti e velocità di crescita dell'incendio), **rischio beni (R_beni)** e **rischio ambiente (R_ambiente)**. Da qui si scelgono i **livelli di prestazione** delle misure.

## Le misure antincendio (S.1–S.10)

1. **Reazione al fuoco** dei materiali (euroclassi A1–F).
2. **Resistenza al fuoco** delle strutture, con la sigla **REI**:
   - **R** = capacità portante (stabilità),
   - **E** = tenuta a fiamme e fumi caldi,
   - **I** = isolamento termico.
   Il numero (**REI 30/60/90/120**) indica i **minuti** garantiti. Si usano anche **R** (solo portante) ed **EI** (solo separante).
3. **Compartimentazione**: suddivisione in **compartimenti** con elementi REI e distanze di separazione per limitare la propagazione.
4. **Esodo**: vie d'uscita, **larghezze** (moduli), **lunghezze massime**, numero e ubicazione delle uscite, luoghi sicuri; dimensionato sull'**affollamento**.
5. **Gestione della sicurezza antincendio (GSA)**.
6. **Controllo dell'incendio**: estintori, rete idranti, impianti **sprinkler**.
7. **Rivelazione e allarme (IRAI)**.
8. **Controllo di fumi e calore (SEFC)**: aperture ed evacuatori.
9. **Operatività antincendio** (accessibilità mezzi di soccorso).
10. **Sicurezza degli impianti tecnologici**.

## Il carico d'incendio

Il **carico d'incendio specifico di progetto q_f,d** [MJ/m²] misura l'**energia termica** dei combustibili presenti (corretta da fattori di rischio e protezione) e determina la **classe del compartimento** e quindi la **resistenza al fuoco** richiesta.

## Procedure amministrative

Le **attività soggette** ai controlli dei Vigili del Fuoco sono elencate nel **DPR 151/2011** in categorie **A, B, C** (rischio crescente). L'iter prevede, secondo i casi, **valutazione del progetto**, **SCIA antincendio** e **controlli/sopralluoghi**, con rinnovo periodico e attestazioni di rinnovo.
""",
    },
    # ------------------------------------------------------------------ ENERGETICO
    {
        "slug": "efficienza-energetica-ape",
        "category": "energetico",
        "title": "Contenimento energetico e APE",
        "subtitle": "Involucro, trasmittanza, NZEB e certificazione",
        "read_minutes": 7,
        "key_points": [
            "Norme base: D.Lgs. 192/2005 e decreti requisiti minimi (DM 26/6/2015); NZEB.",
            "Trasmittanza U (W/m²K): più bassa, più isolante; U-limite per zona climatica (A–F).",
            "APE: classi da A4 (migliore) a G; redatto da tecnico abilitato e indipendente.",
            "Controllo di ponti termici, inerzia estiva e condensa (verifica di Glaser).",
        ],
        "content": """## Quadro normativo

L'efficienza energetica degli edifici deriva dalle direttive europee **EPBD**, recepite con il **D.Lgs. 192/2005** e attuate dai **decreti requisiti minimi (DM 26 giugno 2015)**, che introducono l'**edificio a energia quasi zero (NZEB)** come standard per i nuovi edifici. Il **D.Lgs. 199/2021** disciplina le **fonti rinnovabili** e le quote obbligatorie; il **D.Lgs. 48/2020** aggiorna la EPBD.

## Le dispersioni e la trasmittanza

Le perdite avvengono attraverso l'**involucro** (pareti, coperture, solai contro terra/verso non riscaldato, serramenti) e per **ventilazione**. La **trasmittanza termica U** [W/m²K] quantifica il calore che attraversa un componente per m² e per grado di differenza di temperatura: **U bassa = migliore isolamento**. I decreti fissano **U-limite** per **zona climatica** (dalla **A**, più calda, alla **F**, più fredda, definite in **gradi giorno GG**).

## Ponti termici, inerzia, condensa

- **Ponti termici**: discontinuità dell'isolamento (balconi, pilastri, spallette) da limitare per evitare dispersioni e muffe; il **cappotto** continuo li riduce.
- **Inerzia termica** e **sfasamento**: importanti per il **comfort estivo** (attenuazione dell'onda termica); rilevano massa e capacità termica.
- **Condensa interstiziale**: si verifica con il **diagramma di Glaser**; la corretta successione degli strati (barriera al vapore sul lato caldo) la previene.

## Impianti ed energia rinnovabile

Efficienza dell'impianto di climatizzazione (**pompe di calore**, caldaie a condensazione), **ventilazione meccanica controllata (VMC)** con recupero, **solare termico** e **fotovoltaico**. I nuovi edifici devono coprire **quote minime** dei consumi con fonti rinnovabili.

## L'Attestato di Prestazione Energetica (APE)

L'**APE** esprime la prestazione in **classi da A4 (migliore) a G (peggiore)**, in base all'indice **EP_gl,nren** (energia primaria globale non rinnovabile). È **obbligatorio** in caso di **vendita, locazione, nuova costruzione e ristrutturazione importante** e dev'essere redatto da un **tecnico abilitato e indipendente** (certificatore). Va **allegato** ai contratti e ne va riportata la classe negli annunci. L'APE non va confuso con la **diagnosi energetica** (audit più dettagliato per interventi).
""",
    },
    # ------------------------------------------------------------------ ACUSTICA
    {
        "slug": "acustica-edilizia",
        "category": "acustica",
        "title": "Acustica in edilizia",
        "subtitle": "Requisiti acustici passivi (DPCM 5/12/1997) e zonizzazione",
        "read_minutes": 6,
        "key_points": [
            "Legge quadro: L. 447/1995; requisiti acustici passivi: DPCM 5/12/1997.",
            "Parametri: R'w (partizioni), D2m,nT,w (facciata), L'n,w (calpestio), LAS/LAeq (impianti).",
            "Zonizzazione acustica comunale in 6 classi (I–VI).",
            "Soluzioni: massa, sistemi massa-molla-massa, pavimenti galleggianti, fonoassorbenti.",
        ],
        "content": """## Quadro normativo

La **Legge 26 ottobre 1995, n. 447** è la legge quadro sull'**inquinamento acustico**. Il **DPCM 5 dicembre 1997** fissa i **requisiti acustici passivi degli edifici**, differenziati per **categoria** (A residenze, B uffici, C alberghi, D ospedali/scuole, ecc.). Altri riferimenti: DPCM 14/11/1997 (valori limite delle sorgenti) e la norma UNI 11367 sulla classificazione acustica delle unità immobiliari.

## I parametri fondamentali

- **R'w** – indice del **potere fonoisolante apparente** tra ambienti (partizioni interne): più alto è, migliore l'isolamento.
- **D2m,nT,w** – **isolamento acustico standardizzato di facciata** (rumore esterno).
- **L'n,w** – **livello di rumore da calpestio** dei solai: **più è basso, meglio è**.
- **LASmax** e **LAeq** – livelli **massimo** ed **equivalente** per il rumore degli **impianti** a funzionamento **discontinuo** (ascensori, scarichi) e **continuo** (riscaldamento, ventilazione).

## Zonizzazione acustica

I Comuni classificano il territorio in **6 classi acustiche (I–VI)**: dalle **aree particolarmente protette (I)** (ospedali, scuole) alle **aree esclusivamente industriali (VI)**, fissando i **valori limite** di immissione ed emissione **diurni e notturni**. La compatibilità tra classi contigue evita salti eccessivi.

## Strategie progettuali

- **Legge di massa**: a parità di frequenza, più massa = più isolamento (raddoppiando la massa si guadagnano ~5–6 dB).
- **Sistemi massa-molla-massa** (doppie pareti con intercapedine e materiale fonoassorbente): prestazioni elevate a parità di peso.
- **Pavimenti galleggianti** (massetto desolidarizzato su materassino resiliente) contro il **calpestio**.
- **Materiali fonoassorbenti** per il controllo del **riverbero** interno.
- Cura dei **ponti acustici** (giunti, passaggi impiantistici, cassonetti) che vanificano l'isolamento.
""",
    },
    # ------------------------------------------------------------------ BARRIERE
    {
        "slug": "barriere-architettoniche",
        "category": "barriere",
        "title": "Barriere architettoniche e accessibilità",
        "subtitle": "DM 236/1989 e DPR 503/1996: accessibilità, visitabilità, adattabilità",
        "read_minutes": 6,
        "key_points": [
            "DM 236/1989 (privato/ERP) e DPR 503/1996 (edifici pubblici).",
            "Tre livelli: accessibilità > visitabilità > adattabilità.",
            "Rampe: pendenza max 8%; rotazione sedia a ruote Ø 150 cm; porte luce ≥ 80 cm.",
            "In presenza di vincoli va garantito il massimo grado di accessibilità compatibile.",
        ],
        "content": """## I tre livelli di qualità

Il **DM 14 giugno 1989, n. 236** (edilizia privata e residenziale pubblica) definisce:

- **Accessibilità**: possibilità di **raggiungere e fruire ogni** spazio e attrezzatura in sicurezza e autonomia (livello più alto; richiesto negli spazi/collettivi e pubblici).
- **Visitabilità**: possibilità di accedere agli **spazi di relazione** e ad **almeno un servizio igienico** (livello intermedio; tipico di molte destinazioni private aperte al pubblico).
- **Adattabilità**: possibilità di **modificare nel tempo** lo spazio per renderlo accessibile con **costi limitati** (livello minimo; tipico della residenza privata).

Per l'**edilizia pubblica** vale il **DPR 24 luglio 1996, n. 503**; per la progettazione si fa riferimento anche alla **Legge 13/1989** (interventi negli edifici privati e contributi).

## Parametri dimensionali ricorrenti

- **Rampe**: pendenza **massima 8%** (ammesse pendenze superiori solo per brevi dislivelli secondo abaco: es. 12% per rampe fino a 50 cm); **larghezza ≥ 90 cm**; **ripiani di sosta** ogni 10 m e in corrispondenza di cambi di direzione; cordolo e corrimano.
- **Spazio di manovra**: rotazione della sedia a ruote in un cerchio **Ø 150 cm**.
- **Porte**: luce netta **≥ 80 cm** (≥ 75 cm per le interne in adattabilità); maniglie a leva.
- **Ascensore accessibile**: cabina minima (es. **140×110 cm**), porta **≥ 80 cm**, bottoniera a norma.
- **Servizi igienici**: spazio di accostamento **laterale** al WC (≥ 100 cm) e frontale al lavabo; maniglioni.
- **Corridoi e percorsi**: larghezza adeguata, assenza di gradini isolati, **segnalazioni tattili** e contrasti cromatici per gli ipovedenti.

## Vincoli e soluzioni alternative

Anche in presenza di **vincoli** (beni tutelati, impossibilità tecnica) va ricercata la soluzione che garantisca il **massimo grado di accessibilità compatibile**, ricorrendo a **soluzioni alternative** (servoscala, piattaforme elevatrici) quando quelle standard non sono praticabili, purché di pari efficacia funzionale.
""",
    },
    # ------------------------------------------------------------------ APPALTI
    {
        "slug": "codice-appalti",
        "category": "appalti",
        "title": "Appalti e contratti pubblici",
        "subtitle": "Il nuovo Codice D.Lgs. 36/2023: principi, livelli, procedure",
        "read_minutes": 8,
        "key_points": [
            "Codice vigente: D.Lgs. 36/2023 (sostituisce il D.Lgs. 50/2016).",
            "Principi guida: risultato, fiducia, accesso al mercato.",
            "Due livelli di progettazione: PFTE ed Esecutivo.",
            "Procedure: aperta, ristretta, negoziata, affidamento diretto (sottosoglia); criteri OEPV/minor prezzo.",
        ],
        "content": """## Il nuovo Codice

Il **Codice dei Contratti Pubblici – D.Lgs. 31 marzo 2023, n. 36** (in vigore dal 1° luglio 2023, con allegati "autoesecutivi") ha sostituito il **D.Lgs. 50/2016**. Disciplina appalti e concessioni di **lavori, servizi e forniture**.

## I principi

- **Principio del risultato**: la PA deve perseguire il miglior risultato possibile (tempestività, qualità, prezzo) — criterio interpretativo prioritario.
- **Principio della fiducia** nell'azione legittima dell'amministrazione e dei suoi funzionari.
- **Principio dell'accesso al mercato** (concorrenza, parità, trasparenza, proporzionalità, pubblicità).

## I livelli di progettazione

Il Codice **riduce a due** i livelli:
1. **Progetto di Fattibilità Tecnico-Economica (PFTE)** — assorbe il vecchio "definitivo" e sviluppa fin dall'inizio scelte localizzative, prestazionali e di sostenibilità.
2. **Progetto Esecutivo** — di dettaglio per l'esecuzione.

Segue la fase di **esecuzione** dei lavori.

## Le procedure di affidamento

- **Procedura aperta**: tutti possono presentare offerta.
- **Procedura ristretta**: con **prequalifica** dei candidati.
- **Procedura competitiva con negoziazione / negoziata** (con o senza bando).
- **Dialogo competitivo** e **partenariato per l'innovazione** per soluzioni complesse.
- **Sottosoglia** (art. 50): **affidamento diretto** e **procedure negoziate** con numero minimo di operatori, con **principio di rotazione**.

Le **soglie europee** sono periodicamente aggiornate e distinguono il regime sopra/sotto soglia.

## Criteri di aggiudicazione

- **OEPV – Offerta Economicamente Più Vantaggiosa**: miglior **rapporto qualità/prezzo**; **obbligatoria** per i **servizi di ingegneria e architettura** e i servizi ad alta intensità di manodopera.
- **Minor prezzo**: ammesso nei casi definiti (es. lavori standardizzati).

## Figure, esecuzione e collaudo

- **RUP – Responsabile Unico del Progetto**: governa **tutte** le fasi.
- In esecuzione: **Direttore dei Lavori**, direttori operativi, **coordinatore per la sicurezza**.
- A conclusione: **collaudo** tecnico-amministrativo e, ove previsto, **collaudo statico**; per opere minori, **certificato di regolare esecuzione**.
- Strumenti: **accordo quadro**, **concessione**, **PPP (partenariato pubblico-privato)**, **project financing**. Rilevano i **Criteri Ambientali Minimi (CAM)** e la qualificazione delle stazioni appaltanti.
""",
    },
    # ------------------------------------------------------------------ CATASTO
    {
        "slug": "catasto-estimo",
        "category": "catasto",
        "title": "Catasto ed estimo",
        "subtitle": "Catasto terreni e fabbricati, aspetti economici del valore",
        "read_minutes": 8,
        "key_points": [
            "Il Catasto è l'inventario dei beni immobili; è 'non probatorio' (finalità fiscali).",
            "Catasto Terreni (particella) e Fabbricati (unità immobiliare urbana, categorie A–F).",
            "Identificativo: Foglio – Particella (mappale) – Subalterno.",
            "Estimo: 5 aspetti economici del valore; principio dell'ordinarietà e comparazione.",
        ],
        "content": """## Il Catasto

Il **Catasto** è l'**inventario** dei beni immobili del territorio, gestito dall'**Agenzia delle Entrate**. In Italia è **non probatorio**: non fa piena prova della **proprietà** (che spetta ai **registri immobiliari/conservatoria**), ma ha finalità **fiscali**, di **individuazione** e di supporto alla fiscalità immobiliare (IMU, imposte di trasferimento).

- **Catasto Terreni (CT)**: unità elementare la **particella** (mappale); si definiscono **qualità di coltura, classe, reddito dominicale e agrario**.
- **Catasto Fabbricati (CF)** (ex NCEU): unità elementare l'**unità immobiliare urbana (UIU)**; classificata per **categoria** — **A** abitazioni, **B** collettività (scuole, caserme), **C** commerciali/box, **D** speciali (opifici, alberghi), **E** particolari, **F** fittizie (aree urbane, fabbricati in corso). Ad ogni UIU si attribuisce **categoria, classe e consistenza** (vani per le A, mq per le C, mc per le B) da cui la **rendita catastale**.

L'**identificativo catastale** è: **Foglio – Particella (mappale) – Subalterno**. Le variazioni si presentano con procedure informatiche (**DOCFA** per i fabbricati, **PREGEO** per gli aggiornamenti cartografici).

## Estimo: i cinque aspetti economici

La stima associa al bene un **aspetto economico** coerente con lo **scopo** della valutazione:

1. **Valore di mercato** — più probabile prezzo di scambio.
2. **Valore di costo** — costo di produzione/ricostruzione (a nuovo, poi deprezzato).
3. **Valore di trasformazione** — valore del prodotto trasformato **meno** i costi di trasformazione (tipico delle aree edificabili e dei recuperi).
4. **Valore di capitalizzazione** — attualizzazione dei redditi futuri: **V = R / r**.
5. **Valore complementare** (o di surrogazione) — perdita di valore del complesso in assenza della parte.

## Principi metodologici

- **Principio dell'ordinarietà**: riferimento al comportamento **medio/ordinario** del mercato.
- **Comparazione**: confronto con beni simili (metodo **sintetico-comparativo**, €/mq) o **analitico** (per capitalizzazione dei redditi).
- **Giudizio di convenienza** e **momento della stima** (i valori cambiano nel tempo).

## Applicazioni tipiche

Stima di **fabbricati civili** (sintetico €/mq corretto da coefficienti di merito), **aree edificabili** (valore di trasformazione o mercato), **indennità di esproprio**, **danni** e **servitù**, **divisioni** e **successioni**.
""",
    },
    # ------------------------------------------------------------------ PROFESSIONE
    {
        "slug": "professione-deontologia",
        "category": "professione",
        "title": "Professione: Ordine, deontologia e compensi",
        "subtitle": "Abilitazione, obblighi, incarichi e equo compenso",
        "read_minutes": 6,
        "key_points": [
            "Iscrizione all'Albo (sez. A architetto; sez. B iunior) dopo l'Esame di Stato.",
            "Obblighi: formazione continua (CFP), assicurazione RC, deontologia.",
            "Tariffe minime abrogate (DL 1/2012); preventivo obbligatorio; equo compenso (L. 49/2023).",
            "Ruoli: progettista, direttore dei lavori, coordinatore sicurezza, collaudatore.",
        ],
        "content": """## Accesso e Albo

Superato l'**Esame di Stato**, ci si iscrive all'**Albo dell'Ordine degli Architetti Pianificatori Paesaggisti e Conservatori**, articolato in **sezione A** (laurea magistrale) e **sezione B** (laurea triennale – *architetto iunior*), con **settori**: architettura, pianificazione, paesaggio, conservazione. Gli Ordini provinciali fanno capo al **Consiglio Nazionale (CNAPPC)**.

## Competenze delle sezioni

- **Sezione A**: attività di progettazione, direzione lavori, collaudo, ecc. su tutte le opere di edilizia civile, restauro, urbanistica (con i limiti per il restauro di beni tutelati riservato agli architetti).
- **Sezione B (iunior)**: opere di **modesta complessità** e con metodologie standardizzate, oltre a rilievi, attività tecniche di supporto.

## Obblighi del professionista

- **Formazione Continua**: acquisizione di **crediti formativi professionali (CFP)** obbligatori (DPR 137/2012).
- **Assicurazione RC professionale** obbligatoria, con obbligo di informarne il cliente.
- **Codice Deontologico**: indipendenza, correttezza, lealtà verso colleghi e committenti, riservatezza, divieto di accaparramento e di concorrenza sleale; dovere di competenza e aggiornamento.

## Compensi e incarichi

Le **tariffe minime obbligatorie** sono state **abrogate** (DL 1/2012 e L. 27/2012). Il professionista deve fornire al cliente un **preventivo** (di regola **scritto**) con il grado di complessità e gli oneri. Per i rapporti con la **PA** il **DM 17 giugno 2016 (decreto parametri)** è riferimento per la stima dei corrispettivi a base di gara; la **Legge 49/2023 sull'equo compenso** tutela l'adeguatezza del compenso nei rapporti con committenti "forti".

## I ruoli tecnici

- **Progettista**: redige il progetto (fattibilità, esecutivo) e ne assume la responsabilità.
- **Direttore dei Lavori (DL)**: cura la **conformità** dell'esecuzione al progetto, contabilizza i lavori, coordina con la committenza.
- **Coordinatore per la Sicurezza** (D.Lgs. 81/2008): in progettazione (**CSP**) ed esecuzione (**CSE**).
- **Collaudatore**: verifica tecnica ed economica dell'opera (collaudo statico e tecnico-amministrativo).
""",
    },
    {
        "slug": "sicurezza-cantieri",
        "category": "professione",
        "title": "Sicurezza nei cantieri (D.Lgs. 81/2008)",
        "subtitle": "Titolo IV: PSC, POS, PiMUS, coordinatori e responsabilità",
        "read_minutes": 6,
        "key_points": [
            "Testo Unico sicurezza: D.Lgs. 81/2008; Titolo IV = cantieri temporanei o mobili.",
            "PSC redatto dal CSP; POS da ciascuna impresa esecutrice; PiMUS per i ponteggi.",
            "Coordinatori CSP/CSE obbligatori con presenza di più imprese (anche non contemporanea).",
            "Notifica preliminare all'organo di vigilanza nei casi previsti.",
        ],
        "content": """## Il Testo Unico

Il **D.Lgs. 9 aprile 2008, n. 81** è il Testo Unico su **salute e sicurezza sul lavoro**. Il **Titolo IV** disciplina i **cantieri temporanei o mobili**, integrando i principi generali (valutazione dei rischi, DVR, sorveglianza sanitaria, formazione).

## Le figure del cantiere

- **Committente** e **Responsabile dei Lavori (RL)**: titolari degli obblighi di designazione dei coordinatori e di verifica.
- **Coordinatore per la Sicurezza in fase di Progettazione (CSP)**: redige il **PSC** e il **fascicolo dell'opera**.
- **Coordinatore per la Sicurezza in fase di Esecuzione (CSE)**: verifica l'applicazione del PSC, coordina le imprese, adegua i piani, **sospende** le lavorazioni in caso di pericolo grave e imminente.
- **Imprese esecutrici** e **lavoratori autonomi**: redigono/applicano il **POS**.

La designazione dei coordinatori è **obbligatoria** quando è prevista la **presenza di più imprese esecutrici**, anche **non contemporanea**.

## I documenti

- **PSC – Piano di Sicurezza e Coordinamento**: individua i rischi del cantiere, le misure di prevenzione, l'organizzazione, la gestione delle **interferenze**, cronoprogramma e costi della sicurezza (non soggetti a ribasso).
- **POS – Piano Operativo di Sicurezza**: documento della **singola impresa** relativo alle proprie lavorazioni.
- **PiMUS – Piano di Montaggio, Uso e Smontaggio** dei **ponteggi**.
- **Fascicolo dell'opera**: informazioni utili alla sicurezza nelle **manutenzioni** future.
- **Notifica preliminare**: comunicazione all'ASL/Ispettorato nei casi previsti (durata/entità del cantiere).

## Responsabilità

Il sistema prevede sanzioni **penali e amministrative**. La corretta **attribuzione dei ruoli**, la **formazione**, la **vigilanza effettiva** e la gestione delle interferenze sono decisive nella ripartizione delle responsabilità tra committente, coordinatori, datori di lavoro e preposti.
""",
    },
    # ------------------------------------------------------------------ COSTRUTTIVI
    {
        "slug": "elementi-costruttivi",
        "category": "costruttivi",
        "title": "Elementi costruttivi dell'edificio",
        "subtitle": "Fondazioni, strutture verticali, solai, coperture, involucro",
        "read_minutes": 7,
        "key_points": [
            "Fondazioni dirette (plinti, travi rovesce, platea) e indirette (pali).",
            "Strutture verticali: puntiformi (pilastri) o continue (muratura/setti).",
            "Solai: latero-cementizi, soletta piena, predalles, lamiera collaborante, legno.",
            "Coperture a falda o piane; stratigrafia con isolante, impermeabilizzazione e barriera al vapore.",
        ],
        "content": """## Fondazioni

Trasferiscono i carichi al terreno entro i limiti di **portanza** e **cedimenti** ammissibili.

- **Dirette (superficiali)**: **plinti** (isolati, sotto i pilastri), **travi rovesce** (collegano più pilastri, utili in sisma e su terreni meno uniformi), **platea/fondazione a graticcio** (distribuisce il carico su tutta l'impronta, per terreni scarsi o forti carichi).
- **Indirette (profonde)**: **pali** (battuti, trivellati, micropali) che portano i carichi a **strati profondi** resistenti per **punta** e/o **attrito laterale**. Impiegate quando gli strati superficiali sono scadenti.

La scelta dipende dalla **relazione geologica e geotecnica** (indagini, prove penetrometriche, carotaggi).

## Strutture portanti verticali

- **Puntiformi**: **pilastri** (c.a., acciaio, legno) in sistemi a **telaio**; consentono libertà distributiva e grandi aperture.
- **Continue**: **muratura portante** o **setti/pareti in c.a.** (spesso con funzione **sismoresistente** di controvento).

## Solai

Elementi orizzontali portanti che assolvono anche a requisiti **acustici** (calpestio) e di **resistenza al fuoco**:
- **Latero-cementizio** (travetti + pignatte + soletta collaborante) — il più diffuso;
- **Soletta piena** in c.a. (per luci e carichi particolari, o forme libere);
- **Predalles** (lastre prefabbricate + getto integrativo);
- **Lamiera grecata collaborante** (acciaio-calcestruzzo);
- **Legno** (travi + tavolato, o solai in X-Lam).

## Chiusure verticali

**Tamponature** (nei telai) e **pareti**: devono garantire **isolamento termico e acustico**, tenuta all'acqua e all'aria, resistenza meccanica. Sistemi ad alte prestazioni: **cappotto** (isolamento continuo esterno, riduce i ponti termici) e **parete ventilata** (rivestimento + intercapedine ventilata).

## Coperture

- **A falda** (inclinate): rapido smaltimento dell'acqua; manto in tegole/coppi/lamiera su struttura lignea o in c.a.
- **Piane**: richiedono **pendenze minime** e una stratigrafia curata: **barriera al vapore, isolante termico, impermeabilizzazione (guaine), strato di protezione** (nel "tetto rovescio" l'isolante sta sopra l'impermeabilizzazione).

## Stratigrafia funzionale

In ogni chiusura si controlla, dall'interno all'esterno: **barriera al vapore – isolante – impermeabilizzazione/tenuta**, evitando la **condensa interstiziale** (verifica di Glaser) e garantendo **traspirabilità** e **durabilità**. Fondamentali anche **infissi** (trasmittanza, tenuta), **pavimentazioni/rivestimenti** e l'integrazione con gli **impianti** (elettrico, idrico-sanitario, gas, termico, condizionamento).
""",
    },
]

# =============================================================================
# QUESTIONS — base + ampliamento (focus URBANISTICA) + progettazione a risposta multipla
# =============================================================================
EXTRA_QUESTIONS = [
    # --- URBANISTICA (ampliamento importante) ---
    {"category": "urbanistica", "topic": "urbanistica-fondamenti", "question": "Dopo la riforma del Titolo V (2001), la materia urbanistica rientra in:",
     "options": ["Governo del territorio (competenza concorrente)", "Competenza esclusiva statale", "Competenza esclusiva comunale", "Competenza esclusiva UE"], "correct": 0,
     "explanation": "La riforma ha ricondotto l'urbanistica al 'governo del territorio', materia concorrente: lo Stato fissa i principi, le Regioni legiferano nel dettaglio."},
    {"category": "urbanistica", "topic": "urbanistica-fondamenti", "question": "La 'legge ponte' del 1967 (L. 765) ha reso:",
     "options": ["Obbligatorio il PRG e introdotto la licenza edilizia", "Gratuita l'edificazione", "Facoltativi gli standard", "Abolito l'esproprio"], "correct": 0,
     "explanation": "La legge ponte 765/1967 rese obbligatorio il PRG, introdusse la licenza edilizia e rinviò agli standard (poi DM 1444/68)."},
    {"category": "urbanistica", "topic": "urbanistica-fondamenti", "question": "I vincoli urbanistici preordinati all'esproprio hanno durata:",
     "options": ["5 anni, poi decadono", "10 anni, sempre rinnovabili senza indennizzo", "Illimitata", "1 anno"], "correct": 0,
     "explanation": "I vincoli espropriativi durano 5 anni; se non attuati decadono (zona bianca). La reiterazione che azzera il valore richiede indennizzo (Corte Cost. 179/1999)."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "La zona omogenea destinata a nuova espansione è la:",
     "options": ["Zona C", "Zona A", "Zona B", "Zona E"], "correct": 0,
     "explanation": "La zona C è destinata a nuovi complessi insediativi (espansione). La B è completamento, la A i centri storici, la E l'agricolo."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "Per il direzionale/commerciale lo standard minimo è:",
     "options": ["80 mq ogni 100 mq di superficie lorda", "18 mq/abitante", "10% della superficie", "40 mq ogni 100 mq"], "correct": 0,
     "explanation": "Il DM 1444/68 prevede per direzionale e commerciale 80 mq ogni 100 mq di SLP (di cui metà a parcheggi). I 18 mq/ab valgono per la residenza."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "In zona C, se l'altezza supera i 10 m, la distanza tra pareti finestrate dev'essere:",
     "options": ["Almeno pari all'altezza del fabbricato più alto", "Sempre 3 m", "Sempre 5 m", "Libera"], "correct": 0,
     "explanation": "In zona C, oltre i 10 m di altezza, il distacco tra pareti finestrate dev'essere almeno pari all'altezza dell'edificio più alto (DM 1444/68)."},
    {"category": "urbanistica", "topic": "piani-attuativi", "question": "Il Piano di Lottizzazione è uno strumento:",
     "options": ["Attuativo di iniziativa privata con convenzione", "Sovraordinato al PRG", "Di sola iniziativa pubblica", "Equivalente al PTCP"], "correct": 0,
     "explanation": "Il PdL è un piano attuativo di iniziativa privata, regolato da una convenzione (cessioni, opere di urbanizzazione, garanzie). Attua il PRG su un ambito."},
    {"category": "urbanistica", "topic": "piani-attuativi", "question": "Il PEEP (L. 167/1962) riguarda:",
     "options": ["L'edilizia economica e popolare", "Gli insediamenti produttivi", "Il recupero dei centri storici", "Le grandi infrastrutture"], "correct": 0,
     "explanation": "Il PEEP individua aree per l'edilizia economica e popolare; il PIP è l'analogo per gli insediamenti produttivi (L. 865/1971)."},
    {"category": "urbanistica", "topic": "opere-urbanizzazione-oneri", "question": "Quale opera è di urbanizzazione SECONDARIA?",
     "options": ["Scuola dell'obbligo", "Fognatura", "Rete idrica", "Pubblica illuminazione"], "correct": 0,
     "explanation": "Scuole, chiese, impianti sportivi e centri sociali sono urbanizzazione secondaria; strade, fogne, reti e illuminazione sono primaria."},
    {"category": "urbanistica", "topic": "opere-urbanizzazione-oneri", "question": "La Legge Tognoli (122/1989) fissa i parcheggi pertinenziali in:",
     "options": ["1 mq ogni 10 mc di costruzione", "1 mq ogni 100 mc", "18 mq per abitante", "1 posto per unità"], "correct": 0,
     "explanation": "La L. 122/1989 (Tognoli) prevede 1 mq di parcheggio ogni 10 mc di costruzione, realizzabili anche nel sottosuolo e in deroga agli strumenti urbanistici."},
    {"category": "urbanistica", "topic": "perequazione-compensazione", "question": "La perequazione urbanistica serve a:",
     "options": ["Distribuire equamente diritti edificatori e oneri", "Aumentare sempre le volumetrie", "Abolire gli standard", "Eliminare i piani attuativi"], "correct": 0,
     "explanation": "La perequazione attribuisce diritti edificatori uniformi e ripartisce equamente vantaggi e oneri tra i proprietari di un ambito, superando le disparità della zonizzazione."},
    {"category": "urbanistica", "topic": "perequazione-compensazione", "question": "La 'premialità' urbanistica consiste in:",
     "options": ["Incentivi volumetrici a fronte di prestazioni di interesse pubblico", "Una sanzione per l'abuso", "Un'imposta comunale", "Un vincolo paesaggistico"], "correct": 0,
     "explanation": "La premialità concede bonus volumetrici in cambio di qualità/interesse pubblico (efficienza energetica, edilizia sociale, riqualificazione)."},
    {"category": "urbanistica", "topic": "vincoli-esproprio", "question": "Il Testo Unico sull'espropriazione per pubblica utilità è il:",
     "options": ["DPR 327/2001", "DPR 380/2001", "D.Lgs. 42/2004", "L. 1150/1942"], "correct": 0,
     "explanation": "Il DPR 327/2001 è il T.U. espropri. Il DPR 380/2001 è l'edilizia, il D.Lgs. 42/2004 i beni culturali."},
    {"category": "urbanistica", "topic": "rigenerazione-consumo-suolo", "question": "L'obiettivo europeo di lungo periodo sul suolo è:",
     "options": ["Consumo di suolo netto pari a zero", "Raddoppio delle aree edificabili", "Abolizione dei centri storici", "Espansione illimitata"], "correct": 0,
     "explanation": "L'UE indica il traguardo del consumo di suolo netto pari a zero (tendenzialmente al 2050), privilegiando riuso e rigenerazione dell'esistente."},
    {"category": "urbanistica", "topic": "parametri-edilizi-urbanistici", "question": "L'indice di edificabilità FONDIARIA (IF) si applica alla:",
     "options": ["Superficie fondiaria", "Superficie territoriale", "Superficie coperta", "Superficie utile"], "correct": 0,
     "explanation": "L'IF si applica alla superficie fondiaria (netta delle urbanizzazioni); l'IT si applica alla superficie territoriale ed è più basso."},
    {"category": "urbanistica", "topic": "parametri-edilizi-urbanistici", "question": "Il rapporto di copertura (RC) è definito come:",
     "options": ["Superficie coperta / superficie fondiaria", "Volume / superficie", "Superficie utile / territoriale", "Altezza / larghezza"], "correct": 0,
     "explanation": "RC = superficie coperta / superficie fondiaria (spesso in %). Esempio: SF 800 mq con RC 40% → SC max 320 mq."},

    # --- EDILIZIA (ampliamento) ---
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "La 'doppia conformità' è richiesta per:",
     "options": ["La sanatoria ex art. 36 DPR 380/2001", "L'edilizia libera", "La manutenzione ordinaria", "L'agibilità"], "correct": 0,
     "explanation": "La sanatoria ordinaria (art. 36) richiede la doppia conformità: l'opera deve essere conforme alla disciplina sia al momento della realizzazione sia della domanda."},
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "La demolizione e ricostruzione rientra oggi, di regola, nella:",
     "options": ["Ristrutturazione edilizia", "Nuova costruzione sempre", "Manutenzione ordinaria", "Edilizia libera"], "correct": 0,
     "explanation": "Dopo le modifiche al DPR 380/2001, la demo-ricostruzione è ristrutturazione edilizia (con regole su sagoma/sedime fuori dai centri storici e salvo vincoli)."},

    # --- STRUTTURE (ampliamento) ---
    {"category": "strutture", "topic": "ntc-2018-stati-limite", "question": "Nella combinazione sismica le azioni variabili entrano con il coefficiente:",
     "options": ["ψ2 (valore quasi permanente)", "γ_G1", "ψ0 (valore raro)", "1,5 sempre"], "correct": 0,
     "explanation": "Nella combinazione sismica E + G1 + G2 + Σ ψ2i·Qki le variabili entrano col valore quasi permanente (ψ2)."},
    {"category": "strutture", "topic": "materiali-predimensionamento", "question": "La sigla C25/30 di un calcestruzzo indica:",
     "options": ["Resistenza caratteristica cilindrica/cubica in MPa", "Il diametro delle armature", "La classe di esposizione", "Il copriferro in mm"], "correct": 0,
     "explanation": "C25/30 indica la resistenza caratteristica a compressione: 25 MPa (provino cilindrico) / 30 MPa (cubico)."},

    # --- SISMICA (ampliamento) ---
    {"category": "sismica", "topic": "criteri-antisismici", "question": "Il 'piano soffice' (soft storey) è:",
     "options": ["Un piano molto più debole/deformabile degli altri, pericoloso in sisma", "Un solaio fonoassorbente", "Un piano interrato impermeabile", "Un tetto giardino"], "correct": 0,
     "explanation": "Il piano soffice è un livello con rigidezza/resistenza molto inferiore agli altri (es. pilotis) che concentra le deformazioni e può collassare: va evitato."},

    # --- ENERGETICO (ampliamento) ---
    {"category": "energetico", "topic": "efficienza-energetica-ape", "question": "La condensa interstiziale si verifica con:",
     "options": ["Il diagramma di Glaser", "La legge di massa", "Lo spettro di risposta", "Il metodo pushover"], "correct": 0,
     "explanation": "La verifica di Glaser controlla la formazione di condensa interstiziale negli strati; la barriera al vapore sul lato caldo la previene."},

    # --- APPALTI (ampliamento) ---
    {"category": "appalti", "topic": "codice-appalti", "question": "Quanti livelli di progettazione prevede il D.Lgs. 36/2023?",
     "options": ["Due: PFTE ed esecutivo", "Tre: preliminare, definitivo, esecutivo", "Uno soltanto", "Quattro"], "correct": 0,
     "explanation": "Il nuovo Codice riduce a due i livelli: Progetto di Fattibilità Tecnico-Economica (PFTE) ed Esecutivo (il definitivo è assorbito)."},
    {"category": "appalti", "topic": "codice-appalti", "question": "Il 'principio del risultato' nel D.Lgs. 36/2023:",
     "options": ["È criterio prioritario di interpretazione e applicazione del Codice", "Riguarda solo le forniture", "È stato abolito", "Vale solo sotto soglia"], "correct": 0,
     "explanation": "Il principio del risultato (miglior esito per la PA) è criterio interpretativo prioritario, insieme ai principi di fiducia e accesso al mercato."},

    # --- CATASTO (ampliamento) ---
    {"category": "catasto", "topic": "catasto-estimo", "question": "La categoria catastale 'D' identifica gli immobili:",
     "options": ["Speciali (opifici, alberghi, ecc.)", "Abitazioni", "Box e negozi", "Aree urbane"], "correct": 0,
     "explanation": "La categoria D raccoglie gli immobili a destinazione speciale (opifici, alberghi, industrie). A = abitazioni, C = box/negozi, F = fittizie."},
    {"category": "catasto", "topic": "catasto-estimo", "question": "La pratica per l'aggiornamento cartografico del Catasto Terreni è:",
     "options": ["PREGEO", "DOCFA", "APE", "SCIA"], "correct": 0,
     "explanation": "PREGEO aggiorna la cartografia catastale (terreni); DOCFA riguarda l'accatastamento/variazione dei fabbricati."},

    # --- BARRIERE (ampliamento) ---
    {"category": "barriere", "topic": "barriere-architettoniche", "question": "Il DPR 503/1996 si applica a:",
     "options": ["Edifici e spazi pubblici", "Sole abitazioni private", "Soli capannoni industriali", "Solo edifici vincolati"], "correct": 0,
     "explanation": "Il DPR 503/1996 disciplina l'accessibilità di edifici e spazi pubblici; il DM 236/1989 riguarda l'edilizia privata e residenziale pubblica."},
]

# quesiti di progettazione a risposta multipla (calcolo/scelta) — nella categoria urbanistica
DESIGN_MCQ = [
    {"category": "urbanistica", "topic": "parametri-edilizi-urbanistici", "question": "Lotto con SF = 1.000 mq e IF = 1,5 mc/mq: quale volume è edificabile?",
     "options": ["1.500 mc", "150 mc", "666 mc", "15.000 mc"], "correct": 0,
     "explanation": "Volume = SF × IF = 1.000 × 1,5 = 1.500 mc. È il calcolo base della capacità edificatoria fondiaria."},
    {"category": "urbanistica", "topic": "parametri-edilizi-urbanistici", "question": "Con SF = 800 mq e rapporto di copertura RC = 40%, la superficie coperta massima è:",
     "options": ["320 mq", "200 mq", "400 mq", "480 mq"], "correct": 0,
     "explanation": "SC = RC × SF = 0,40 × 800 = 320 mq."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "Nuovo insediamento residenziale per 300 abitanti: dotazione minima di standard (DM 1444)?",
     "options": ["5.400 mq", "1.800 mq", "540 mq", "9.000 mq"], "correct": 0,
     "explanation": "300 abitanti × 18 mq/ab = 5.400 mq di spazi pubblici, ripartiti in istruzione, interesse comune, verde/sport e parcheggi."},
    {"category": "urbanistica", "topic": "opere-urbanizzazione-oneri", "question": "Edificio di 1.500 mc: quanti mq di parcheggi pertinenziali (Tognoli) vanno previsti?",
     "options": ["150 mq", "15 mq", "1.500 mq", "75 mq"], "correct": 0,
     "explanation": "Legge Tognoli: 1 mq ogni 10 mc → 1.500 / 10 = 150 mq di parcheggi pertinenziali."},
    {"category": "urbanistica", "topic": "parametri-edilizi-urbanistici", "question": "Volume edificabile 1.600 mc, parametro 80 mc/abitante: abitanti insediabili?",
     "options": ["20", "80", "200", "128"], "correct": 0,
     "explanation": "Abitanti = Volume / (mc per abitante) = 1.600 / 80 = 20 abitanti insediabili."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "Due edifici con pareti finestrate antistanti, altezza 9 m in zona B: distanza minima?",
     "options": ["10 m", "9 m", "5 m", "3 m"], "correct": 0,
     "explanation": "Il minimo inderogabile tra pareti finestrate è 10 m (DM 1444/68), indipendentemente dall'altezza quando questa è ≤ 10 m."},
]

ALL_QUESTIONS = list(seed_data.QUESTIONS) + EXTRA_QUESTIONS + DESIGN_MCQ

# =============================================================================
# FLASHCARDS — base + ampliamento urbanistica/progettazione
# =============================================================================
EXTRA_FLASHCARDS = [
    {"category": "urbanistica", "front": "Legge ponte (1967)", "back": "L. 765/1967: PRG obbligatorio + licenza edilizia"},
    {"category": "urbanistica", "front": "Legge Bucalossi", "back": "L. 10/1977: edificazione onerosa (contributo di costruzione)"},
    {"category": "urbanistica", "front": "Durata dei vincoli espropriativi", "back": "5 anni, poi decadono (zona bianca)"},
    {"category": "urbanistica", "front": "T.U. espropri", "back": "DPR 327/2001"},
    {"category": "urbanistica", "front": "Piano di Lottizzazione", "back": "Attuativo di iniziativa privata con convenzione"},
    {"category": "urbanistica", "front": "PEEP / PIP", "back": "Edilizia economica e popolare (167/62) / insediamenti produttivi (865/71)"},
    {"category": "urbanistica", "front": "Urbanizzazione primaria vs secondaria", "back": "Primaria: strade, reti, parcheggi. Secondaria: scuole, chiese, sport"},
    {"category": "urbanistica", "front": "Legge Tognoli", "back": "L. 122/1989: 1 mq parcheggio ogni 10 mc"},
    {"category": "urbanistica", "front": "Perequazione", "back": "Distribuzione equa di diritti edificatori e oneri"},
    {"category": "urbanistica", "front": "Indice territoriale vs fondiario", "back": "IT su sup. territoriale; IF su sup. fondiaria (più alto)"},
    {"category": "urbanistica", "front": "Rapporto di copertura", "back": "RC = superficie coperta / superficie fondiaria"},
    {"category": "urbanistica", "front": "Standard direzionale/commerciale", "back": "80 mq ogni 100 mq di SLP"},
    {"category": "edilizia", "front": "Doppia conformità", "back": "Requisito della sanatoria ex art. 36 DPR 380/2001"},
    {"category": "catasto", "front": "DOCFA / PREGEO", "back": "DOCFA: fabbricati; PREGEO: cartografia terreni"},
]

ALL_FLASHCARDS = list(seed_data.FLASHCARDS) + EXTRA_FLASHCARDS

TRACCE = seed_data.TRACCE

# =============================================================================
# QUESITI DI PROGETTAZIONE (aperti, con svolgimento guidato)
# =============================================================================
DESIGN_QUESTIONS = [
    {
        "category": "urbanistica",
        "titolo": "Dimensionamento degli standard urbanistici",
        "prompt": "In un nuovo Piano attuativo residenziale si prevede un insediamento per 250 abitanti. Determina la dotazione minima di aree per standard e ripartiscila nelle quattro categorie del DM 1444/68.",
        "guida": "Dotazione totale = 250 ab × 18 mq/ab = 4.500 mq.\nRipartizione (DM 1444/68):\n• Istruzione 4,5 mq/ab → 1.125 mq\n• Attrezzature di interesse comune 2,0 mq/ab → 500 mq\n• Verde attrezzato, gioco e sport 9,0 mq/ab → 2.250 mq\n• Parcheggi pubblici 2,5 mq/ab → 625 mq\nSuggerimento: colloca il verde in continuità con spazi esistenti e i parcheggi su viabilità primaria; verifica gli abitanti insediabili con il parametro locale (80–100 mc/ab).",
    },
    {
        "category": "urbanistica",
        "titolo": "Capacità edificatoria di un lotto",
        "prompt": "Un lotto ha superficie fondiaria di 1.200 mq e indice fondiario IF = 1,2 mc/mq. Calcola il volume edificabile, gli abitanti insediabili (100 mc/ab) e la superficie coperta massima con RC = 35%.",
        "guida": "Volume = 1.200 × 1,2 = 1.440 mc.\nAbitanti = 1.440 / 100 = 14,4 → ~14 abitanti.\nSuperficie coperta max = 0,35 × 1.200 = 420 mq.\nVerifica poi altezze e distanze (≥10 m tra pareti finestrate) e la dotazione di parcheggi pertinenziali Tognoli: 1.440/10 = 144 mq.",
    },
    {
        "category": "urbanistica",
        "titolo": "Scelta del titolo abilitativo",
        "prompt": "Un committente vuole: (a) frazionare un appartamento in due unità con opere strutturali; (b) tinteggiare la facciata interna; (c) demolire e ricostruire un edificio con aumento di volumetria. Indica il titolo corretto per ciascun intervento.",
        "guida": "(a) Frazionamento con opere strutturali → manutenzione straordinaria strutturale: SCIA.\n(b) Tinteggiatura interna → edilizia libera (nessun titolo), salvo vincoli.\n(c) Demolizione e ricostruzione con aumento di volume → in genere Permesso di Costruire (ristrutturazione edilizia 'pesante'/nuova costruzione se muta sagoma e volume in zona vincolata).\nMotiva sempre con l'art. 3 e gli artt. 6, 10, 22 del DPR 380/2001.",
    },
    {
        "category": "urbanistica",
        "titolo": "Verifica delle distanze",
        "prompt": "In zona C due edifici hanno pareti finestrate antistanti; il più alto è 14 m. Qual è la distanza minima da rispettare e perché?",
        "guida": "Il minimo inderogabile è 10 m tra pareti finestrate (DM 1444/68). Tuttavia in zona C, quando l'altezza supera 10 m, la distanza tra pareti finestrate dev'essere almeno pari all'altezza del fabbricato più alto: quindi ≥ 14 m. Verifica inoltre distanze dai confini e dalle strade.",
    },
    {
        "category": "urbanistica",
        "titolo": "Recupero di un edificio esistente",
        "prompt": "Ti viene affidato il recupero di un piccolo edificio residenziale degli anni '60 in zona sismica. Imposta i temi progettuali principali che tratteresti nella relazione.",
        "guida": "Temi chiave: 1) classificazione dell'intervento (art. 3 DPR 380/2001) e verifica dello stato legittimo; 2) miglioramento o adeguamento sismico (NTC 2018) con valutazione della sicurezza; 3) efficientamento energetico dell'involucro (cappotto, serramenti, U-limite per zona climatica) e verifica della condensa; 4) superamento delle barriere architettoniche (DM 236/89: accessibilità/visitabilità, rampe 8%, porte ≥80 cm); 5) requisiti acustici (DPCM 5/12/1997); 6) titolo abilitativo e oneri; 7) eventuale premialità di rigenerazione urbana.",
    },
    {
        "category": "urbanistica",
        "titolo": "Schema distributivo di una scuola dell'infanzia",
        "prompt": "Imposta lo schema distributivo e i requisiti principali di una piccola scuola dell'infanzia a un piano su un lotto pianeggiante.",
        "guida": "Distribuzione: ingresso/atrio filtro, sezioni (aule) con esposizione favorevole (sud/est) e accesso diretto al giardino, spazi comuni (refettorio, attività), servizi igienici dedicati ai bambini e per il personale/accessibili, zona cucina/sporzionamento, spazi per il personale. Requisiti: accessibilità totale (DM 236/89), sicurezza antincendio (attività scolastica soggetta: esodo, compartimentazione, REI), illuminazione e ventilazione naturali adeguate, contenimento energetico, arredi e altezze a misura di bambino, uscite di sicurezza sul giardino. Rispetta standard urbanistici e distanze.",
    },
]
