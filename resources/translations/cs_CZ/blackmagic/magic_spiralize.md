Spiralizovat vnější obrys
====
Spiralizace vnějšího obrysu je trik.

Když tisknete vrstvu po vrstvě, tryska se obvykle musí přesunout z jedné vrstvy na další. Tento pohyb způsobí, že tryska se téměř na zlomek vteřiny zastaví, což zanechává šev na povrchu nazvaný Z-šev. Toto nastavení má tomu a dalším zabránit.

Při spirálování modelu nedostane model žádnou výplň ani vrcholy. Dostane pouze jednu stěnu a dno. Je důležité, pokud je aktivována funkce [Vyhladit spiralizované obrysy](smooth_spiralized_contours.md), výška trysky se bude postupně zvyšovat přes tloušťku vrstvy. Tímto způsobem se vytvoří spirála podle obrysu modelu. Nebude se pohybovat z jedné vrstvy na druhou, protože tryska se již postupně posunula směrem k další vrstvě. 

Spiralizační režim je běžný u mnoha slicerů. Někdy se také nazývá „režim vázy“, protože je to dobrý způsob, jak tisknout vázy. Mezi některé další vlastnosti patří: 
* Tiskne velmi rychle. 
* Povrch je velmi hladký. 
* Nebude moc silný. 
* Je obtížné zajistit, aby byl tisk vodotěsný, pokud má jakoukoli velikost. K tomu je vhodné mít alespoň 2 stěny. 

*Spiralizace nebude dobře fungovat u výtisků s mnoha vodorovnými plochami. Vůbec nezvládá převisy a netiskne horní povrchy, takže se nic nebude moci opírat o vodorovný povrch. Rovněž nefunguje dobře, když je na vrstvě více částí.* 
