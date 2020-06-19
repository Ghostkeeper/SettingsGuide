Relativní extruze
====
Cura zapisuje pokyny pro tiskárnu k tisku vašeho objektu v g-kódu. Tyto pokyny posunou tiskovou hlavu do určitých poloh a zapnou podavač. Cura normálně zaznamenává jak souřadnice pro pohyb tiskové hlavy, tak i rotaci podavače v absolutních souřadnicích. Pokud je však toto nastavení povoleno, budou souřadnice podavače zaznamenány relativně.

Pokud je to zakázáno (tj. absolutní extruze), je pozice vlákna na začátku tisku udržována jako nulová souřadnice. Pozice vlákna se v celém souboru zvětšuje, jak se vytlačuje více materiálu a vlákno se musí pohybovat dále a dále od počátečního bodu na začátku tisku.

Je-li však toto povoleno, bude mít každý samostatný řádek v g-kódu zapsánu extruzi odděleně, vzhledem k pozici v předchozím řádku. Každá řádek pak obsahuje pouze množství materiálu vytlačovaného pro tento konkrétní řádek.

Relativní extruze usnadňuje editaci g-kódu po jeho vygenerování. Pokud je třeba někde mezi nimi extrudovat další materiál (přidat nebo odebrat segmenty linií nebo upravit průtoky), je třeba nový výtisk jednoduše zapsat do editované části. Pokud je použita absolutní extruze, musí být poloha podavače resetována pomocí `G92`, aby se zajistilo, že jsou všechny následující příkazy správné.

Pokud však dojde během zpracování g-kódu k nějakým chybám zaokrouhlování (v Cura, firmwaru nebo pohybu), absolutní extruze se automaticky napraví na dalším řádku. Při relativní extruzi to povede k nadextruzi nebo podextruzi, byť extrémně malé.

Ne všechny firmware tiskáren podporují relativní extruzi.

**Pokud je použita absolutní extruze, Cura stále vynuluje polohu vlákna každých 10 metrů, aby se zabránilo chybám zaokrouhlování s plovoucí desetinnou čárkou ve firmwaru.**


