Glossary
====
This page explains some of the industry terms employed by Cura. Cura is not always the most consistent when it comes to usage of terminology, so some terms are synonyms.

* **Layer adattativi:** Tecnica capace di variare l'altezza dei layer durante la stampa per ridurre la visibilità degli strati, mantenendo una velocità di stampa ragionevolmente veloce.
* **Aliasing:** Errore di stampa dove il limite della risoluzione degli stepper risulta visibile nella parte esterna della stampa
* **Maglia Anti-overhang:** Un modello che impedirà la generazione del supporto per sostenere qualsiasi sporgenza con cui il modello si sovrappone. Sinonimo di "support blocker".
* **Cordone:** Un filo di materiale dopo che è stato posato dal carrello-estrusore. Il termine "cordone" è usato nella scienza in cui è importante considerare la forma effettiva del tratto di filamento dopo che è stato solidificato. Simile a "linea".
* **Blob:** Un punto di materiale in eccesso all'esterno della stampa.
* **Tubo Bowden:** Un tubo flessibile e vuoto, utilizzato per guidare il filamento attraverso il carrello-estrusore.
* **Bridging:** Tecnica per stampare linee sospese a mezz'aria, stirando linee dritte tra due punti. Cura è in grado di aggiustare i parametri dei tratti sospesi e correggerà la direzione di alcune linee per creare ponti.
* **Brim:** (Falda) Anello di materiale, attaccato alla stampa, che agisce come lo "skirt" ma che contribuisce anche ad una migliore adesione al piatto di stampa, fornendo maggior superficie al materiale per aderire.
* **Build plate:** (Piano di stampa) Piano sul quale viene posizionata la stampa, durante la realizzazione. Alcuni piani sono riscaldati per consentire al materiale una migliore adesione durante la fase di stampa.
* **Build volume:** (Volume di stampa) Volume all'interno del quale la stampante può arrivare ad estrudere materiale.
* **Coasting:** Tecnica in cui l'ultima parte di un percorso di estrusione viene stampata con flusso 0%, drenando l'ugello dalla pressione in eccesso.
* **Combing:** Movimento che cerca di evitare di attraversare i perimetri durante gli spostamenti, per evitare di creare una cicatrice visibile all'esterno della stampa.
* **Coordinate origin:** Posizione sul piano di stampa in cui si muoverebbe un ugello se richiesto di spostarsi alle coordinate [0, 0, 0].
* **CuraEngine:** Programma utilizzato da Cure per effettuare il lavori pesante legato al processo di "slicing". Trasforma un modello 3D in g-code.
* **Cutting mesh:** Strumento che relativamente al modello presente sul piano di stampa, può modificare le impostazioni per la parte del suo volume che si sovrappone a quella dei modelli previsti per la stampa. Il modello stesso non viene stampato, ma ritaglia pezzi di altri modelli e può quindi modificare le impostazioni o con quale carrello-estrusore vengano stampate quelle parti.
* **Disallowed area:** (Area non consentita) Un punto o una porzione sul piano di stampa su cui non è consentito posizionare un modello per la stampa. Ad esempio, perché colpirebbe le clip che tengono premuto il letto, la torre principale o perché la tua stampa avrebbe parti ausiliarie che uscirebbero dal volume di costruzione.
* **Draft shield:** Un guscio di materiale che viene stampato intorno all'oggetto, mantenendo costante la temperatura intorno alla stampa.
* **Elephant's foot:** (Zampa d'elefante) Un difetto per colpa del quale, la parte bassa della stampa si presenta più estesa del desiderato
* **Extruder:** (Estrusore) Complesso formato dallo spingifilo, tubo Bowden (opzionale), zona riscaldata, "hotend" ed ugello, insieme. Alcune stampanti hanno più di un estrusore o hanno alcune parti replicate più di una volta, rispetto al carrello-estrusore. Forma abbreviata per "carrello-estrusore".
* **Extruder switch:** (Cambio estrusore) Solitamente, c'è un solo estrusore attivo alla volta. Un cambio estrusore avviene passando da un estrusore ad un altro.
* **Extruder train:** (Carrello estrusore) Complesso formato dallo spingifilo, tubo Bowden (opzionale), zona riscaldata, "hotend" ed ugello, insieme. Alcune stampanti hanno più di un estrusore o hanno alcune parti replicate più di una volta, rispetto al carrello-estrusore.
* **Extrusion:** (Estrusione) L'azione di spingere il filamento attraverso l'estrusore affinché il materiale  estruso fuori dall'ugello venga depositato nel punto esatto del piano di stampa per la stampa.
* **Face:** (Faccia) Superficie piatta di un reticolo 3D. Con reticoli triangolari (gli unici che Cura è in grado di processare), tutte le facce sono triangoli nello spazio tridimensionale.
* **Fan:** (Ventola) Non una ventola qualunque della stampante ma, precisamente, la ventola (o le ventole), collegata all'estrusore, incaricata di raffreddare la stampa, appena estrusa.
* **FDM printing:** (Stampa FDM) Fused Deposition Modelling. Tecnologia di stampa 3D realizzata tramite l'estrusione di linee di plastica di una determinata forma. Questa tecnologia di stampa, è l'unica attualmente supportata da Cura. Sinonimo di stampa "FFF"
* **Feeder:** Complesso costituito da un motore ed una scatola di ingranaggi che spinge o tira il filamento attraverso l'estrusore.
* **Feedrate:** Velocità alla quale il filamento viene spinto all'interno dell'estrusore
* **FFF printing:** (Stampa FFF) Fused Filament Fabrication. Tecnologia di stampa realizzata tramite l'estrusione di linee di plastica in una determinata forma.Questa tecnologia di stampa, è l'unica attualmente supportata da Cura. Sinonimo di stampa "FDM"
* **Filament:** (Filamento) Filo di plastica utilizzato per alimentare la stampa 3D. Venduto in formato di bobine. Una volta estruso non è più filamento ma semplice materia.
* **Flow:** (Flusso) Il valore di estrusione del materiale in rapporto al suo parametro normale di riferimento. Valori superiori al 100% estruderanno, teoricamente, più materiale di quanto possa esserne contenuto in un volume specifico. Meno del 100%, teoricamente estruderà troppo poco materiale.
* **Gantry:** (Portale) Telaio con meccanica in grado di muovere l'estrusore all'interno del volume di stampa.
* **Gap filling:** Tecnica utilizzata da Cura per riempire piccoli spazi vuoti all'interno di una stampa, con del materiale, adottando tratti molto piccoli.
* **Gradual infill:** (Riempimento graduale) Tecnica grazie alla quale, la quantità di materiale  viene diminuita nelle parti inferiori del volume stampato ma resta più alto nei punti superiori per supportare correttamente il materiale. Ciò non accade solo per il materiale ma anche per i supporti.
* **Hardness:** (Durezza) Valore per una stampa di quanto possa resistere a deformazioni elastiche o perforazione.
* **Heater:** (Riscaldatore) Elemento riscaldante che porta il filamento alla temperatura richiesta per la stampa 3D.
* **Heat zone:** (Zona calda) La zona in cui il filamento si sta riscaldando nel tragitto verso l'ugello. All'inizio della zona termica il filamento è a temperatura ambiente. Alla fine è a temperatura di stampa.
* **Hop:** (Salto) Azione che provvede a sollevare l'ugello verso l'alto (+Z) al fine di spostarsi sopra la stampa con un minimo di tolleranza. Sinonimo di "Z Hop".
* **Hot end:** Parte in metallo o ceramica contenente l'ugello, l'elemento riscaldante ed il sensore di temperatura.
* **Infill:** (Riempimento) Struttura creata all'interno della stampa che sorregge il rivestimento superiore e fornisce rigidità strutturale e supporto alla stampa.
* **Infill mesh:** (Reticolo di riempimento) Similmente al reticolo di taglio (cutting mesh) ma applicato solamente laddove si vengano a sovrapporre i riempimenti di due volume. Questo modello aggiusta e corregge il riempimento di un modello terzo.
* **Inner walls:** (Perimetri interni) Tutti i muri tranne il muro più esterno. Sebbene una parte per ogni strato abbia un solo muro esterno, può avere un numero qualsiasi di pareti interne.
* **Inset:** (Riquadro) Un'operazione sui poligoni che produce un poligono più piccolo/sottile, il cui contorno mantiene una certa distanza dal contorno del poligono originale. Un riquadro con una distanza negativa è chiamato "offset".
* **Ironing:** Tecnica che passa sopra una superficie piana (tutte o solo la più alta), più volte per renderla extra liscia.
* **Jerk:** Limite per la quantità di variazione istantanea della velocità applicata all'inizio di ogni mossa. Questo termine non corrisponde allo stesso "jerk" impiegato in fisica!
* **Layer:** (Livelli o strati) La stampa 3D si compone di sottili strati di materiale. Questi strati sono forme in 2D con determinati spessori che, una volta bloccati verticalmente formano una stampa 3D
* **Layer shift:** Un errore di stampa che mostra la posizione orizzontale di un layer, involontariamente scarta lateralmente, spostando tipicamente a anche la stampa.
* **Layer split:** Un errore di stampa per colpa del quale i livelli non aderiscono a sufficientemente, rompendosi.
* **Line:** (Linea) Un tratto di materiale appena deposto in opera dall'estrusore. In Cura le linee sono modellate come se fossero blocchi rettangolari, di una certa larghezza e spessore (layer height) e lunghezza. Sinomino di "cordone".
* **Line segment:** (Segmento linea) Per distinguere col termine "linea" della stampa 3D, che si riferisce alla linea in senso matematico. Cura adotterà sempre il termine esteso "segmento linea" per indicare una linea geometrica dritta po di lunghezza limitata.
* **Material:** (Materiale) La materia di cui è fatta la tua stampa 3D. Tipicamente termoplastica in una stampa FFF.
* **Mesh:** (Reticolo) Una collezione di triangoli che, collegati tra di loro formano un modello. A volte viene utilizzato anche come sinonimo di "oggetto" o "modello" si usa tuttavia in contesti in cui si desidera indicare qualcosa che si vuole stampare.
* **Model:** (Modello) Modello 3D caricato all'interno della scena 3D di Cura (prima dello "slicing"). Sinonimo di "oggetto".
* **Nozzle:** (Ugello) L'apertura dalla quale il materiale di stampa esce, dopo il carrello filo.
* **Object:** (Oggetto) Modello 3D caricato nella scena 3D di Cura, prima di processare lo slicing. Sinonimo di "modello".
* **Offset:** Un'operazione sui poligoni che produce un poligono più grande/più grosso, il cui contorno mantiene una certa distanza dal contorno del poligono originale. Un offset con una distanza negativa è chiamato "inset".
* **One-at-a-time mode:** Modalità di stampa di più oggetti, in sequenza dove ogni oggetto viene completato prima di continuare con la stampa del successivo (mentre, normalmente, verrebbe stampato un layer per tutti gli oggetti, prima di procedere con il layer successivo.
* **Ooze shield:** Guscio di materiale realizzato attorno alla stampa che cattura il materiale trasudato quando l'ugello viene spostato verso la stampa.
* **Oozing:** Fuoriuscita di materiale dall'ugello mentre non in funzione. In genere questo lascia del materiale durante gli spostamenti dell'estrusore.
* **Outer wall:** Il perimetri più esterno. C'è solo una parete esterna per parte, per strato.
* **Overextrusion:** (Sovraestrusione) Estrusione di troppo materiale in un volume limitato con fuoriuscita del materiale dove non previsto dalla stampa.
* **Overhang:** (Sporgenza) Parte della stampa che non è (o non completamente) sostenuta dal materiale negli strati sottostanti. Se la sporgenza è troppo estrema per stampare bene, è necessario un supporto o un ponte.
* **Overpressure:** Durante la stampa, la camera degli ugelli viene mantenuta a pressione elevata per garantire che il materiale venga estruso in modo costante.
* **Parking:** (Parcheggio) Messa in pausa temporanea della stampa mentre l'ugello è distante, per consentire al materiale di raffreddarsi un po'.
* **Part:** (Parte) Forma chiusa (poligono), su un singolo strato. Un modello può separare in più elementi su alcuni strati, quando sottoposto al processo di slicing.
* **Pattern:** (Trama) Impiegata per riempire un volume con materiale, anche se non necessariamente al 100% di densità. Cura offre la scelta tra diversi modelli come linee, griglia, concentrici, tetraedrici, ecc.
* **Pillowing:** Difetto di stampa in cui l'ultimo strato superiore si gonfia o si rompe nel mezzo dove poggia sulle linee di riempimento sottostanti.
* **Polygon:** (Poligono) Una forma bidimensionale o un anello chiuso costituito da una serie di punti con segmenti di linea retta tra di loro.
* **Prime blob:** Massa di materiale che viene spurgata all'inizio di una stampa per preparare l'estrusore.
* **Prime tower:** (Torre di preparazione) Struttura creata, oltre la stampa, che permette alla stampante di spurgare i suoi ugelli sugli strati superiori senza che il materiale in eccesso finisca sul lato della stampa vera e propria. Utilizzato per le stampe in cui sono coinvolti più estrusori per spurgare un estrusore dopo essere stato in stand-by per un po'.
* **Priming:** (Preparazione) L'atto di spurgare del materiale per garantire che il filamento sia allineato alla punta dell'ugello e che la camera dell'ugello sia riempita e pressurizzata correttamente. Solitamente fatto all'inizio di una stampa o dopo un interruttore dell'estrusore.
* **Purging:** (Spurgo) L'atto di estrudere del materiale come scarto. Un motivo comune per lo spurgo è il "Priming".
* **Raft:** Una tecnica per migliorare l'adesione al piatto di stampa creando una lastra solida sotto la stampa che viene successivamente scartata. La lastra ha superficie estesa ed è stampata con linee spesse che aderiscono bene catturando qualsiasi irregolarità nella planarità della lastra di costruzione.
* **Retraction:** (Retrazione) Movimento utilizzato dallo spingifilo per riportare materiale nella camera dell'ugello. Solitamente fatto per impedire temporaneamente al materiale di fuoriuscire dall'ugello durante gli spostamenti della testa di stampa.
* **Ringing:** Difetto di stampa in cui la superficie oscilla a causa dell'estrusione incoerente o dell'oscillazione dell'ugello. In genere accade dopo aver creato angoli acuti troppo velocemente.
* **Scar:** (Cicatrice) Un punto danneggiato sulla superficie della stampa in cui l'ugello ha fuso il materiale durante il passaggio.
* **Seam:** (Cucitura) La posizione in cui inizia e si interrompe un perimetri. Questo punto è solitamente visibile sulla stampa finale ed è, quindi ragionevole posizionarlo in un punto in cui non sia molto visibile.
* **Shell:** (Guscio) Si riferisce sia alle pareti esterne che ai perimetri interni.
* **Skin:** (Pelle) Parte superiore ed inferiore della stampa. Sempre stampati al 100% di riempimento, tipicamente con un motivo a linee. Sinonimo di "superiore/inferiore".
* **Skirt:** (Gonna) Un bordo disegnato attorno alla stampa sul primo strato per preparare il materiale e per permettere all'utente di verificare se il piano di stampa sia completamente in piano.
* **Slicing:** Processo di conversione di un modello 3D in istruzioni/comandi per la stampa da parte di una stampante 3D. Nel contesto di CuraEngine, ciò viene talvolta utilizzato anche per il processo di creazione di sezioni trasversali del modello, che è una delle fasi del processo di slicing completo.
* **Spiralise mode:** Modalità per stampare solo il contorno dei modelli, in genere aumentando gradualmente la posizione di Z su tutto il livello eliminando la cucitura e stampando il modello in una grande spirale. Al di fuori di Cura questo è anche noto come "modalità vaso" o "vase mode".
* **Stand-by:** (Attesa) Quando si stampa con più estrusori, in genere è attivo solo uno degli estrusori alla volta. Gli altri estrusori restano in "stand-by".
* **Stitching:** (Cucitura) Parte del processo di slicing. Vengono realizzate sezioni trasversali tra gruppi di triangoli; ciò si traduce in un gruppo di segmenti di linea su ogni livello. La cucitura combina quei segmenti di linea in poligoni determinando quale sia il lato interno del livello.
* **Strength:** (Forza) Termine che indica varie misure di resistenza al movimento incluse durezza, rigidità e robustezza quando vengono applicati vari tipi di forza.
* **Stringing:** (Filatura) Trasuda di materiale che avviene durante gli spostamenti che crea fili sottili di materiale chiamati "stringhe" o "fili". I fili non si estendono necessariamente per tutta la lunghezza di uno spostamento. Una modalità meno estrema di questo fenomeno si traduce in "blob".
* **Support:** (Supporto) Parte della stampa che viene rimossa al termine del processo. I supporti sono a volte necessari per mantenere in posizione alcune porzioni di materiale mentre la stampa è ancora in corso. In questo modo si impedisce che il materiale collassi venendo stampato nel vuoto o che il pezzo oscilli troppo.
* **Support blocker:** Funzionalità che impedirà la generazione del supporto per supportare qualsiasi sporgenza con cui il modello si sovrappone. Sinonimo di "reticolo anti-sbalzo".
* **Support floor:** Il lato inferiore del supporto, impiegato nel punto in cui il supporto si collega al modello. Questa parte del supporto può essere stampata opzionalmente con impostazioni diverse. Non è previsto un pavimento per il supporto dove il supporto poggia sulla piano di stampa.
* **Support infill:** (Riempimento del supporto), Componente principale del supporto. Se non è presente un'interfaccia di supporto, il supporto consisterà solo nel riempimento stesso del supporto.
* **Support interface:** (Interfaccia del supporto) L'interfaccia di supporto per il tetto e la base, costituisce il punto in cui il modello si unisce ai supporti stessi. La parte inferiore del supporto che poggia sul piano di stampa, non usa interfacce di supporto.
* **Support mesh:** (Reticolo di supporto) Modalità utilizzata riempiendo con una struttura di supporto, al posto di una stampa convenzionale. Può essere impiegato per personalizzare la forma del proprio supporto.
* **Support roof:** (Tetto del supporto) Lato superiore del supporto, impiegato quando il modello giace su un supporto. Questa porzione di supporto può essere stampata personalizzandola con impostazioni differenti.
* **Support towers:** (Torri di supporto) Una tecnica per sostenere parti della stampa molto sottili o piccole. La parte viene sostenuta dalla punta di una torre che si allarga verso il basso in modo che il supporto non si rovesci durante la stampa.
* **Thermoplastic:** (Termoplastico) Un tipo di plastica che diventa morbida quando si scioglie. Solo i materiali termoplastici possono essere utilizzati per la stampa FFF.
* **Thickness:** (Spessore) Dimensione dell'oggetto che si estende in verticale, lungo l'asse Z. Confronta con "width" o "larghezza".
* **Top/bottom:** (Superiore ed inferiore), I lati superiori e inferiori della stampa. Vengono sempre stampati al 100% di densità, in genere con il motivo a linee. Sinonimo di "skin" o "pelle".
* **Top surface:** (Superficie superiore) La parte più alta dello strato superiore. Raramente più di 1 strato, questa superficie superiore può essere stampata con impostazioni separate per ottenere una maggiore qualità senza spendere molto tempo di stampa aggiuntivo.
* **Topography:** (Topografia) Effetto per colpa del quale la limitata altezza dello strato trasforma una superficie quasi piatta in qualcosa che assomiglia a una mappa geografica dell'altezza con anelli dove terminano gli strati.
* **Toughness:** (Durezza) Misura di una stampa volta ad indicare quanta resistenza possa opporre ad una deformazione plastica.
* **Travel (move):** (Trasferimento / spostamento) Lo spostamento dell'ugello da un punto del piano ad un altro punto, senza estrudere materiale.
* **Underextrusion:** (Sottoestrusione) Estrusione insufficiente di materiale tale da non poter riempire correttamente un volume o da creare cordoni omogenei e robusti.
* **Underpressure:** (Sottopressione) Durante la retrazione, la camera dell'ugello viene mantenuta a pressione negativa per risucchiare materiale al suo interno, impedendo la fuoriuscita di materiale.
* **Vase mode:** Modalità impiegata per stampare il singolo perimetro esterno del modello, tipicamente con una crescita graduale delle coordinate in Z, da layer a layer, usata per non impiegare le cuciture. In Cura viene chiamata "modalità spirale", "spiralized mode!
* **Walls:** (Muri perimetrali) I fianchi della stampa. Girano intorno al modello, orizzontalmente.
* **Warping:** (Deformazione) Deformazione della stampa che avviene a causa del ritiro del materiale o per sollecitazioni interne che tirano il materiale mentre non è ancora solidificato.
* **Width:** (Larghezza) dimensione di un oggetto in direzione orizzontale (X/Y). Confronta con "spessore".
* **Winding order:** La sequenza dei punti che formano un poligono. O in senso orario o antiorario. In Cura, un ordine di avvolgimento in senso antiorario indica una forma positiva mentre un ordine di avvolgimento in senso orario indica un foro. I modelli 3D di input devono avere triangoli con ordine di avvolgimento in senso antiorario se visti dall'esterno.
* **Wiping:** Tecnica per fare in modo che l'ugello sorvoli una forma precedentemente stampata apposta per rimuovere il materiale trasudato che penzola dalla punta dell'ugello, per evitare che quel materiale venga lasciato all'esterno della stampa.
* **Wire printing:** Tecnica per stampare un modello usando solo un wireframe attorno al suo guscio. Altamente sperimentale.
* **Z seam:** Un punto visibile sulla parete esterna in cui l'ugello si è spostato da uno strato all'altro. Spesso utilizzato in modo errato al posto della semplice "cucitura".
* **Z hop:** Tecnica grazie alla quale l'ugello viene spostato verso l'alto (+Z) per sorvolare la stampa con un po' di tolleranza. Sinonimo di "salto".
