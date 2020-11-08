Drátový tisk
====
Toto nastavení umožňuje zcela odlišný režim tisku zvaný Drátový tisk. Při použití drátového tisku tiskárna nevytváří pevný objekt, ale pouze trojúhelníkovou mřížku vnějšího tvaru z jemných vláken.

Tato technika má řadu výhod:
* Tiskne mnohem rychleji než pevný objekt. 
* Používá pouze zlomek materiálu, který by použil normální tisk. 
* Vypadá zvláštně, jako by byl ručně konstruován pomocí 3D tiskového pera. 

Výsledný objekt však není funkční. Bude to zhruba správná velikost, díky čemuž je pro vytváření prototypu užitečné měřítko tisku užitečné, i když velikost není příliš přesná. Získaný objekt je mimořádně křehký nejen během tisku, ale i později. Je obtížné ji vyjmout z montážní desky, aniž by došlo k jejímu poškození. Model také ztratí většinu svých detailů.

Drátový tisk sestává z nanášení prstenců materiálu s poměrně velkým svislým odstupem několika milimetrů. Mezi těmito kroužky nakreslí tvar pily, který umožňuje, aby další prsten spočíval na předchozím. Když je povrch modelu vodorovný, podobná technika se používá k uzavření vrcholu. Ve střeše jsou soustředné kruhy držené pohromadě tvarem pily, pečlivě zavěšené ve vzduchu zvnějšku (kde může spočívat na stěně) dovnitř.

Drátový tisk funguje spolehlivě pouze s téměř zcela svislými tvary, jako je typ modelu, který by dobře fungoval v režimu [Spiralizování vnějšího obrysu](../blackmagic/magic_spiralize.md). Pokud je povrch vodorovný na velkých plochách, musí technika zavírání střechy překonat extrémně velkou vzdálenost. V tomto případě je velmi pravděpodobné, že technika selže. Pokud bude model dále stoupat do poloviny nad vodorovnou plochu, bude téměř jistě vytištěn ve vzduchu.

**Pohled na vrstvy v aplikaci Cura po slicování, nebude správně drátový tisk zobrazovat. Výsledek však můžete zobrazit i nadále uložením g-kódu na disk a opětovným otevřením g-kódu pomocí Cury.**