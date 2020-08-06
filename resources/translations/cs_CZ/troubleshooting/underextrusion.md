Pod-extruze
====
Jedním z nejčastějších problémů s 3D tiskem je to, že tiskárna nevysouvá dostatek materiálu k vytvoření pěkného pevného objektu. Když k tomu dojde, mluvíme o "pod-extruzi": Tryska vytlačuje méně materiálu, než se očekávalo.

![Extrémní případ podextruze, kde můžete dokonce vidět vnitřek objektu](../../../articles/images/underextrusion.jpg)

Podextruze se také může projevit mnoha způsoby. V nejextrémnějším případě je objekt velmi křehký a jeho vnitřní části jsou vidět přes povrch. Někdy je vidět, že šířka linií je příliš malá, takže se nepřipojují k sousedním liniím. Někdy se projevuje pouze malými otvory v horním povrchu nebo malými zlomeninami ve stěnách.

Existuje mnoho možných příčin pod-extruze, což velmi ztěžuje odstraňování problémů. Zbytek tohoto článku popisuje některé z nejpravděpodobnějších příčin a jejich řešení.

Ucpaná tryska
----
Pokud vaše tiskárna dříve tiskla velmi dobře a najednou vykazuje pod-extruzi, aniž by došlo k významné úpravě tištěného objektu nebo parametrů, je pravděpodobné, že problém je někde ve vytlačovacím mechanismu. Obecně je nejslabším článkem tryska.

Ucpané trysky jsou běžným jevem u jakékoli 3D tiskárny. K tomu může dojít, když je vlákno kontaminováno prvky, které se dobře neroztavují a jsou tlačeny do trysky. K tomu může také dojít, když je vlákno samo v trysce spáleno. K tomu může dojít, když je plast příliš tvrdý nebo příliš dlouho udržovaný na vysoké hodnotě. Materiál se degraduje, polymery krystalizují a nakonec skončí kusem tvrdého plastu, který se v trysce neroztaví. Chcete-li to napravit, musíte z trysky odstranit zbytky.

Existuje několik technik pro odstranění nečistot z trysky. Pokud máte akupunkturní jehlu nebo jiný tenký kovový kolík, můžete ho vytlačit zdola. Nejběžnější technika je však známá jako "atomová vytažení". Pro provedení této techniky vezměte kus vlákna alespoň 50 cm dlouhý, nejlépe z materiálu s vysokou teplotou tání. Zahřívejte trysku na bod tání tohoto vlákna (například 190°C pro PLA) a potom tlačte vlákno kleštěmi dovnitř, dokud z trysky nevyjde určitý materiál. Potom nechte trysku vychladnout na teplotu skelného přechodu (např. 60°C pro PLA), a přitom tlačte vlákno dolů do trysky. Těsně před dosažením skelného přechodu vlákno rychle vytáhněte. Pokud je konec vlákna znečištěn černým plastem, odřízněte ho a zkuste to znovu, dokud nebude čistý. Zkuste něco vytisknout znovu a snad to bude nyní lepší.

Prokluzující podavač
----
Extrudér někdy nemá dostatečnou přilnavost na vláknu, aby ho tlačil dostatečně tvrdě dolů tryskou. Během tisku pak můžete pravidelně slyšet sklouznutí vlákna, každých několik sekund jemný zvuk. To je podavač, který se snaží vtlačit vlákno dovnitř, ale vlákno znovu vyklouzne ven.

Většina podavačů bude mít nastavovací body pro úpravu síly, kterou vyvíjí na vlákno. Zkuste podavač nastavit na vlákno trochu pevněji. Pokud podavač tlačí na vlákno příliš tvrdě, může to vlákno zlomit nebo způsobit příliš velké tření a začít ho brousit. Pokud je příliš volný, často uvidíte nějakou podextruzi. 

Nerovnoměrný průměr vlákna
----
Zatímco většina filamentů je v pořádku, někdy se vyrobí šarže, kde je filament příliš tenký. To může mít velké důsledky na množství vytlačování v tisku. Levnější vlákna často vykazují tento problém. Pomocí měřidla můžete změřit skutečný průměr vašeho vlákna. Nezapomeňte měřit na několika různých místech podél délky vlákna a neměřte tam, kde podavač vlákno rozdrtil.

