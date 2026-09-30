"""
Contenuti di studio per l'Esame di Stato da Architetto.
Basati sul "riassunto-ceccarelli" (Prontuario Tecnico, Università Popolare di Roma)
e sulle tracce estratte IUAV 2024.

Nota didattica: i testi sono sintesi di studio. Verifica sempre la normativa
vigente (i riferimenti possono evolvere) sulle fonti ufficiali.
"""

# -----------------------------------------------------------------------------
# CATEGORIE (macro-argomenti)
# -----------------------------------------------------------------------------
CATEGORIES = [
    {"slug": "urbanistica", "name": "Urbanistica", "icon": "map", "blurb": "Pianificazione del territorio, zone omogenee, standard e piani urbanistici."},
    {"slug": "edilizia", "name": "Edilizia e titoli", "icon": "file-text", "blurb": "Interventi edilizi, permesso di costruire, SCIA, CILA e sanzioni."},
    {"slug": "strutture", "name": "Strutture e NTC 2018", "icon": "layers", "blurb": "Stati limite, azioni, materiali e predimensionamento strutturale."},
    {"slug": "sismica", "name": "Zona sismica", "icon": "activity", "blurb": "Classificazione sismica, criteri antisismici e interventi sull'esistente."},
    {"slug": "incendi", "name": "Prevenzione incendi", "icon": "alert-triangle", "blurb": "Resistenza al fuoco, compartimentazione ed esodo (Codice PI)."},
    {"slug": "energetico", "name": "Contenimento energetico", "icon": "thermometer", "blurb": "APE, involucro, trasmittanze e requisiti dell'edificio."},
    {"slug": "acustica", "name": "Acustica", "icon": "volume-2", "blurb": "Requisiti acustici passivi e zonizzazione acustica."},
    {"slug": "barriere", "name": "Barriere architettoniche", "icon": "users", "blurb": "Accessibilità, visitabilità e adattabilità (DM 236/89)."},
    {"slug": "appalti", "name": "Appalti pubblici", "icon": "briefcase", "blurb": "Codice dei contratti, procedure e figure dei lavori pubblici."},
    {"slug": "catasto", "name": "Catasto ed estimo", "icon": "home", "blurb": "Catasto terreni e fabbricati, teoria estimativa e valutazione."},
    {"slug": "professione", "name": "Pratica professionale", "icon": "award", "blurb": "Ordine, deontologia, direzione lavori, collaudo e onorari."},
    {"slug": "costruttivi", "name": "Elementi costruttivi", "icon": "grid", "blurb": "Fondazioni, strutture verticali, solai, coperture e involucro."},
]

