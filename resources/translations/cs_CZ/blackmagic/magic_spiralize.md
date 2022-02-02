Spiralizovat vnější obrys
====
Spiralizace vnějšího obrysu je trik.

Když tisknete vrstvu po vrstvě, tryska se obvykle musí přesunout z jedné vrstvy na další. Tento pohyb způsobí, že tryska se téměř na zlomek vteřiny zastaví, což zanechává šev na povrchu nazvaný Z-šev. Toto nastavení má tomu a dalším zabránit. Výrazně zjednodušuje proces tisku vynecháním mnoho jeho aspektů.

Při spirálování modelu nedostane model žádnou výplň ani vrcholy. Dostane pouze jednu stěnu a dno. Rozhodující je, že pokud je povoleno [Vyhladit spiralizované obrysy](smooth_spiralized_contours.md), výška trysky se bude postupně v průběhu vrstvy zvyšovat. Tímto způsobem se vytvoří spirála podle obrysu modelu. Nebude se pohybovat z jedné vrstvy na druhou, protože tryska se již postupně posunula směrem k další vrstvě.

Spiralizační režim je běžný u mnoha slicerů. Někdy se také nazývá "režim vázy", protože je to dobrý způsob, jak tisknout vázy. Mezi některé další vlastnosti patří: 
* Tiskne velmi rychle.
* Povrch je velmi hladký. Pokud je povolen [režim spiralizace](smooth_spiralized_contours.md), nevzniká při přesunu na další vrstvu žádný [Z-šev](../troubleshooting/seam.md).
* Nebude příliš silný. Pokud je model příliš velký, má tendenci se kvůli tenké stěně [rozdělit](../troubleshooting/layer_splitting.md).
* Je obtížné zajistit, aby byl tisk vodotěsný, pokud má jakoukoli velikost. K tomu je vhodné mít alespoň 2 stěny. Spiralizace vnějšího obrysu je tedy nemožná.

**Spiralizace nebude dobře fungovat u výtisků s mnoha vodorovnými plochami. Vůbec nezvládá převisy a netiskne horní povrchy, takže se nic nebude moci opírat o vodorovný povrch. Rovněž nefunguje dobře, když je na vrstvě více částí.**