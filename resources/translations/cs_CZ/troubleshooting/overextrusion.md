Nad-extruze
====
Nad-extruze je termín používaný, když tiskárna vytlačuje příliš mnoho materiálu na jednom místě. Materiál potom teče do strany nebo nahoru, čímž je povrch velmi drsný a nepravidelný. Může také způsobit [strunování](stringing.md) a mnoho [kapek](blobs.md).

![V tomto tisku došlo k masivní nad-extruzi](../../../articles/images/overextrusion.jpg)

Ovládání teploty
----
Nejčastější příčinou nadměrného vytlačování je příliš horký tisk. Pokud je [Teplota tisku](../material/material_print_temperature.md) nastavena příliš vysoko, bude mít materiál nižší viskozitu, což způsobí, že vyjde z trysky bez kontroly. To obecně vede k nad-extruzi v určitých oblastech, jako jsou vnější stěny, ale k pod-extruzi v jiných, jako je výplň.

Chcete-li to napravit, musíte postupně snižovat teplotu. Pečlivě si prohlédněte technický list materiálu, s nímž tisknete, abyste zjistili, jaký je přijatelný rozsah a snižte svůj tisk směrem k dolní části tohoto rozsahu.

Průměr vlákna
----
Pro průměr vláken existuje několik norem. Nejběžnější jsou 1,75 mm a 2,85 mm, ale stále jsou možné i 3,00 mm. Kromě toho ne všichni výrobci vyrábějí svá vlákna s konstantním průměrem. Pokud je vaše vlákno širší, než to, co Cura očekává, vytlačíte příliš mnoho materiálu, protože Cura dá tiskárně pokyn k vytlačení určité délky vlákna, které bude mít příliš velký objem.

K vyřešení tohoto problému nejprve změřte skutečný průměr vlákna pomocí posuvného měřítka. Nejlepší je změřit ho na několika místech, v případě, že se liší, a pod různými úhly po obvodu. Vezměte průměr těchto měření. Tento průměr lze zadat v aplikaci Cura na stránce Správa materiálu jako vlastnost materiálu. Pokud průměr nelze změnit, protože se jedná o vestavěný materiál, možná budete muset materiál nejprve duplikovat. To by vám pak mělo umožnit průměr upravit.

Kalibrace extrudéru
----
Někdy je problém v tom, že hardware nesplňuje očekávání firmwaru. Pokud je vytlačovací motor krokový motor (který je běžný ve 3D tiskárnách), musí firmware vědět, kolik kroků motoru způsobí posunutí určité vzdálenosti. Firmware má k tomu parametr, který měří přesnost posuvu v krocích na milimetr. Pokud je tento parametr nesprávně nakonfigurován, může se podavač pohybovat příliš rychle nebo příliš pomalu. Pokud je to možné, je nejlepší upravit toto nastavení ve firmwaru. Pokud to však není možné, může být v aplikaci Cura upraven [tok](../material/material_flow.md) tak, aby to kompenzoval. Musíte také kompenzovat všechny [vzdálenosti retrakce](../travel/retraction_amount.md) a [rychlosti](../travel/retraction_speed.md).  

<!--if cura_version<5.0:
Překrývající se stěny
----
Cura normálně jen kreslí obrysy tisku s určitou šířkou linie. Pokud se stěny přiblíží k určitým místům ve stopě, způsobí to překrývání linií. Tyto linie zesílí a vytvoří skvrny, protože může existovat až dvakrát tolik materiálu, kolik je třeba. Když dojde k velkému překrytí, druhá linie se nemůže protlačit a tlak uvnitř tryskové komory se zvyšuje, dokud není vytlačen a nevytvoří kuličku.

Tomu lze zabránit aktivací [kompenzace překrývajících se stěn](../shell/travel_compensate_overlapping_walls_enabled.md). Vytlačování druhé linie bude sníženo tak, že vytlačuje tolik materiálu, kolik je nutné k vyplnění zbývajícího prostoru stěny, což zabraňuje nadměrnému vytlačování.

Pokud se stěny překrývají kvůli [vnoření vnější stěny](../shell/wall_0_inset.md), můžete zkusit toto vnoření omezit, abyste se vyhnuli přílišnému vytlačování. Můžete také zkusit vytisknout [vnější stěnu před vnitřní](../shell/outer_inset_first.md). Přebytečný materiál bude poté zatlačen do interiéru modelu, kde je neviditelný.-->

Přímé nastavení průtoku
----
Pokud nevíte, co způsobuje toto nadměrné vytlačování, můžete také přímo upravit [průtok](../material/material_flow.md). Snižte průtok, dokud se váš povrch znovu neobjeví. To může přímo kompenzovat nějaký neznámý faktor.