Pokud je průměr vlákna příliš vzdálený (rozdíl 50 μm začíná být na výtisku viditelný), pak můžete upravit průměr vašeho vlákna ve správci materiálu. Pokud používáte vestavěný materiál Cura, budete jej muset před úpravou duplikovat. Cura poté kompenzuje nový průměr úpravou rychlosti podavače.

Tavení materiálu 
----
Kromě skutečnosti, že je vaše 3D tiskárna v perfektním stavu, by parametry, které používáte k tisku, měly odpovídat vlastnostem materiálu, který používáte. Nejdůležitější je teplota tisku.

Pokud je hodnota [teploty tisku](../material/material_print_temperature.md) příliš nízká, rychle si všimnete pod-extruze. Pokud je materiál příliš chladný, bude velmi viskózní, což ztěžuje řádné vytékání z trysky. V kombinaci s vysokou rychlostí tisku nemá materiál čas na to, aby se správně roztavil, ani na to, aby vytékal na místo. Některé materiály, jako je PVA nebo nylon, mají tendenci absorbovat vlhkost ze vzduchu. Tato vlhkost se odpařuje, když je materiál tištěn, to plast ochlazuje. K vyrovnání vlivu vzdušné vlhkosti je nutné použít náhradní materiály.

Získání tekoucího materiálu
----
Vždy existuje prodleva mezi okamžikem, kdy tiskárna posouvá materiál a kdy se skutečně začne extrudovat. Tato latence může vést k pod-extruzi, pokud není brána v úvahu. Když tiskárna tlačí materiál vpřed, tlak v komoře trysky se postupně zvyšuje, dokud to nestačí k vytlačení roztaveného materiálu směrem ven na druhém konci. Může to trvat až sekundu, než materiál dosáhne svého normálního průtoku. Je-li tiskárna vybavena bowdenovou trubicí mezi podavačem a tryskou, může být toto zpoždění ještě mnohem delší, s kulovým parkováním asi 10 sekund.

Když tiskárna potřebuje začít extrudovat více materiálu než dříve, bude materiál rychleji podávat, ale bude trvat nějakou dobu, než se dostane na konec trysky. Během této doby se tryska pokusí nakreslit linii, ale tato linie bude podextrudována. Zejména pokud je tisk velmi podrobný, může to způsobit značnou pod-extruzi.

K nápravě tohoto problému můžete provést dvě úpravy: Základní nastavení a nastavení rychlosti.

Základní nastavení zahrnuje vytlačení malého množství materiálu před začátkem tisku důležité části. Často se to provádí na začátku tisku v samostatné rutině, tiskem malého řádku nebo kapky plastu v rohu tiskové podložky. Můžete také použít [sukénku nebo krempu](../platform_adhesion/adhesion_type.md), které vytisknou několik linií kolem samotného tisku. Když materiál proudí správně a veškerý vzduch vyteče z tryskové komory, bude vytlačování rovnoměrnější.

Když je materiál zatažen, tok materiálu se přeruší. Když je materiál tlačen zpět do trysky, může to nějakou dobu trvat, než obnoví svůj tok. Snížení rychlosti [při které se materiál tlačí zpět](../travel/retraction_prime_speed.md) umožňuje, aby se materiál před vytlačením lépe roztavil, což trochu pomáhá. Pokud tomu tak není, můžete se také pokusit posunout materiál o něco dále než před retrakcí tak, že ho [naplníte trochu více](../travel/retraction_extra_prime_amount.md), abyste kompenzovali pod-extruzi. Úprava je však velmi citlivá.

Vyrovnávání rychlosti 
----
Pokud vidíte pod-extruzi pouze v určitých tiskových strukturách, jako je výplň a podpěra, zkuste dále vyrovnat tok v tisku. Vždy existuje prodleva mezi okamžikem, kdy podavač podává materiál a kdy materiál skutečně vychází z trysky. Pokud se rychlost tisku během části tisku zvýší, tisková hlava zrychluje relativně rychle, ale tok materiálu zůstává pozadu, dokud se tlak v komoře trysky nezvýší, aby se vyrovnal s vyšší rychlostí vytlačování. To také vede k pod-extruzi. Podobně, zpomalením rychlosti vytlačování dochází vždy k nad-extruzi.

