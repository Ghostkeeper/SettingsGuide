Slovníček pojmů
====
Tato stránka vysvětluje některé industriální výrazy používané společností Cura. Cura není vždy nejkonzistentnější, pokud jde o použití terminologie, takže některé termíny jsou synonyma.

* **Adaptive layers (adaptivní vrstvy):** Technika, která mění výšku vrstvy napříč tiskem, aby se snížila viditelnost topologie a přitom tisk probíhal přiměřeně rychle.
* **Aliasing:** Vada tisku, při které je na vnější straně výtisku viditelný limit rozlišení krokových motorů.
* **Anti-overhang mesh (síť proti převisu):** Model, který zabrání generování podpěry pro podepření jakéhokoli převisu, s nímž se model překrývá. Synonymum pro "blokátor podpěr".
* **Bead (korálek, kapka):** Pramínek materiálu poté, co byl položen vedením extrudéru. Termín "korálek" se používá ve vědě, kde je důležité vzít v úvahu skutečný tvar vlákna po jeho ztuhnutí. Podobně jako "linie".
* **Blob (kapka, hrudka):** Puntík přebytečného materiálu na vnější straně výtisku.
* **Bowden tube (bowdenová trubička):** Dutá, ohebná trubička používaná k vedení vlákna extrudérem.
* **Bridging (přemostění):** Technika tisku převislých linií ve vzduchu natažením přímek mezi dvěma opěrnými body. Cura může upravit parametry překlenovacích linií a upravit směr některých linií tak, aby vytvářely mosty.
* **Brim (krempa):** Materiál, připojený k okraji výtisku, který funguje jako sukénka, ale také lépe připevňuje výtisk k tiskové ploše tím, že poskytuje větší povrchovou plochu pro přilepení materiálu.
* **Build plate (tisková podložka):** Deska, na kterou se při konstrukci tiskne. Některé desky jsou zahřívány, aby materiál během tisku lépe držel.
* **Build volume (tiskový objem):** 3D prostor, ve kterém je tiskárna schopna vytlačovat materiál.
* **Coasting (doběh):** Technika, při které je poslední část vytlačovací dráhy vytištěna s 0% průtokem, čímž se uvolní přetlak v trysce.
* **Combing (objíždění):** Pohyb, který se pokouší během přesunů vyhnout se křížení stěn, aby se zabránilo vytvoření viditelné jizvy na vnější straně výtisku.
* **Coordinate origin (počátek souřadnic):** Místo na tiskové ploše, kam by se tryska přesunula, pokud by dostala pokyn k přesunu na souřadnice [0, 0, 0].
* **CuraEngine:** Program, který Cura používá při procesu slicování. Převádí 3D modely do g-kódu.
* **Cutting mesh (síť ořezu):** Model na tiskové ploše, který může změnit nastavení pro část svého objemu, která se překrývá se skutečnými tištěnými modely. Samotný model se nevytiskne, ale vystřihne části jiných modelů a poté může změnit nastavení nebo extrudér, kterým se tyto součásti tisknou.
* **Disallowed area (zakázaná oblast):** Místo na tiskové ploše, kam nesmíte umístit model pro tisk. Například proto, že by zasáhlo klipy přidržující podložku, aktivační věž, nebo proto, že váš tisk může mít pomocné části, které by se dostaly mimo objem tisku.
* **Draft shield (ochranný štít):** Plášť materiálu, který se tiskne kolem objektu, což udržuje konzistentní teplotu kolem výtisku.
* **Elephant's foot (sloní noha):** Vada tisku, kde je spodní strana tisku mírně širší, než je požadováno.
* **Extruder (extrudér):** Podavač, volitelně bowdenová trubička, tepelná zóna, horký konec a tryska dohromady. Některé tiskárny mají více extruderů nebo mají více než jedno vedení extrudéru. Zkratka pro "vedení extrudéru".
* **Extruder switch (přepínač extrudéru):** Typicky je aktivní vždy jen jeden z extrudérů. Přepínač extrudéru je, když mění aktivní extrudér z jednoho extrudéru na druhý.
* **Extruder train (souprava extrudéru):** Podavač, volitelně bowdenová trubička, tepelná zóna, horký konec a tryska dohromady. Některé tiskárny mají více souprav extrudérů nebo mají více než jednu z některých částí soupravy extrudéru.
* **Extrusion (extruze, vytlačování):** Akt protlačování vlákna soupravou extrudéru tak, že z trysky vychází materiál, který se snad ukládá na správné místo, aby vytvořil tisk.
* **Face (stěna, líc):** Rovný povrch 3D sítě. S trojúhelníkovými sítěmi (jediný druh, který dokáže Cura zpracovat) jsou všechny stěny trojúhelníky ve 3D prostoru.
* **Fan (ventilátor):** Ne jen jakýkoli ventilátor tiskárny, ale konkrétně ventilátor(y) připojené k tiskové hlavě, které ochladí tisk ihned po extrudování materiálu.
* **FDM printing (FDM tisk):** Fused Deposition Modelling (modelování fúzním ukládáním). Typ 3D tisku prováděného vytlačováním linií plastu v určitém tvaru. Toto je jediná technika 3D tisku, kterou Cura podporuje. Synonymum pro "FFF tisk".
* **Feeder (podavač):** Motor a převodovka, které tlačí nebo táhnou vlákno vytlačovacím zařízením.
* **Feedrate (posuv):** Rychlost, kterou se vlákno přivádí do extrudéru.
* **FFF printing (FFF tisk):** Fused Filament Fabrication (výroba taveného vlákna). Typ 3D tisku prováděného vytlačováním linií plastu v určitém tvaru. Toto je jediná technika 3D tisku, kterou Cura podporuje. Synonymum pro "FDM tisk".
* **Filament (vlákno):** Vlákno plastu přiváděné do 3D tiskárny. Dodávané namotané na cívce. Jakmile je extrudováno, už to není vlákno, ale jen materiál.
* **Flow (tok):** Rychlost vytlačovaného materiálu jako poměr jeho normální rychlosti. Více než 100% tok teoreticky vytlačuje více materiálu, než by se vešlo do přiděleného objemu. Méně než 100% tok teoreticky vytlačuje příliš málo materiálu.
* **Gantry (portál):** Mechanický rám, který pohybuje tiskovou hlavou podél objemu tisku.
* **Gap filling (vyplnění mezer):**Technika používaná Curou k vyplnění malých mezer v tisku materiálem pomocí velmi malých liniových segmentů.
* **Gradual infill (postupná výplň):** Technika, při které je množství materiálu sníženo v nižších vrstvách objemu, ale stále vysoké ve vyšších vrstvách, aby byl materiál správně nad ní správně podepřen. To se používá nejen pro materiál, ale také pro podpěru.
* **Hardness (tvrdost):** Měření výtisku, do jaké míry odolá elastické deformaci nebo propíchnutí.
* **Heater (topné těleso):** Topné těleso, které přivádí vlákno na teplotu potřebnou pro 3D tisk.
* **Heat zone (zóna ohřevu):** Zóna, ve které se vlákno ohřívá jak přichází k trysce. Na začátku tepelné zóny má vlákno pokojovou teplotu. Na konci je na teplotě tisku.
* **Hop (skok):** Technika, při které je tryska posunuta nahoru (+Z), aby mohla cestovat nad tiskem s trochou vůle. Synonymum pro "Z-skok".
* **Hot end (horký konec):** Horký kovový nebo keramický díl obsahující trysku, topný článek a teplotní čidlo.
* **Infill (výplň):** Struktura vytvořená na vnitřní straně výtisku, která drží horní povrch a poskytuje dodatečnou sílu výtisku.
* **Infill mesh (síť výplně):** Podobně jako "síť ořezu", ale aplikuje se pouze tam, kde se překrývá s objemem výplně jiného modelu. Toto je model, který upravuje nastavení pro výplň jiného modelu.
* **Inner walls (vnitřní stěny):** Všechny stěny kromě vnější stěny. Zatímco díl na vrstvě má pouze jednu vnější stěnu, může mít libovolný počet vnitřních stěn.
* **Inset (vnoření):** Operace na polygonech, která produkuje menší/tenčí mnohoúhelník, jehož obrys udržuje určitou vzdálenost od obrysu původního mnohoúhelníku. Vnoření se zápornou vzdáleností se říká "odsazení".
* **Ironing (žehlení):** Technika, při které prochází tryska vícekrát přes horní povrch, aby byl extra hladký.
* **Jerk (ryv):**Limit velikosti okamžité změny rychlosti použité na začátku každého pohybu. Není to totéž jako běžná definice "ryvu" ve fyzice!
* **Layer (vrstva):** 3D tisk se provádí v tenkých vrstvách materiálu. Tyto vrstvy jsou 2D tvary s určitou tloušťkou, které při vertikálním stohování vytvářejí 3D tisk.
* **Layer shift (posun vrstvy):** Vada tisku, kde je vodorovná poloha vrstvy neúmyslně posunuta, obvykle se také posunuje zbytek tisku.
* **Layer split (rozdělení vrstev):** Vada tisku, kde se vrstvy dostatečně dobře neslepí a otevře se prasklina.
* **Line (linie):** Pramen materiálu poté, co byl položen sestavou extrudéru. V Cuře jsou linie modelovány jako obdélníkové bloky s určitou šířkou, tloušťkou (výškou vrstvy) a délkou. Podobně jako "korálek".
* **Line segment (úsečka):** Aby se oddělil od pojmu "linie" pro 3D tisk, bude Cura při odkazu na úsečku v matematickém smyslu vždy používat celý výraz "úsečka" k označení přímé geometrické čáry omezené délky.
* **Material (materiál):** Materiál, ze kterého se skládá váš 3D tisk. Typicky termoplast v FFF tisku.
* **Mesh (síť):** Kolekce trojúhelníků, které společně tvoří model. Ačkoli se někdy používá jako synonymum pro "objekt" a "model", obvykle se používá spíše v kontextu dat než v případě něčeho, co byste chtěli tisknout.
* **Model (model):** 3D model načtený do 3D scény Cura (před slicováním). Synonymum pro "objekt".
* **Nozzle (tryska):** Otvor, kde tiskový materiál vystupuje z extrudéru.
* **Object (objekt):** 3D model načtený do 3D scény Cura (před slicováním). Synonymum pro "model".
* **Offset (odsazení):** Operace na mnohoúhelnících, která produkuje větší/tlustší mnohoúhelník, jehož obrys udržuje určitou vzdálenost od obrysu původního mnohoúhelníku. Posun se zápornou vzdáleností se nazývá "vnoření".
* **One-at-a-time mode (režim vše najednou):** Režim tisku více objektů, kde je každý objekt plně dokončen před pokračováním s dalším objektem, zatímco normálně vytiskne vrstvu pro každý objekt před pokračováním s další vrstvou.
* **Ooze shield (štít proti výtoku):** Plášť materiálu, který se tiskne kolem výtisku, který zachytí jakýkoli vyteklý materiál, když přesun pohybuje tryskou směrem k tisku.
* **Oozing (výtok):** Unikající materiál z trysky, i když to není zamýšleno. Typicky to zanechává řetězec materiálu podél dráhy pojezdu.
* **Outer wall (vnější stěna):** Nejvzdálenější stěna. Na každou vrstvu je pouze jedna vnější stěna.
* **Overextrusion (nad-extruze):** Vytlačování příliš velkého množství materiálu v omezeném objemu, což způsobí rozlití materiálu tam, kam nemá.
* **Overhang (převis):** Část tisku, která není (nebo není zcela) podepřena materiálem ve vrstvách pod ním. Pokud je převis příliš extrémní na to, aby se dobře tiskl, je nutná podpěra nebo přemostění.
* **Overpressure (přetlak):** Během tisku se komora trysky udržuje pod velkým tlakem, aby se zajistilo, že se materiál důsledně vytlačuje.
* **Parking (parkování):** Akt spočívající v pozastavení tisku na chvíli, když je tryska mimo tisk, aby materiál mohl nějakou dobu vychladnout.
* **Part (díl, část):** Spojitý tvar (mnohoúhelník) na jedné vrstvě. Jeden model se může při slicování v určitých vrstvách rozdělit na více částí.
* **Pattern (vzor):** Technika plnění objemu materiálem, i když ne nutně při 100% hustotě. Cura poskytuje výběr mezi několika vzory, jako jsou linie, mřížka, soustředný, čtyřboký atd.
* **Pillowing (polštářování):** Porucha tisku, při které se horní část pláště vyboulí nebo se zlomí mezi místa, kde leží na liniích výplně níže.
* **Polygon (mnohoúhelník):** 2D tvar nebo uzavřená smyčka skládající se z řady bodů s přímými segmenty mezi nimi.
* **Prime blob (zaváděcí kapka):** Část materiálu, který je vyčištěn na začátku tisku, aby se zaplnil extrudér.
* **Prime tower (aktivační věž):** Struktura vytvořená vedle tisku, která umožňuje tiskárně plnit trysky ve vyšších vrstvách, aniž by přebytečný materiál skončil na straně skutečného tisku. Používá se pro výtisky, kde je zapojeno více extruderů, aby se extrudér naplnil po chvíli v pohotovostním režimu.
* **Priming (plnění):** Akt čištění nějakého materiálu, aby se zajistilo, že je vlákno vyrovnáno se špičkou trysky a komora trysky je naplněna a správně natlakována. Obvykle se provádí na začátku tisku nebo po přepnutí extrudéru.
* **Purging (čištění):** Akt vytlačení nějakého materiálu jako odpadu. Běžným důvodem pro čištění je "plnění".
* **Raft (raft):** Technika pro zlepšení adheze tiskové plochy vytištěním pevné podložky pod tisk, která je později vyřazena. Podložka má velkou plochu a je vytištěna silnými liniemi, které dobře drží a zachycují jakékoli nepravidelnosti v rovinnosti podložky tisku.
* **Retraction (retrakce):** Akt použití podavače k vytlačení materiálu zpět do komory trysky. Obvykle se provádí k dočasnému zastavení toku materiálu z trysky pro čistý pohyb.
* **Ringing (zvlnění):** Vada tisku, kde se povrch vlní v důsledku nekonzistentního vytlačování nebo chvěním trysky. Obvykle se to stane po  příliš rychlém vytváření ostrých rohů.
* **Scar (jizva):** Místo poškození na vnější straně výtisku, kde tryska průchodem roztavila materiál.
* **Seam (šev):** Místo, kde začíná a končí uzavřená smyčka. Toto místo je obvykle viditelné na konečném výtisku, takže byste ho chtěli umístit na místo, kde to není příliš viditelné.
* **Shell (skořepina):** Stěny i plášť.
* **Skin (plášť):** Horní a spodní strana výtisku. Ty jsou vždy vytištěny se 100% hustotou, obvykle s liniovým vzorem. Synonymum pro "horní/dolní".
* **Skirt (sukénka):** Kontura nakreslená kolem tisku na první vrstvě, aby se materiál naplnil a aby uživatel mohl vidět, zda je podložka tisku zcela vyrovnaná.
* **Slicing (slicování):** Proces převodu 3D modelu do pokynů pro 3D tiskárnu pro jeho vytištění. V kontextu CuraEngine se to někdy také používá pro proces vytváření průřezů modelu, což je jedna z fází celého procesu slicování.
* **Spiralise mode (režim spiralizování):** Režim tisku pouze obrysu modelů, obvykle při postupném zvyšování souřadnice Z v celé vrstvě, aby se eliminoval šev v Z vytištěním modelu v jedné velké spirále. Mimo Cura je toto také známé jako "režim vázy".
* **Stand-by (pohotovostní stav):** Při tisku s více extrudéry je obvykle současně aktivní pouze jeden z extruderů. Ostatní extrudéry budou v pohotovostním stavu.
* **Stitching (sešití):** Část procesu slicování. Vytvoření průřezů skupiny trojúhelníků má za následek spoustu úseček v každé vrstvě. Sešití spojuje tyto úsečky do mnohoúhelníků a určuje, co je uvnitř vrstvy.
* **Strength (pevnost):** Zahrnující pojem označující různé míry odporu proti pohybu, včetně tvrdosti, tuhosti a houževnatosti při použití různých typů síly.
* **Stringing (strunování):** Během pojezdu při vytékání materiálu se vytvářejí tenké prameny materiálu zvaného "strunování". Prameny se nemusí nutně rozpínat po celé délce přesunu. Méně extrémní forma tohoto výsledku vede ke "kapkám".
* **Support (podpěra):** Část tisku, která je po vytištění odstraněna, ale je nutné ponechat tyto části tisku na místě, zatímco tisk stále probíhá, aby se zabránilo pádu nebo přílišnému poklesu materiálu.
* **Support blocker (blokátor podpěr):** Model, který zabrání generování podpěry na podepření jakéhokoli převisu, s nímž se model překrývá. Synonymum pro "síť proti převisu".
* **Support floor (podlaha podpěry):** Spodní strana podpěry, která se používá tam, kde podpěra spočívá na modelu. Tuto část podpěry lze volitelně vytisknout s různými nastaveními. U podpěry na tiskové podložce podlaha podpěry není.
* **Support infill (výplň podpěry):** Hlavní složka podpěry. Pokud není k dispozici žádné rozhraní podpěry, skládá se podpěra pouze z výplně podpěry.
* **Support interface (rozhraní podpěry):** Střecha a podlaha podpěry , kde model spočívá na podpěře a kde podpěra spočívá na modelu. Spodní strana podpěry, kde podpěra spočívá na tiskové podložce, nedostává rozhraní podpěry.
* **Support mesh (podpůrná síť):** Model, který je vyplněn podpůrnou strukturou místo, aby byl normálně vytištěn. Lze ho použít k přizpůsobení tvaru vaší podpěry.
* **Support roof (střecha podpěry):** Horní strana podpěry, která se používá tam, kde model spočívá na podpěře. Tuto část podpěry lze volitelně vytisknout s různými nastaveními.
* **Support towers (podpůrné věže):** Technika podpory velmi tenkých nebo malých částí tisku. Část je podepřena špičkou věže, která se dále dolů rozšiřuje, aby se podpěra při tisku nepřevrátila.
* **Thermoplastic (termoplast):** Typ plastu, který při tavení měkne. Pro FFF tisk lze použít pouze termoplasty.
* **Thickness (tloušťka):** Velikost nějaké struktury ve svislém směru (Z). Porovnejte se "šířkou".
* **Top/bottom (horní/dolní):** Horní a spodní strana výtisku. Ty jsou vždy vytištěny se 100% hustotou, obvykle s liniovým vzorem. Synonymum pro "plášť".
* **Top surface (horní povrch):** Nejvyšší část horního pláště. Zřídka může být tento horní povrch vytištěn více než 1 vrstvou se samostatným nastavením, aby se dosáhlo vyšší kvality, aniž by to stálo spoustu času navíc.
* **Topography (topografie):** Efekt, kdy omezená výška vrstvy změní téměř rovnou plochu na něco, co se podobá geografické výškové mapě s kruhy, kde končí vrstvy.
* **Toughness (tuhost):** Měření výtisku, jak moc dokáže odolat plastické deformaci.
* **Travel (move) (pojezd (přesun)):** Přesouvání trysky z jednoho místa na druhé bez vytlačování materiálu.
* **Underextrusion (pod-extruze):** Vytlačování příliš málo materiálu, pro řádné vyplnění objemu nebo správné vytvoření silných a souvislých korálků.
* **Underpressure (podtlak):** Při retrakci je komora trysky udržována v  podtlaku, aby nasávala materiál dovnitř, aby se zabránilo výtoku.
* **Vase mode (režim vázy):** Režim pro tisk pouze obrysů modelů, obvykle při postupném zvyšování souřadnice Z v celé vrstvě, aby se eliminoval spoj Z. Cura tomu vždy říká "spirálový režim".
* **Walls (stěny):** Boky tisku. Obíhají vodorovně kolem modelu.
* **Warping (deformace):** Deformace výtisku po tisku, v důsledku smršťování materiálu nebo v důsledku vnitřního namáhání tahem na materiál, zatímco ještě není ztuhlý.
* **Width (šířka):** Velikost nějaké struktury v horizontálním směru (X/Y). Porovnejte s "tloušťkou".
* **Winding order (pořadí vinutí):** Pořadí bodů tvořících mnohoúhelník. Buď ve směru hodinových ručiček, nebo proti směru hodinových ručiček. V Cuřa označuje pořadí vinutí proti směru hodinových ručiček pozitivní tvar, zatímco pořadí vinutí ve směru hodinových ručiček označuje otvor. Vstupní 3D modely musí mít při pohledu zvenčí trojúhelníky s pootočením proti směru hodinových ručiček.
* **Wiping (otírání):** Technika, díky které tryska záměrně protíná dříve potištěnou strukturu, aby setřela jakýkoli visící vyteklý materiál ze špičky trysky, aby se zabránilo tomu, aby byl tento materiál umístěn na vnější stranu tisku.
* **Wire printing (drátový tisk):** Technika tisku modelu tiskem pouze drátového modelu kolem jeho skořepiny. Vysoce experimentální.
* **Z seam (Z šev):** Viditelný bod na vnější stěně, kde se tryska pohybovala z jedné vrstvy na druhou. Často nesprávně použito místo jen "šev".
* **Z hop (Z skok):** Technika, při které je tryska posunuta nahoru (+ Z), aby mohla cestovat nad tiskem s trochou vůle. Synonymum pro "skok".