# -----------------------------------------------------------------------------
# TOPICS (teoria) — ciascuno con contenuto in markdown e punti chiave
# -----------------------------------------------------------------------------
TOPICS = [
    {
        "slug": "urbanistica-fondamenti",
        "category": "urbanistica",
        "title": "Fondamenti di urbanistica e livelli di pianificazione",
        "subtitle": "Dalla legge 1150/1942 al governo del territorio Stato–Regioni",
        "read_minutes": 6,
        "key_points": [
            "La legge urbanistica fondamentale è la L. 1150/1942, più volte modificata.",
            "La materia 'governo del territorio' è di competenza concorrente Stato–Regioni (art. 117 Cost.).",
            "La pianificazione è gerarchica: dal livello territoriale (PTR, PTCP) a quello comunale (PRG/PGT) e attuativo (piani esecutivi).",
        ],
        "content": """## Il quadro normativo

L'urbanistica moderna in Italia nasce con la **Legge 17 agosto 1942, n. 1150** (Legge Urbanistica Fondamentale), che introduce gli strumenti di pianificazione a scala comunale e sovracomunale. La riforma del **Titolo V della Costituzione (L. cost. 3/2001)** ha ricondotto la materia al **"governo del territorio"**, competenza **concorrente**: lo Stato fissa i principi fondamentali, le Regioni legiferano nel dettaglio.

## I livelli della pianificazione

La pianificazione è **gerarchica e a cascata**: ogni livello deve essere coerente con quello superiore.

- **Livello territoriale/regionale**: Piano Territoriale Regionale (PTR), Piano Territoriale di Coordinamento Provinciale (PTCP). Definiscono indirizzi, tutele e grandi infrastrutture.
- **Livello comunale**: il **Piano Regolatore Generale (PRG)** – nelle leggi regionali più recenti articolato in Piano Strutturale + Piano Operativo (es. PGT in Lombardia). Disciplina l'intero territorio comunale.
- **Livello attuativo/esecutivo**: Piani Particolareggiati, Piani di Lottizzazione, PEEP, PIP, Piani di Recupero. Attuano le previsioni del PRG su ambiti specifici.

## Contenuti del PRG

Il PRG **azzona** il territorio, fissa indici e parametri (indice di edificabilità, altezze, distanze), individua le opere di urbanizzazione e i vincoli. È accompagnato dalle **Norme Tecniche di Attuazione (NTA)**.

## Il DM 1444/1968

Il **Decreto Interministeriale 2 aprile 1968, n. 1444** è centrale: definisce le **zone territoriali omogenee (A–F)** e gli **standard urbanistici minimi** (dotazioni di spazi pubblici), oltre a limiti inderogabili di densità, altezza e distanza tra fabbricati (di norma **10 m** tra pareti finestrate).
""",
    },
    {
        "slug": "zone-omogenee-standard",
        "category": "urbanistica",
        "title": "Zone omogenee (DM 1444/68) e standard urbanistici",
        "subtitle": "Le zone A–F e le dotazioni minime di spazi pubblici",
        "read_minutes": 5,
        "key_points": [
            "Zone: A centro storico, B completamento, C espansione, D produttive, E agricole, F attrezzature.",
            "Standard residenziale: 18 mq/abitante di spazi pubblici (istruzione, verde, parcheggi, interesse comune).",
            "Distanza minima tra pareti finestrate di edifici antistanti: 10 m.",
        ],
        "content": """## Le zone territoriali omogenee

Il **DM 1444/1968** classifica il territorio in zone omogenee:

- **Zona A** – agglomerati di interesse **storico, artistico e ambientale** (centri storici).
- **Zona B** – parti del territorio **totalmente o parzialmente edificate** (completamento).
- **Zona C** – parti destinate a **nuovi complessi insediativi** (espansione).
- **Zona D** – parti destinate a **insediamenti produttivi** (industriali/artigianali).
- **Zona E** – parti destinate a usi **agricoli**.
- **Zona F** – parti destinate ad **attrezzature e impianti di interesse generale**.

## Gli standard urbanistici

Lo **standard** è la dotazione minima di spazi pubblici per abitante insediato. Per la residenza il minimo è **18 mq/abitante**, così ripartiti:

- **4,5 mq** aree per l'istruzione (asili, scuole dell'obbligo);
- **2,0 mq** attrezzature di interesse comune;
- **9,0 mq** aree per spazi pubblici attrezzati a parco, gioco e sport;
- **2,5 mq** aree per parcheggi.

Per insediamenti produttivi e direzionali/commerciali sono previsti standard specifici (es. per il direzionale 80 mq ogni 100 mq di superficie lorda).

## Limiti inderogabili

Il decreto fissa anche **densità edilizie, altezze massime e distanze**. La distanza minima tra pareti finestrate e pareti di edifici antistanti è **10 m**; nelle zone C possono valere distacchi maggiori in funzione dell'altezza.
""",
    },
    {
        "slug": "titoli-abilitativi",
        "category": "edilizia",
        "title": "Titoli abilitativi: Permesso di Costruire, SCIA, CILA",
        "subtitle": "Il DPR 380/2001 (Testo Unico dell'Edilizia)",
        "read_minutes": 7,
        "key_points": [
            "Il Testo Unico dell'Edilizia è il DPR 380/2001.",
            "Permesso di Costruire per nuova costruzione e ristrutturazione 'pesante'.",
            "SCIA e CILA per interventi minori; edilizia libera senza titolo.",
        ],
        "content": """## Il Testo Unico dell'Edilizia

Il **DPR 6 giugno 2001, n. 380** raccoglie la disciplina dell'attività edilizia. Gli interventi (art. 3) sono classificati in:

- **Manutenzione ordinaria (MO)**: riparazioni, rinnovo finiture.
- **Manutenzione straordinaria (MS)**: opere per rinnovare/sostituire parti anche strutturali, senza aumento di volume né mutamento di destinazione d'uso.
- **Restauro e risanamento conservativo**: conservano l'organismo edilizio.
- **Ristrutturazione edilizia**: possono portare a un organismo in tutto o in parte diverso.
- **Nuova costruzione** e **ristrutturazione urbanistica**.

## I titoli abilitativi

- **Permesso di Costruire (PdC)** – art. 10: interventi di **nuova costruzione**, ristrutturazione urbanistica e ristrutturazione edilizia "pesante" (con aumento di unità, volumi o modifiche della sagoma in zona vincolata). È oneroso (contributo di costruzione).
- **SCIA** – Segnalazione Certificata di Inizio Attività: per MS strutturale, restauro/risanamento, ristrutturazione "leggera". Si inizia subito; c'è la **SCIA alternativa al PdC** (super-SCIA).
- **CILA** – Comunicazione Inizio Lavori Asseverata: interventi di MS **non** strutturale e opere interne non riconducibili all'edilizia libera.
- **Edilizia libera** – art. 6: MO, opere temporanee, ecc., senza alcun titolo.

## Il contributo di costruzione

Il PdC è oneroso: il **contributo** è dato da **oneri di urbanizzazione** (primaria e secondaria) + **costo di costruzione**. Alcuni interventi (es. edilizia con finalità pubbliche o in certi casi ristrutturazioni) possono essere gratuiti.

## Sanzioni

Il TU disciplina l'**abuso edilizio**: dalle sanzioni pecuniarie alla demolizione. La **fiscalizzazione dell'abuso** è ammessa solo quando la demolizione non è possibile senza pregiudizio per la parte legittima.
""",
    },
    {
        "slug": "ntc-2018-stati-limite",
        "category": "strutture",
        "title": "NTC 2018: stati limite e azioni sulle costruzioni",
        "subtitle": "Metodo semiprobabilistico agli stati limite (SLU/SLE)",
        "read_minutes": 7,
        "key_points": [
            "Le NTC 2018 (DM 17/01/2018) usano il metodo semiprobabilistico agli stati limite.",
            "SLU: sicurezza (collasso); SLE: esercizio (deformazioni, fessurazione, comfort).",
            "Le azioni si combinano con coefficienti parziali γ e coefficienti di combinazione ψ.",
        ],
        "content": """## Il metodo agli stati limite

Le **Norme Tecniche per le Costruzioni (DM 17 gennaio 2018)** adottano il **metodo semiprobabilistico agli stati limite** con **coefficienti parziali di sicurezza**. La verifica generale è:

> **E_d ≤ R_d**  (effetto delle azioni di progetto ≤ resistenza di progetto)

## Stati limite

- **SLU – Stati Limite Ultimi**: riguardano la **sicurezza** e l'incolumità (perdita di equilibrio, rottura, instabilità, meccanismi). Si applicano coefficienti parziali sui materiali (γ_M) e sulle azioni (γ_F).
- **SLE – Stati Limite di Esercizio**: riguardano la **funzionalità** in condizioni d'uso (deformazioni e spostamenti, fessurazione, vibrazioni, comfort).

## Le azioni

Le azioni si classificano in **permanenti (G)**, **variabili (Q)**, **eccezionali (A)** e **sismiche (E)**. Le azioni permanenti si distinguono in strutturali (G1) e non strutturali (G2).

## Le combinazioni di carico

- **Combinazione fondamentale (SLU)**:  γ_G1·G1 + γ_G2·G2 + γ_Q1·Q_k1 + Σ γ_Qi·ψ_0i·Q_ki
- **Combinazione caratteristica (rara)** e **frequente/quasi permanente** per gli SLE.
- **Combinazione sismica**: E + G1 + G2 + Σ ψ_2i·Q_ki.

I **coefficienti di combinazione ψ0, ψ1, ψ2** riducono le azioni variabili in funzione della probabilità di contemporaneità.

## Vita nominale, classi d'uso, periodo di riferimento

La sicurezza è tarata sulla **vita nominale (V_N)**, sulla **classe d'uso (I–IV)** con coefficiente C_U, e sul **periodo di riferimento V_R = V_N · C_U**, che governa le azioni sismiche.
""",
    },
    {
        "slug": "materiali-predimensionamento",
        "category": "strutture",
        "title": "Materiali strutturali e predimensionamento",
        "subtitle": "Calcestruzzo armato, acciaio, legno, muratura",
        "read_minutes": 6,
        "key_points": [
            "Il c.a. abbina calcestruzzo (compressione) e acciaio (trazione).",
            "Regole di predimensionamento: travi h ≈ L/10, solai h ≈ L/25.",
            "La muratura è un materiale resistente prevalentemente a compressione.",
        ],
        "content": """## Calcestruzzo armato

Il **c.a.** sfrutta il calcestruzzo (ottimo a compressione, scarso a trazione) e le armature in acciaio (ottime a trazione). La classe di resistenza si indica come **C25/30** (resistenza cilindrica/cubica in MPa). L'acciaio da c.a. tipico è **B450C**. Il **copriferro** protegge le armature da corrosione e fuoco.

## Acciaio

L'acciaio strutturale (es. **S235, S275, S355**) è duttile e resiste bene a trazione e compressione; richiede verifiche di **instabilità** (aste compresse) e attenzione ai **collegamenti** (bullonati/saldati) e alla protezione al fuoco.

## Legno

Materiale leggero, rinnovabile, buon rapporto resistenza/peso. Si usa massiccio o **lamellare**; richiede controllo di umidità, durabilità e comportamento al fuoco (la carbonizzazione superficiale protegge il nucleo).

## Muratura

Resiste soprattutto a **compressione**; poco a trazione e taglio. Fondamentale nelle costruzioni esistenti e nei centri storici. In zona sismica si distingue muratura **ordinaria** e **armata**.

## Regole pratiche di predimensionamento

- **Trave** in c.a.: altezza h ≈ **L/10 ÷ L/12** della luce.
- **Solaio** latero-cementizio: h ≈ **L/25** (indicativamente 20–30 cm per luci correnti).
- **Pilastro**: dimensionato allo sforzo normale con snellezza controllata.
- **Sbalzo/mensola**: h maggiore, ≈ **L/8**.

Il predimensionamento fornisce dimensioni di primo tentativo da verificare poi agli SLU/SLE.
""",
    },
    {
        "slug": "criteri-antisismici",
        "category": "sismica",
        "title": "Progettazione in zona sismica",
        "subtitle": "Classificazione sismica, gerarchia delle resistenze e regolarità",
        "read_minutes": 6,
        "key_points": [
            "L'OPCM 3274/2003 ha riclassificato tutto il territorio in 4 zone sismiche.",
            "La 'gerarchia delle resistenze' (capacity design) evita rotture fragili.",
            "Regolarità in pianta e in elevazione migliorano la risposta sismica.",
        ],
        "content": """## Classificazione sismica

Con l'**OPCM 3274/2003** l'intero territorio nazionale è stato classificato in **quattro zone sismiche** (1 = maggiore pericolosità, 4 = minore). Le NTC 2018 definiscono l'azione sismica in termini di **accelerazione al suolo (a_g)** e spettri di risposta, in funzione della pericolosità del sito, della categoria di sottosuolo e della topografia.

## Comportamento e duttilità

Un edificio ben progettato dissipa energia sismica deformandosi in modo **duttile**. Si definisce un **fattore di comportamento q** che riduce le forze elastiche in funzione della capacità dissipativa (classi di duttilità **CD"A" alta** e **CD"B" media**).

## Gerarchia delle resistenze (capacity design)

Principio cardine: garantire che i meccanismi **duttili** (es. flessione delle travi) si attivino **prima** di quelli **fragili** (taglio, rottura dei nodi, dei pilastri). Si progetta quindi "trave debole – pilastro forte" per evitare il **piano soffice** e il collasso improvviso.

## Regolarità strutturale

- **Regolarità in pianta**: forma compatta, simmetria di masse e rigidezze, baricentro delle masse vicino al centro delle rigidezze (riduce effetti torsionali).
- **Regolarità in elevazione**: continuità di masse, rigidezze e resistenze lungo l'altezza; evitare bruschi restringimenti.

## Interventi sull'esistente

Le NTC distinguono **adeguamento** (riportare l'edificio ai livelli di sicurezza richiesti dalla norma), **miglioramento** (aumentare la sicurezza senza raggiungere il pieno adeguamento) e **riparazioni/interventi locali**. La valutazione della sicurezza è obbligatoria in casi definiti (es. sopraelevazioni, cambi d'uso gravosi).
""",
    },
    {
        "slug": "prevenzione-incendi",
        "category": "incendi",
        "title": "Prevenzione incendi: principi e Codice PI",
        "subtitle": "Resistenza al fuoco (REI), compartimentazione ed esodo",
        "read_minutes": 6,
        "key_points": [
            "Il Codice di Prevenzione Incendi è il DM 3 agosto 2015 (aggiornato).",
            "REI: R=stabilità, E=tenuta, I=isolamento termico; i minuti indicano la durata.",
            "Strategia antincendio: reazione/resistenza al fuoco, compartimentazione, esodo, impianti.",
        ],
        "content": """## L'approccio prestazionale

Il **DM 3 agosto 2015 – Codice di Prevenzione Incendi** ha introdotto un approccio **prestazionale** (in alternativa alle regole tecniche verticali). L'obiettivo è la **sicurezza delle persone** e la limitazione dei danni.

## Le misure della strategia antincendio

Il Codice organizza la progettazione in **misure (S.1 … S.10)**, tra cui:

- **Reazione al fuoco** dei materiali (classi di combustibilità/euroclassi).
- **Resistenza al fuoco** delle strutture, espressa con la sigla **REI**:
  - **R** = capacità portante (stabilità),
  - **E** = tenuta a fiamme e fumi,
  - **I** = isolamento termico.
  Il numero (es. **REI 60, REI 120**) indica i **minuti** per cui la prestazione è garantita.
- **Compartimentazione**: suddivisione in **compartimenti** per limitare la propagazione.
- **Esodo**: vie di fuga, larghezze, lunghezze massime, luoghi sicuri, uscite.
- **Gestione della sicurezza**, **controllo dell'incendio** (estintori, idranti, sprinkler), **rivelazione e allarme**, **controllo di fumi e calore (SEFC)**, **operatività antincendio**.

## Il carico d'incendio

Il **carico d'incendio specifico di progetto (q_f,d)** [MJ/m²] misura l'energia termica dei materiali combustibili e determina la **classe del compartimento** e quindi la resistenza al fuoco richiesta.

## Procedure

Le attività soggette sono elencate nel **DPR 151/2011** (categorie A, B, C in base al rischio). Sono previsti **SCIA antincendio**, valutazione del progetto e controlli dei Vigili del Fuoco.
""",
    },
    {
        "slug": "efficienza-energetica-ape",
        "category": "energetico",
        "title": "Contenimento energetico e APE",
        "subtitle": "Involucro, trasmittanza e Attestato di Prestazione Energetica",
        "read_minutes": 6,
        "key_points": [
            "La normativa base è il D.Lgs. 192/2005 e i decreti 'requisiti minimi' del 2015.",
            "La trasmittanza U (W/m²K) misura il flusso di calore: più bassa, meglio è.",
            "L'APE classifica l'edificio da A4 (migliore) a G (peggiore).",
        ],
        "content": """## Quadro normativo

Il **D.Lgs. 192/2005** (attuazione della direttiva EPBD) e i **decreti requisiti minimi (DM 26/6/2015)** disciplinano l'efficienza energetica degli edifici, introducendo il concetto di **edificio a energia quasi zero (NZEB)**.

## L'involucro e la trasmittanza

Le dispersioni dipendono dall'**involucro** (pareti, coperture, solai, serramenti). La **trasmittanza termica U** [W/m²K] quantifica il calore che attraversa un componente per unità di superficie e differenza di temperatura: **valori bassi = migliore isolamento**. I decreti fissano U-limite per zona climatica (dalla **A** più calda alla **F** più fredda).

## Ponti termici e inerzia

Vanno limitati i **ponti termici** (discontinuità dell'isolamento) e valorizzata l'**inerzia termica** (sfasamento e attenuazione) per il comfort estivo. Importante anche il controllo della **condensa interstiziale** (verifica di Glaser).

## L'APE

L'**Attestato di Prestazione Energetica** esprime la prestazione in **classi da A4 (migliore) a G (peggiore)**, basate sull'indice di prestazione energetica globale non rinnovabile (EP_gl,nren). È obbligatorio in caso di **vendita, locazione e nuova costruzione/ristrutturazione importante** e va redatto da un **tecnico abilitato e indipendente**.

## Fonti rinnovabili

Il **D.Lgs. 199/2021** impone quote minime di **energia da fonti rinnovabili** (solare termico, fotovoltaico, pompe di calore) per i nuovi edifici e le ristrutturazioni rilevanti.
""",
    },
    {
        "slug": "acustica-edilizia",
        "category": "acustica",
        "title": "Acustica in edilizia",
        "subtitle": "Requisiti acustici passivi (DPCM 5/12/1997) e zonizzazione",
        "read_minutes": 5,
        "key_points": [
            "La legge quadro sull'inquinamento acustico è la L. 447/1995.",
            "I requisiti acustici passivi degli edifici sono nel DPCM 5/12/1997.",
            "Si valutano isolamento di facciata, tra ambienti, calpestio e rumore degli impianti.",
        ],
        "content": """## Quadro normativo

La **Legge 447/1995** è la legge quadro sull'**inquinamento acustico**. Il **DPCM 5 dicembre 1997** fissa i **requisiti acustici passivi** degli edifici, in funzione della **categoria** (residenze, scuole, ospedali, uffici, ecc.).

## I parametri principali

- **R'w** – potere fonoisolante apparente tra ambienti (partizioni interne).
- **D2m,nT,w** – isolamento acustico standardizzato di **facciata**.
- **L'n,w** – livello di rumore da **calpestio** dei solai (più basso è, meglio è).
- **LASmax / LAeq** – livelli massimi/equivalenti per il rumore degli **impianti** (a funzionamento discontinuo/continuo).

## Zonizzazione acustica

I Comuni classificano il territorio in **classi acustiche (I–VI)**, dalle aree particolarmente protette (I) alle aree esclusivamente industriali (VI), fissando i **limiti di immissione ed emissione** diurni e notturni.

## Progettazione

Il controllo del rumore si ottiene con **massa** (legge di massa), **sistemi massa-molla-massa** (doppie pareti), **materiali fonoassorbenti**, **desolidarizzazione** dei massetti (pavimenti galleggianti) contro il calpestio e attenzione ai **ponti acustici**.
""",
    },
    {
        "slug": "barriere-architettoniche",
        "category": "barriere",
        "title": "Barriere architettoniche e accessibilità",
        "subtitle": "DM 236/1989: accessibilità, visitabilità, adattabilità",
        "read_minutes": 5,
        "key_points": [
            "Il DM 236/1989 definisce i tre livelli di qualità dello spazio costruito.",
            "Accessibilità > visitabilità > adattabilità (livelli decrescenti).",
            "Rampe: pendenza max 8%; spazio di rotazione sedia a ruote Ø 150 cm.",
        ],
        "content": """## I tre livelli

Il **DM 14 giugno 1989, n. 236** (per l'edilizia privata e residenziale pubblica) definisce tre livelli:

- **Accessibilità**: possibilità di raggiungere e fruire **ogni** spazio e attrezzatura in sicurezza e autonomia (il livello più alto).
- **Visitabilità**: possibilità di accedere agli spazi di **relazione** e a un servizio igienico (livello intermedio).
- **Adattabilità**: possibilità di modificare nel tempo lo spazio per renderlo accessibile con **costi limitati** (livello minimo).

Per l'edilizia pubblica si applica anche il **DPR 503/1996**.

## Parametri dimensionali ricorrenti

- **Rampe**: pendenza massima **8%** (ammesse pendenze superiori solo per brevi tratti secondo abaco); larghezza min. 90 cm; ripiani di sosta.
- **Spazio di manovra** della sedia a ruote: rotazione di 360° in un cerchio di **Ø 150 cm**.
- **Porte**: luce netta min. **80 cm** (75 cm per le interne in adattabilità).
- **Ascensore** accessibile: cabina di dimensioni minime (es. 140×110 cm) con porta da 80 cm.
- **Servizi igienici**: spazio laterale al WC e accostamento al lavabo.

## Superamento dei vincoli

Anche in presenza di **vincoli** (es. beni tutelati) va ricercata la soluzione che garantisca il massimo grado di accessibilità compatibile, con soluzioni alternative quando quelle standard non sono praticabili.
""",
    },
    {
        "slug": "codice-appalti",
        "category": "appalti",
        "title": "Appalti e contratti pubblici",
        "subtitle": "Dal D.Lgs. 50/2016 al nuovo Codice D.Lgs. 36/2023",
        "read_minutes": 7,
        "key_points": [
            "Il Codice vigente è il D.Lgs. 36/2023 (ha sostituito il D.Lgs. 50/2016).",
            "Procedure: aperta, ristretta, negoziata, affidamento diretto (sottosoglia).",
            "Criteri di aggiudicazione: OEPV (offerta economicamente più vantaggiosa) o minor prezzo.",
        ],
        "content": """## Il Codice dei contratti pubblici

Il nuovo **Codice dei Contratti Pubblici – D.Lgs. 31 marzo 2023, n. 36** ha sostituito il precedente **D.Lgs. 50/2016**. Disciplina appalti e concessioni di lavori, servizi e forniture, ispirandosi ai principi di **risultato, fiducia e accesso al mercato**, oltre a trasparenza, concorrenza e proporzionalità.

## I livelli di progettazione

Il nuovo Codice riduce i livelli a **due**: **Progetto di Fattibilità Tecnico-Economica (PFTE)** e **Progetto Esecutivo** (il progetto definitivo è stato assorbito). Segue la fase di **esecuzione**.

## Le procedure di affidamento

- **Procedura aperta**: tutti gli operatori possono presentare offerta.
- **Procedura ristretta**: previa selezione dei candidati (prequalifica).
- **Procedura negoziata** (con o senza bando).
- **Affidamento diretto** e procedure semplificate per i **contratti sotto soglia** (soglie europee periodicamente aggiornate).

## Criteri di aggiudicazione

- **OEPV – Offerta Economicamente Più Vantaggiosa**: rapporto qualità/prezzo (obbligatoria per servizi ad alta intensità di manodopera, servizi di ingegneria e architettura oltre soglia).
- **Minor prezzo**, in casi definiti.

## Figure e fasi

Il **RUP – Responsabile Unico del Progetto** governa l'intero ciclo. In esecuzione operano il **Direttore dei Lavori**, il **coordinatore per la sicurezza** e, a fine opera, il **collaudo** (tecnico-amministrativo e statico). Sono previsti strumenti come l'**accordo quadro**, il **dialogo competitivo** e il **partenariato pubblico-privato**.
""",
    },
    {
        "slug": "catasto-estimo",
        "category": "catasto",
        "title": "Catasto ed estimo",
        "subtitle": "Catasto terreni e fabbricati, aspetti economici del valore",
        "read_minutes": 6,
        "key_points": [
            "Il Catasto è l'inventario dei beni immobili; è un catasto 'non probatorio'.",
            "Catasto Terreni e Catasto Fabbricati; l'unità è la particella / unità immobiliare.",
            "L'estimo valuta il bene secondo l'aspetto economico legato allo scopo della stima.",
        ],
        "content": """## Il Catasto

Il **Catasto** è l'inventario dei beni immobili del territorio nazionale, gestito dall'**Agenzia delle Entrate**. In Italia è **non probatorio**: non fa piena prova della proprietà (quella spetta ai registri immobiliari/conservatoria), ma ha finalità **fiscali** e di individuazione.

Si distingue in:

- **Catasto Terreni (CT)**: unità elementare la **particella**; qualità di coltura, classe, **reddito dominicale e agrario**.
- **Catasto Fabbricati (CF)** (ex NCEU): unità elementare l'**unità immobiliare urbana (UIU)**, classificata per **categoria** (A residenze, B collettività, C commerciali, D speciali, E particolari), **classe** e **consistenza** (vani/mq/mc), da cui la **rendita catastale**.

L'identificativo è dato da **Foglio – Particella (mappale) – Subalterno**.

## Estimo: i cinque aspetti economici

La stima associa al bene un **aspetto economico** coerente con lo **scopo**:

1. **Valore di mercato** (più probabile prezzo di scambio).
2. **Valore di costo** (costo di produzione/ricostruzione).
3. **Valore di trasformazione** (valore del prodotto trasformato meno costi di trasformazione).
4. **Valore di capitalizzazione** (attualizzazione dei redditi futuri: V = R/r).
5. **Valore complementare** e valore di surrogazione.

## Principi

Vale il **principio dell'ordinarietà** (riferimento al comportamento medio del mercato) e la **comparazione** con beni simili. Per i fabbricati civili si usa spesso il metodo **sintetico-comparativo** (€/mq); per le aree edificabili il **valore di trasformazione**.
""",
    },
    {
        "slug": "professione-deontologia",
        "category": "professione",
        "title": "Professione: Ordine, deontologia e compensi",
        "subtitle": "Abilitazione, obblighi deontologici, equo compenso",
        "read_minutes": 5,
        "key_points": [
            "L'iscrizione all'Albo (sez. A e B) è requisito per l'esercizio della professione.",
            "Le tariffe minime sono abolite (DL 1/2012); vige il preventivo e l'equo compenso.",
            "Obblighi: formazione continua, assicurazione RC professionale, deontologia.",
        ],
        "content": """## Accesso alla professione

Superato l'**Esame di Stato**, ci si iscrive all'**Albo dell'Ordine degli Architetti P.P.C.**, articolato in **sezione A** (architetto, laurea magistrale) e **sezione B** (architetto iunior, laurea triennale), con settori (architettura, pianificazione, paesaggio, conservazione).

## Obblighi del professionista

- **Formazione Continua** (crediti formativi professionali – CFP obbligatori).
- **Assicurazione RC professionale** obbligatoria (DPR 137/2012).
- Rispetto del **Codice Deontologico**: indipendenza, correttezza, lealtà verso colleghi e committenti, riservatezza, divieto di concorrenza sleale.

## Compensi

Le **tariffe minime** sono state **abrogate** (DL 1/2012 e L. 27/2012). Il professionista deve rendere noto al cliente un **preventivo** (di norma scritto) con il grado di complessità dell'incarico. Per i compensi nei rapporti con la PA vale il **DM 17/6/2016 (decreto parametri)** come riferimento e la disciplina dell'**equo compenso (L. 49/2023)**.

## Ruoli tecnici

- **Progettista**: redige il progetto.
- **Direttore dei Lavori (DL)**: controlla la corretta esecuzione conforme al progetto e contabilizza i lavori.
- **Coordinatore della sicurezza** (D.Lgs. 81/2008): in fase di progettazione (CSP) ed esecuzione (CSE).
- **Collaudatore**: verifica tecnica ed economica dell'opera.
""",
    },
    {
        "slug": "sicurezza-cantieri",
        "category": "professione",
        "title": "Sicurezza nei cantieri (D.Lgs. 81/2008)",
        "subtitle": "Titolo IV: PSC, POS, coordinatori e responsabilità",
        "read_minutes": 5,
        "key_points": [
            "Il Testo Unico sicurezza è il D.Lgs. 81/2008; il Titolo IV riguarda i cantieri.",
            "PSC redatto dal CSP; POS redatto da ciascuna impresa esecutrice.",
            "Coordinatori CSP (progettazione) e CSE (esecuzione) in presenza di più imprese.",
        ],
        "content": """## Il Testo Unico

Il **D.Lgs. 9 aprile 2008, n. 81** è il Testo Unico in materia di **salute e sicurezza sul lavoro**. Il **Titolo IV** disciplina i **cantieri temporanei o mobili**.

## Le figure

- **Committente** e **Responsabile dei Lavori**: titolari degli obblighi generali.
- **Coordinatore per la Sicurezza in fase di Progettazione (CSP)**: redige il **PSC** e il **fascicolo dell'opera**.
- **Coordinatore per la Sicurezza in fase di Esecuzione (CSE)**: verifica l'applicazione del PSC, coordina le imprese, sospende i lavori in caso di pericolo grave.
- **Imprese esecutrici**: redigono il **POS (Piano Operativo di Sicurezza)**.

La nomina dei coordinatori è obbligatoria quando è prevista la **presenza di più imprese**, anche non contemporanea.

## I documenti

- **PSC – Piano di Sicurezza e Coordinamento**: valuta i rischi del cantiere e le misure, l'organizzazione, le interferenze.
- **POS – Piano Operativo di Sicurezza**: documento della singola impresa relativo al proprio cantiere.
- **Fascicolo dell'opera**: informazioni utili alla sicurezza nelle future manutenzioni.
- **Notifica preliminare** all'organo di vigilanza nei casi previsti.

## Responsabilità

Il sistema è **sanzionatorio penale/amministrativo**. La corretta attribuzione dei ruoli e la vigilanza effettiva sono decisive per la ripartizione delle responsabilità.
""",
    },
    {
        "slug": "elementi-costruttivi",
        "category": "costruttivi",
        "title": "Elementi costruttivi dell'edificio",
        "subtitle": "Fondazioni, strutture verticali, solai, coperture, involucro",
        "read_minutes": 6,
        "key_points": [
            "Fondazioni dirette (plinti, travi rovesce, platea) e indirette (pali).",
            "Chiusure verticali: tamponature e pareti, con isolamento e tenuta.",
            "Coperture a falda o piane; fondamentali impermeabilizzazione e barriera al vapore.",
        ],
        "content": """## Fondazioni

Trasferiscono i carichi al terreno. Si distinguono in:

- **Dirette (superficiali)**: **plinti** (isolati), **travi rovesce**, **platea/fondazione a graticcio**. Usate con terreni di buona portanza a bassa profondità.
- **Indirette (profonde)**: **pali** (battuti o trivellati), che portano i carichi a strati profondi resistenti. Impiegate con terreni scadenti in superficie.

## Strutture portanti verticali

- **Puntiformi**: **pilastri** (c.a., acciaio, legno) in sistemi a telaio.
- **Continue**: **muratura** portante o **pareti/setti** in c.a. (spesso con funzione sismoresistente).

## Solai

Elementi orizzontali portanti: **latero-cementizi** (travetti + pignatte + soletta), **a soletta piena**, **predalles**, **lamiera grecata collaborante**, **legno**. Assolvono anche a requisiti acustici (calpestio) e di resistenza al fuoco.

## Chiusure verticali

**Tamponature** (in telaio) e **pareti**: devono garantire isolamento termico e acustico, tenuta all'acqua e all'aria. Sistemi a **cappotto** o a **parete ventilata** migliorano le prestazioni e controllano i ponti termici.

## Coperture

- **A falda** (tetti inclinati): smaltimento rapido dell'acqua, manto di copertura (tegole, coppi, lamiera).
- **Piane**: richiedono pendenze minime, **impermeabilizzazione** (guaine), **barriera al vapore**, isolamento (tetto caldo/rovescio) e strato di protezione.

## Stratigrafia funzionale

In ogni chiusura si controllano, dall'interno all'esterno: **barriera al vapore, isolante termico, impermeabilizzazione**, evitando la **condensa interstiziale** e garantendo traspirabilità e durabilità.
""",
    },
]