Některý firmware je schopen tento efekt kompenzovat. Marlin má funkci nazvanou [Lineární postup](http://marlinfw.org/docs/features/lin_advance.html), která začíná zvyšovat tlak uvnitř tryskové komory předem tak, že může vystoupit z trysky dříve. Sailfish má [podobnou funkci](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html), kterou nazývá JKN Advance. Chcete-li nastavit parametry pro tyto funkce, podívejte se, jaký g-kód byste měli zapsat do počátečního g-kódu.

Pokud tyto funkce nejsou dostupné nebo neúčinné, budete muset zajistit, aby nedošlo k žádným náhlým a významným změnám v toku při tisku. [Tloušťka vrstvy výplně](../infill/infill_sparse_thickness.md) a [Tloušťka vrstvy výplně podpěry](../support/support_infill_sparse_thickness.md). Tyto parametry násobí rychlost vytlačování, aby se získala větší výška vrstvy.

A co je nejdůležitější, musíte se ujistit, že výplň, vnitřní stěny, vnější stěna, plášť a zadní strana jsou tištěny podobnou rychlostí vytlačování. Rychlost vytlačování linie je součinem její šířky, výšky vrstvy, průtoku a (průměrné) rychlosti. Vynásobte spolu tyto čtyři hodnoty a ujistěte se, že výsledek je přibližně stejný pro výplň ([výška vrstvy](../infill/infill_sparse_thickness.md), [šířka linie](../resolution/infill_line_width.md), [tok](../material/infill_material_flow.md) a [rychlost](../speed/speed_infill.md)), pro plášť ([šířka linie](../resolution/skin_line_width.md), [horní/dolní tok](../material/skin_material_flow.md) a [rychlost](../speed/speed_topbottom.md)), pro vnější stěnu ([šířka linie](../resolution/wall_line_width_0.md), [tok vnější stěny](../material/wall_0_material_flow.md) a [rychlost](../speed/speed_wall_0.md)), pro vnitřní stěnu ([šířka linie vnitřní stěny](../resolution/wall_line_width_x.md), [tok](../material/wall_x_material_flow.md) a [rychlost](../speed/speed_wall_x.md)) a pro podpěru ([tloušťka vrstvy výplně podpěry](../support/support_infill_sparse_thickness.md), [šířka linie](../resolution/support_line_width.md), [tok](../material/support_material_flow.md) a [rychlost](../speed/speed_support.md)). Pokud chcete [kompenzovat překrytí stěny](../shell/travel_compensate_overlapping_walls_enabled.md), nezapomeňte povolit [vyrovnání toku vlákna](../speed/speed_equalize_flow_enabled.md) tak, aby byla spíše upravována rychlost než průtok.

Limity trysek
----
Vytlačování příliš velkého množství materiálu pomocí malé trysky může také způsobit podtlak. Při tisku ve vysoké výšce vrstvy, šířce linií nebo rychlosti pomocí malé trysky nebude materiál fyzicky schopen vytékat z trysky včas. Zvýšení teploty může do určité míry přispět k větší tekutosti materiálu, ale vždy existuje určité omezení, co může tryska vytlačovat. Nad tento limit zvažte nákup větší trysky.

Na druhé straně vytlačování příliš malého množství materiálu může také vést k pod-extruzi. Pokud je tlak v komoře trysky velmi nízký, pak povrchové napětí tekutého plastu může udržovat materiál v komoře trysky. Občas vytlačí velkou kapičku a zanechá vzduch na jiných místech. To může mít podobný účinek jako pod-extruze.

Přímé nastavení průtoku
----
Pokud vše ostatní selže, má Cura také nastavení pro přímou úpravu [toku](../material/material_flow.md). Tento způsob nastavení může kompenzovat neznámou chybu někde v systému.

To nebude fungovat, pokud je fyzicky zabráněno rychlému toku materiálu (například z důvodu ucpané trysky). V jiných případech to na některých místech pravděpodobně způsobí nad-extruzi. Toto je však jednoduchý způsob, jak upravit tisk podle potřeby.
