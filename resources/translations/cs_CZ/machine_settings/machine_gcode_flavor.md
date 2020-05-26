Varianta g-kódu
====
Zatímco g-kód je standardizovaný formát pro komunikaci instrukcí na CNC strojích, jako jsou 3D tiskárny, stále existují určité rozdíly v tom, které g-kódy jsou příslušnou tiskárnou podporovány, jaký je jejich počáteční stav a někdy v tom, jak příkazy interpretují. S variantou g-kódu můžete do značné míry určit, jakou sadu příkazů vaše tiskárna přijímá.

Rozdíl mezi těmito variantami g-kódu je obecně poměrně malý. Nejdůležitější příkazy, jako je pohyb a zahřívání trysky, jsou obecně stejné.

Správnou variantu g-kódu vyberte v dokumentaci k firmwaru tiskárny. Měl by vám sdělit, které funkce jsou podporovány a které nikoli. Toto jsou dostupné varianty v aplikaci Cura a jejich rozdíly.

Marlin
----
Marlin je považován za výchozí variantu g-kódu. Je určen pro hlavní [Marlin firmware](https://marlinfw.org/), které je nejoblíbenějším firmwarem pro 3D tisk a základem většiny alternativních firmwarů.

Marlin (objemový)
----
Toto je varianta Marlina, kde příkazy extruze specifikují, hodnoty v krychlových milimetrech a ne v délkách vlákna. Toto jsou významné změny:
* Parametr „E“ příkazu „G1“ je počítán v milimetrech krychlových, objemu přiváděného plastu, místo délky vlákna, které má být během tohoto pohybu přiváděno.
* Statistiky na začátku g-kódu také uvádějí použité vlákno v krychlových milimetrech.

RepRap
----
Toto je varianta zaměřená na podporu tiskáren, které se vyvinuly z projektu [RepRap](https://reprap.org/wiki/RepRap). Má řadu pozoruhodných výjimek:
* Při nastavování počáteční teploty vrstvy vždy uvádí extrudér, i když existuje pouze jeden extrudér.
* Po tisku se vratí k relativnímu vytlačování.
* Mění zrychlení pomocí parametrů `P` a` T` příkazu `M204`, a to pro zrychlení tisku a zrychlení přesunu, místo parametru` S`.
* Mění ryv (jerk) pomocí příkazu `M566`, místo příkazu `M205`.

Ultimaker 2
----
Tato varianta g-kódu je určena pro rodinu Ultimaker 2. Firmware této rodiny měl zvláštní myšlenku, že by měl nechat tiskárnu, aby ovládala nastavení související s materiálem, místo sliceru. Jedná se o výjimky:
* V g-kódu nebudou žádné příkazy teploty tisku.
* V g-kódu nebudou žádné příkazy teploty podložky tisku.
* V g-kódu nebudou žádné příkazy pro nastavení teploty objemu tisku.
* Předpokládá se, že první tryska má při zahájení tisku [teplotu tisku počáteční vrstvy](../material/material_print_temperature_layer_0.md).
* Při spuštění tisku se předpokládá, že teplota tiskové podložky má hodnotu [teploty pro tisk počáteční vrstvy](../material/material_bed_temperature_layer_0.md).
* Parametr `E` příkazu` G1` je počítán v krychlových milimetrech, což je objem přiváděného plastu, místo délky vlákna, která se má během tohoto pohybu posunout.
* Statistiky na začátku g-kódu uvádějí použité vlákno v krychlových milimetrech.

Griffin
----
Toto je varianta g-kódu pro moderní tiskárny Ultimaker, Ultimaker 3 a novější. Tyto tiskárny vyžadují spoustu metadat v určitém formátu na začátku g-kódu. Rozdíly v této variantě g-kódu jsou:
* Na začátku g-kódu je velké záhlaví obsahující informace o metadatech, jako je délka tisku, název tiskové úlohy a některé praktické informace, jako je počáteční teplota a ohraničující rámeček tisku.
* V g-kódu nebudou žádné příkazy pro sestavení teploty objemu tisku.
* U první trysky se předpokládá, že při zahájení tisku bude mít [teplotu tisku počáteční vrstvy](../material/material_print_temperature_layer_0.md).
* Při spuštění tisku se předpokládá, že teplota tiskové podložky má hodnotu [teploty pro tisk počáteční vrstvy](../material/material_bed_temperature_layer_0.md).
* Předpokládá se, že tiskárna nespustí první extrudér, takže se vždy přepne na počáteční extruder na začátku tisku pomocí příkazu `T`.
* Při prvním zahájení tisku je pro každý extrudér vytištěna hlavní kapka příkazem `G280` namísto retrakce.

Makerbot
----
Jedná se o variantu g-kódu určenou pro firmware založeném na [Sailfish](https://www.sailfishfirmware.com/). Tento firmware se používá u potomků původních tiskáren Makerbot. Některé významné rozdíly jsou:
*Při změně teploty tisku není podporován příkaz `M109` (nastavená teplota a čekání). Místo toho vydá příkaz `M104`, který nečeká na dosažení teploty. Poté pomocí příkazu `M116` vydá tiskárně příkaz k vyčkávání, dokud se nedosáhne této teploty.
* Rozměr `E` příkazu extruze `G1` se během tisku neobnoví. Pro jiné varianty se tento parametr obnoví po každých 10 metrech vlákna pomocí příkazu `G92 E0`, aby se zabránilo chybám zaokrouhlování s plovoucí desetinnou čárkou ve firmwaru.
* Přepínání extruderů se děje příkazem `M135` a ne příkazy `T`.
* Na výstupu není rychlost ventilátoru. Ventilátor je buď zapnutý nebo vypnutý. Cura nařídí tiskárně zapnout ventilátor, pokud by to jinak vyžadovalo rychlost ventilátoru 50% nebo více.

Bits from Bytes
----
Jedná se o variantu g-kódu zaměřenou na tiskárny Bits from Bytes, které měly svůj vlastní firmware. Jejich varianta g-kódu se výrazně liší od ostatních. Toto jsou změny, které Cura provede:
* Velikost extruze se zapisuje pomocí otáček podavače a ne pomocí parametru `E`.
* V závislosti na aktivním extrudéru jsou retrakce zapsány kódy „M101“ nebo „M201“.
* Rychlost retrakce jeza psána samostatným příkazem `M108`.
* Pohyby přesunu jsou označeny příkazem `M103`, místo přepínání `G1` pro `G0`. Nebudou zde žádné příkazy `G0`.
* Tiskárna je nastavena na použití automatické retrakce pomocí příkazu `M227`.
* Cura vydává nové řádky ve stylu Windows s návratem vozíku místo jen symbolu nové řádky.
* Rozměr `E` příkazu extruze `G1` se během tisku neobnoví. Pro jiné varianty se tento parametr obnoví po každých 10 metrech vlákna pomocí příkazu `G92 E0`, aby se zabránilo chybám zaokrouhlování s plovoucí desetinnou čárkou ve firmwaru.

Mach3
----
Jedná se o variantu g-kódu, která zůstává blíže tomu, jaký očekávají CNC frézky. Existuje pouze jeden pozoruhodný rozdíl:
* Hodnoty extruze se zapisují pomocí parametru `A` příkazu` G1`, a ne pomocí parametru `E`.

Repetier
----
Jedná se o variantu g-kódu zaměřenou na 3D tiskárny od společnosti Repetier. Napodobuje výstup sliceru Repetier. Toto jsou výrazné rozdíly této varianty g-kódu:
* Je-li povolena firmwarová retrakce, používá retrakce pro přepnutí extrudéru `G10 S1` k označení, že se jedná o retrakci pro přepnutí extrudéru .
* Změny zrychlení se provádějí pomocí příkazů `M201` a` M202` (pro zrychlení tisku a zrychlení přesunu) namísto `M204`.
* Změny ryvu (jerku) se provádějí pomocí příkazu `M207` a ne pomocí příkazu 'M205`.

*Protože se jedná o nastavení stroje, nebude obvykle uvedeno v normálním seznamu nastavení. Pro toto nastavení existuje menu výběru, v dialogu nastavení tiskárny, který se nachází v seznamu přidaných tiskáren v dialogu předvoleb..*