# -----------------------------------------------------------------------------
# QUIZ — domande a risposta multipla con spiegazione dell'errore
# -----------------------------------------------------------------------------
QUESTIONS = [
    # URBANISTICA
    {"category": "urbanistica", "topic": "urbanistica-fondamenti", "question": "Qual è la legge urbanistica fondamentale italiana?",
     "options": ["L. 1150/1942", "L. 457/1978", "DPR 380/2001", "D.Lgs. 42/2004"], "correct": 0,
     "explanation": "La Legge Urbanistica Fondamentale è la L. 1150/1942. La L. 457/1978 riguarda il recupero edilizio, il DPR 380/2001 è il Testo Unico dell'Edilizia e il D.Lgs. 42/2004 è il Codice dei beni culturali."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "Nel DM 1444/68 la zona 'A' identifica:", 
     "options": ["I centri storici", "Le zone di espansione", "Le zone produttive", "Le zone agricole"], "correct": 0,
     "explanation": "La zona A è quella di interesse storico-artistico (centri storici). L'espansione è la C, le produttive la D, le agricole la E."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "Lo standard urbanistico minimo per la residenza è pari a:",
     "options": ["18 mq/abitante", "9 mq/abitante", "25 mq/abitante", "12 mq/abitante"], "correct": 0,
     "explanation": "Il DM 1444/68 fissa 18 mq/abitante di spazi pubblici per la residenza (istruzione, interesse comune, verde/sport, parcheggi). I 9 mq sono la sola quota di verde attrezzato."},
    {"category": "urbanistica", "topic": "zone-omogenee-standard", "question": "La distanza minima tra pareti finestrate di edifici antistanti (DM 1444/68) è:",
     "options": ["10 m", "5 m", "3 m", "6 m"], "correct": 0,
     "explanation": "Il limite inderogabile è 10 m tra pareti finestrate. I 3 m sono la distanza minima dal confine in molti regolamenti; non è il valore richiesto qui."},

    # EDILIZIA
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "Il Testo Unico dell'Edilizia è contenuto in:",
     "options": ["DPR 380/2001", "L. 1150/1942", "D.Lgs. 50/2016", "DM 1444/1968"], "correct": 0,
     "explanation": "Il DPR 380/2001 è il Testo Unico dell'Edilizia. Il D.Lgs. 50/2016 era il vecchio Codice appalti, il DM 1444/68 riguarda zone e standard."},
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "Quale intervento richiede di regola il Permesso di Costruire?",
     "options": ["Nuova costruzione", "Manutenzione ordinaria", "Tinteggiatura interna", "Sostituzione di infissi identici"], "correct": 0,
     "explanation": "La nuova costruzione richiede il Permesso di Costruire. La manutenzione ordinaria e le piccole opere rientrano nell'edilizia libera senza titolo."},
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "La CILA è richiesta per:",
     "options": ["Manutenzione straordinaria non strutturale", "Nuova costruzione", "Ristrutturazione urbanistica", "Demolizione e ricostruzione con aumento di volume"], "correct": 0,
     "explanation": "La CILA copre la manutenzione straordinaria NON strutturale e opere interne non in edilizia libera. Gli interventi 'pesanti' richiedono SCIA o Permesso di Costruire."},
    {"category": "edilizia", "topic": "titoli-abilitativi", "question": "Il contributo di costruzione è composto da:",
     "options": ["Oneri di urbanizzazione + costo di costruzione", "Solo IVA", "Solo imposta di registro", "Oneri di urbanizzazione soltanto"], "correct": 0,
     "explanation": "Il contributo è dato dagli oneri di urbanizzazione (primaria e secondaria) sommati al costo di costruzione."},

    # STRUTTURE
    {"category": "strutture", "topic": "ntc-2018-stati-limite", "question": "Le NTC 2018 adottano il metodo:",
     "options": ["Semiprobabilistico agli stati limite", "Delle tensioni ammissibili", "Deterministico al collasso", "Empirico tabellare"], "correct": 0,
     "explanation": "Le NTC 2018 usano il metodo semiprobabilistico agli stati limite con coefficienti parziali. Il metodo alle tensioni ammissibili è quello storico ormai superato."},
    {"category": "strutture", "topic": "ntc-2018-stati-limite", "question": "Lo SLU riguarda principalmente:",
     "options": ["La sicurezza/collasso della struttura", "Le deformazioni in esercizio", "Il comfort acustico", "Le vibrazioni percepibili"], "correct": 0,
     "explanation": "Lo Stato Limite Ultimo riguarda la sicurezza (collasso, rottura, instabilità). Deformazioni, fessurazione e vibrazioni sono Stati Limite di Esercizio (SLE)."},
    {"category": "strutture", "topic": "materiali-predimensionamento", "question": "Nel calcestruzzo armato la resistenza a trazione è affidata a:",
     "options": ["L'acciaio delle armature", "Il calcestruzzo", "Gli inerti", "Il copriferro"], "correct": 0,
     "explanation": "Il calcestruzzo lavora bene a compressione ma poco a trazione: la trazione è affidata alle armature in acciaio."},
    {"category": "strutture", "topic": "materiali-predimensionamento", "question": "Una regola pratica di predimensionamento della trave in c.a. suggerisce un'altezza pari a circa:",
     "options": ["L/10 della luce", "L/2 della luce", "L/40 della luce", "L della luce"], "correct": 0,
     "explanation": "Indicativamente l'altezza di una trave si assume h ≈ L/10÷L/12 della luce. È un valore di primo tentativo da verificare."},

    # SISMICA
    {"category": "sismica", "topic": "criteri-antisismici", "question": "In quante zone sismiche è classificato il territorio dopo l'OPCM 3274/2003?",
     "options": ["4", "2", "6", "10"], "correct": 0,
     "explanation": "Il territorio è suddiviso in 4 zone sismiche (1 massima pericolosità, 4 minima)."},
    {"category": "sismica", "topic": "criteri-antisismici", "question": "La 'gerarchia delle resistenze' (capacity design) mira a:",
     "options": ["Far precedere i meccanismi duttili a quelli fragili", "Massimizzare la rigidezza", "Ridurre il peso proprio", "Aumentare le luci"], "correct": 0,
     "explanation": "Il capacity design impone che i meccanismi duttili (es. flessione delle travi) si attivino prima di quelli fragili (taglio, nodi), evitando collassi improvvisi."},
    {"category": "sismica", "topic": "criteri-antisismici", "question": "Un intervento che riporta l'edificio ai livelli di sicurezza di norma si definisce:",
     "options": ["Adeguamento", "Miglioramento", "Riparazione locale", "Manutenzione"], "correct": 0,
     "explanation": "L'adeguamento riporta l'edificio ai livelli richiesti dalla norma; il miglioramento aumenta la sicurezza senza raggiungerli pienamente; l'intervento locale interessa singole parti."},

    # INCENDI
    {"category": "incendi", "topic": "prevenzione-incendi", "question": "Nella sigla REI, la lettera 'I' indica:",
     "options": ["Isolamento termico", "Impermeabilità", "Illuminazione", "Inerzia"], "correct": 0,
     "explanation": "R = capacità portante, E = tenuta a fiamme/fumi, I = isolamento termico. Il numero indica i minuti di prestazione garantita."},
    {"category": "incendi", "topic": "prevenzione-incendi", "question": "Il Codice di Prevenzione Incendi è il:",
     "options": ["DM 3 agosto 2015", "DPR 151/2011", "DM 236/1989", "D.Lgs. 81/2008"], "correct": 0,
     "explanation": "Il Codice PI è il DM 3/8/2015 (approccio prestazionale). Il DPR 151/2011 elenca le attività soggette; il D.Lgs. 81/2008 è il TU sicurezza."},
    {"category": "incendi", "topic": "prevenzione-incendi", "question": "La compartimentazione serve a:",
     "options": ["Limitare la propagazione dell'incendio", "Aumentare il carico d'incendio", "Ridurre l'illuminazione", "Migliorare l'acustica"], "correct": 0,
     "explanation": "La compartimentazione suddivide l'edificio in compartimenti REI per contenere fiamme, calore e fumi limitandone la propagazione."},

    # ENERGETICO
    {"category": "energetico", "topic": "efficienza-energetica-ape", "question": "La trasmittanza termica U si misura in:",
     "options": ["W/m²K", "kWh/anno", "MJ/m²", "dB"], "correct": 0,
     "explanation": "La trasmittanza U si esprime in W/m²K: più è bassa, migliore è l'isolamento. MJ/m² è il carico d'incendio, dB riguarda l'acustica."},
    {"category": "energetico", "topic": "efficienza-energetica-ape", "question": "La migliore classe energetica nell'APE è:",
     "options": ["A4", "A", "A+", "B"], "correct": 0,
     "explanation": "La scala va da A4 (migliore) a G (peggiore): esistono A1, A2, A3, A4. Quest'ultima è la più efficiente."},
    {"category": "energetico", "topic": "efficienza-energetica-ape", "question": "L'APE deve essere redatto da:",
     "options": ["Un tecnico abilitato e indipendente", "Il proprietario", "L'impresa costruttrice sempre", "Il notaio"], "correct": 0,
     "explanation": "L'Attestato di Prestazione Energetica è redatto da un tecnico abilitato e indipendente (certificatore) e serve in vendita, locazione e nuove costruzioni."},

    # ACUSTICA
    {"category": "acustica", "topic": "acustica-edilizia", "question": "I requisiti acustici passivi degli edifici sono fissati dal:",
     "options": ["DPCM 5/12/1997", "L. 447/1995", "DM 1444/1968", "DPR 380/2001"], "correct": 0,
     "explanation": "Il DPCM 5/12/1997 fissa i requisiti acustici passivi. La L. 447/1995 è la legge quadro sull'inquinamento acustico."},
    {"category": "acustica", "topic": "acustica-edilizia", "question": "Il parametro L'n,w riguarda:",
     "options": ["Il rumore da calpestio dei solai", "L'isolamento di facciata", "Il rumore degli impianti", "Il potere fonoisolante delle pareti"], "correct": 0,
     "explanation": "L'n,w è il livello di rumore da calpestio dei solai (più basso è, meglio è). D2m,nT,w è la facciata, R'w le partizioni."},

    # BARRIERE
    {"category": "barriere", "topic": "barriere-architettoniche", "question": "Quale livello garantisce la fruizione di OGNI spazio in autonomia?",
     "options": ["Accessibilità", "Visitabilità", "Adattabilità", "Agibilità"], "correct": 0,
     "explanation": "L'accessibilità è il livello più alto (ogni spazio fruibile). La visitabilità riguarda spazi di relazione e un servizio, l'adattabilità la modificabilità futura."},
    {"category": "barriere", "topic": "barriere-architettoniche", "question": "La pendenza massima di norma per una rampa accessibile è:",
     "options": ["8%", "15%", "20%", "3%"], "correct": 0,
     "explanation": "Il DM 236/89 fissa la pendenza massima all'8% (con deroghe per brevi tratti). Serve inoltre uno spazio di rotazione Ø 150 cm per la sedia a ruote."},

    # APPALTI
    {"category": "appalti", "topic": "codice-appalti", "question": "Il Codice dei contratti pubblici vigente è il:",
     "options": ["D.Lgs. 36/2023", "D.Lgs. 50/2016", "D.Lgs. 163/2006", "L. 109/1994"], "correct": 0,
     "explanation": "Il Codice vigente è il D.Lgs. 36/2023, che ha sostituito il D.Lgs. 50/2016 (a sua volta successore del D.Lgs. 163/2006 e della L. Merloni 109/1994)."},
    {"category": "appalti", "topic": "codice-appalti", "question": "L'acronimo OEPV indica:",
     "options": ["Offerta Economicamente Più Vantaggiosa", "Opera Edile a Priorità Variabile", "Ordine Esecutivo Pubblico di Vigilanza", "Offerta Estesa a Più Vincitori"], "correct": 0,
     "explanation": "OEPV = Offerta Economicamente Più Vantaggiosa, criterio basato sul rapporto qualità/prezzo, alternativo al minor prezzo."},
    {"category": "appalti", "topic": "codice-appalti", "question": "Chi governa l'intero ciclo dell'appalto pubblico?",
     "options": ["Il RUP", "Il collaudatore", "Il progettista", "Il fornitore"], "correct": 0,
     "explanation": "Il RUP (Responsabile Unico del Progetto) governa tutte le fasi: programmazione, progettazione, affidamento ed esecuzione."},

    # CATASTO
    {"category": "catasto", "topic": "catasto-estimo", "question": "L'identificativo catastale di un fabbricato è dato da:",
     "options": ["Foglio, particella, subalterno", "Solo particella", "Solo foglio", "Via e numero civico"], "correct": 0,
     "explanation": "L'unità immobiliare urbana è individuata da Foglio, Particella (mappale) e Subalterno."},
    {"category": "catasto", "topic": "catasto-estimo", "question": "Il valore di capitalizzazione si ottiene:",
     "options": ["Attualizzando i redditi futuri (V = R/r)", "Sommando i costi di costruzione", "Dal solo prezzo di mercato", "Dal valore di trasformazione"], "correct": 0,
     "explanation": "Il valore di capitalizzazione attualizza i redditi futuri: V = R/r, dove R è il reddito e r il saggio di capitalizzazione."},

    # PROFESSIONE
    {"category": "professione", "topic": "professione-deontologia", "question": "Le tariffe professionali minime obbligatorie sono state:",
     "options": ["Abrogate (DL 1/2012)", "Rese obbligatorie", "Raddoppiate", "Sostituite dall'IVA"], "correct": 0,
     "explanation": "Le tariffe minime sono state abolite dal DL 1/2012: oggi vige il preventivo al cliente e la disciplina dell'equo compenso."},
    {"category": "professione", "topic": "sicurezza-cantieri", "question": "Chi redige il PSC?",
     "options": ["Il Coordinatore per la Sicurezza in fase di Progettazione (CSP)", "Ogni impresa esecutrice", "Il direttore dei lavori", "Il committente in prima persona"], "correct": 0,
     "explanation": "Il PSC è redatto dal CSP. Il POS è invece redatto da ciascuna impresa esecutrice per il proprio cantiere."},
    {"category": "professione", "topic": "sicurezza-cantieri", "question": "La nomina dei coordinatori per la sicurezza è obbligatoria quando:",
     "options": ["È prevista la presenza di più imprese, anche non contemporanea", "Il cantiere dura meno di un giorno", "C'è una sola impresa e un solo lavoratore", "Non ci sono rischi"], "correct": 0,
     "explanation": "Il Titolo IV del D.Lgs. 81/2008 richiede i coordinatori in presenza di più imprese esecutrici, anche non contemporaneamente."},

    # COSTRUTTIVI
    {"category": "costruttivi", "topic": "elementi-costruttivi", "question": "I pali di fondazione sono un esempio di fondazione:",
     "options": ["Indiretta (profonda)", "Diretta (superficiale)", "A platea", "A trave rovescia"], "correct": 0,
     "explanation": "I pali sono fondazioni indirette/profonde, usate quando gli strati superficiali sono scadenti. Plinti, travi rovesce e platee sono fondazioni dirette."},
    {"category": "costruttivi", "topic": "elementi-costruttivi", "question": "In una copertura piana la barriera al vapore serve a:",
     "options": ["Impedire la condensa interstiziale", "Sostenere i carichi", "Isolare acusticamente", "Aumentare la pendenza"], "correct": 0,
     "explanation": "La barriera al vapore, posta sul lato caldo, limita la migrazione del vapore e previene la condensa interstiziale nello strato isolante."},
]

# -----------------------------------------------------------------------------
# FLASHCARD — ripetizione veloce
# -----------------------------------------------------------------------------
FLASHCARDS = [
    {"category": "urbanistica", "front": "Legge urbanistica fondamentale", "back": "L. 1150/1942"},
    {"category": "urbanistica", "front": "Decreto su zone omogenee e standard", "back": "DM 1444/1968"},
    {"category": "urbanistica", "front": "Standard residenziale minimo", "back": "18 mq/abitante di spazi pubblici"},
    {"category": "urbanistica", "front": "Distanza minima tra pareti finestrate", "back": "10 metri (DM 1444/68)"},
    {"category": "edilizia", "front": "Testo Unico dell'Edilizia", "back": "DPR 380/2001"},
    {"category": "edilizia", "front": "Titolo per la nuova costruzione", "back": "Permesso di Costruire (art. 10)"},
    {"category": "edilizia", "front": "Cosa copre la CILA?", "back": "Manutenzione straordinaria NON strutturale e opere interne"},
    {"category": "edilizia", "front": "Contributo di costruzione", "back": "Oneri di urbanizzazione + costo di costruzione"},
    {"category": "strutture", "front": "Metodo delle NTC 2018", "back": "Semiprobabilistico agli stati limite (E_d ≤ R_d)"},
    {"category": "strutture", "front": "SLU vs SLE", "back": "SLU = sicurezza/collasso; SLE = esercizio (deformazioni, fessure, comfort)"},
    {"category": "strutture", "front": "Predimensionamento trave in c.a.", "back": "h ≈ L/10 della luce"},
    {"category": "strutture", "front": "Periodo di riferimento V_R", "back": "V_R = V_N · C_U (vita nominale × coeff. classe d'uso)"},
    {"category": "sismica", "front": "Numero di zone sismiche", "back": "4 zone (OPCM 3274/2003)"},
    {"category": "sismica", "front": "Capacity design", "back": "Gerarchia delle resistenze: duttile prima del fragile"},
    {"category": "sismica", "front": "Adeguamento vs miglioramento", "back": "Adeguamento = livello di norma; miglioramento = aumento parziale della sicurezza"},
    {"category": "incendi", "front": "Significato di R-E-I", "back": "R stabilità, E tenuta, I isolamento termico (minuti)"},
    {"category": "incendi", "front": "Codice di Prevenzione Incendi", "back": "DM 3 agosto 2015"},
    {"category": "incendi", "front": "Attività soggette a controllo VVF", "back": "Elencate nel DPR 151/2011 (cat. A, B, C)"},
    {"category": "energetico", "front": "Unità della trasmittanza U", "back": "W/m²K (più bassa = più isolante)"},
    {"category": "energetico", "front": "Scala delle classi APE", "back": "Da A4 (migliore) a G (peggiore)"},
    {"category": "energetico", "front": "Edificio NZEB", "back": "Edificio a energia quasi zero"},
    {"category": "acustica", "front": "Requisiti acustici passivi", "back": "DPCM 5/12/1997"},
    {"category": "acustica", "front": "Parametro del calpestio", "back": "L'n,w"},
    {"category": "barriere", "front": "Tre livelli DM 236/89", "back": "Accessibilità > Visitabilità > Adattabilità"},
    {"category": "barriere", "front": "Pendenza massima rampa", "back": "8% (spazio rotazione Ø 150 cm)"},
    {"category": "appalti", "front": "Codice contratti pubblici vigente", "back": "D.Lgs. 36/2023"},
    {"category": "appalti", "front": "OEPV", "back": "Offerta Economicamente Più Vantaggiosa"},
    {"category": "appalti", "front": "Figura che governa l'appalto", "back": "RUP – Responsabile Unico del Progetto"},
    {"category": "catasto", "front": "Identificativo catastale fabbricato", "back": "Foglio – Particella – Subalterno"},
    {"category": "catasto", "front": "Valore di capitalizzazione", "back": "V = R/r (attualizzazione dei redditi)"},
    {"category": "professione", "front": "Tariffe minime professionali", "back": "Abrogate (DL 1/2012); vige l'equo compenso"},
    {"category": "professione", "front": "Chi redige il PSC / il POS", "back": "PSC = CSP; POS = impresa esecutrice"},
    {"category": "costruttivi", "front": "Fondazioni profonde", "back": "Pali (battuti o trivellati)"},
    {"category": "costruttivi", "front": "Funzione barriera al vapore", "back": "Evitare la condensa interstiziale"},
]

# -----------------------------------------------------------------------------
# TRACCE D'ESAME (IUAV 2024) — sintesi delle prove estratte
# -----------------------------------------------------------------------------
TRACCE = [
    {
        "sezione": "Sezione A – Architettura",
        "tipo": "Prova pratica",
        "sessione": "I sessione 2024 (25 luglio 2024)",
        "titolo": "Progettazione architettonica di un piccolo edificio pubblico",
        "testo": "Il candidato sviluppi il progetto di un edificio di modeste dimensioni a destinazione pubblica/collettiva su un lotto assegnato, redigendo planimetria, piante, prospetti e sezioni in scala adeguata, con relazione tecnico-illustrativa. Dovrà motivare le scelte distributive, strutturali e tecnologiche, il rispetto degli standard urbanistici, dell'accessibilità (DM 236/89) e dei requisiti energetici, illustrando l'inserimento nel contesto.",
        "suggerimenti": "Imposta parti-to distributivo chiaro, rispetta distanze e altezze (DM 1444/68), cura accessibilità e uscite di sicurezza, giustifica sistema strutturale e stratigrafie dell'involucro.",
    },
    {
        "sezione": "Sezione A – Architettura",
        "tipo": "Prova scritta (candidati con tirocinio professionale)",
        "sessione": "I sessione 2024",
        "titolo": "Quesiti su normativa edilizia, urbanistica e professione",
        "testo": "Il candidato risponda a quesiti teorici relativi agli strumenti urbanistici, ai titoli abilitativi del DPR 380/2001, alle procedure dei lavori pubblici e agli obblighi deontologici e di sicurezza del professionista, argomentando con i riferimenti normativi.",
        "suggerimenti": "Collega i titoli abilitativi agli interventi, cita norme (DPR 380/2001, D.Lgs. 36/2023, D.Lgs. 81/2008) e chiarisci ruoli e responsabilità professionali.",
    },
    {
        "sezione": "Sezione A – Architettura",
        "tipo": "Prova pratica",
        "sessione": "II sessione 2024 (14 novembre 2024)",
        "titolo": "Recupero e rifunzionalizzazione di un edificio esistente",
        "testo": "Il candidato proponga il progetto di recupero/ristrutturazione di un manufatto esistente, definendo gli interventi (categoria ex art. 3 DPR 380/2001), le soluzioni strutturali di miglioramento/adeguamento sismico e l'aggiornamento prestazionale (energetico e accessibilità), con elaborati grafici e relazione.",
        "suggerimenti": "Classifica correttamente l'intervento, distingui miglioramento e adeguamento sismico, tratta il superamento delle barriere e il cappotto/isolamento con verifica della condensa.",
    },
    {
        "sezione": "Sezione A – Pianificazione territoriale",
        "tipo": "Prova pratica",
        "sessione": "I sessione 2024",
        "titolo": "Analisi e proposta di assetto per un ambito territoriale",
        "testo": "Il candidato analizzi un ambito territoriale assegnato e formuli una proposta di assetto coerente con la pianificazione sovraordinata (PTR/PTCP), individuando zone, standard, dotazioni e sistemi di mobilità, con relazione e schemi grafici.",
        "suggerimenti": "Applica il sistema gerarchico dei piani, dimensiona gli standard (DM 1444/68) e motiva le scelte di tutela e sostenibilità.",
    },
    {
        "sezione": "Sezione B – Architettura (iunior)",
        "tipo": "Prova pratica",
        "sessione": "I sessione 2024 (31 luglio 2024)",
        "titolo": "Progetto di una piccola unità residenziale",
        "testo": "Il candidato architetto iunior sviluppi il progetto di una piccola costruzione residenziale (o un intervento di limitata complessità), con piante, prospetti, sezioni e particolari costruttivi, nel rispetto dei limiti di competenza della sezione B.",
        "suggerimenti": "Rimani entro le competenze della sezione B, cura i particolari costruttivi (nodi, stratigrafie) e i requisiti minimi di accessibilità ed efficienza.",
    },
    {
        "sezione": "Sezione B – Pianificazione (iunior)",
        "tipo": "Prova pratica",
        "sessione": "I sessione 2024",
        "titolo": "Elaborazione di dati urbanistici e supporto al piano",
        "testo": "Il candidato elabori dati e cartografie a supporto della redazione di uno strumento urbanistico, rappresentando zonizzazione, standard e dotazioni con adeguata restituzione grafica e nota illustrativa.",
        "suggerimenti": "Concentrati sulla corretta rappresentazione di zone e standard e sulla coerenza con lo strumento sovraordinato.",
    },
]
