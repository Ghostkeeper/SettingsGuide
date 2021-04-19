Šířka linie horního povrchu pláště
====
Pomocí parametru [Vrstvy horního povrchu pláště](../top_bottom/roofing_layer_count.md), může být několika vrstvám umístěným na samém vrcholu přiřazena jiná šířka linií, než je tomu u hlubších horních vrstev.

Plášť na horní straně tisku plní několik funkcí. Zejména musí uzavřít otvory, zanechané výplní na horní straně a poskytnout dílu velkou pevnost. Kromě toho by bylo ideální, kdyby vypadala hezky a hladce. Zmenšení parametru [Šířka linie horní/dolní strany](../resolution/skin_line_width.md) lze použít k vytvoření hladšího povrchu, ale tisk bude trvat mnohem déle. Toto nastavení vytváří hladký horní povrch s velmi jemnými liniemi, aniž by bylo nutné tisknout zbytek horní a dolní části se stejnými šířkami linií. Doba tisku je tak méně penalizována.

Zmenšením šířky linií pláště horní plochy získáte hladší povrch na horní straně tisku. Tisk však bude o něco delší.

Nadměrné zmenšení šířky linií může vést k přerušení toku, pokud je menší než minimální průtoková rychlost trysky. Materiál poté vytvoří korálky, když opouští trysku, a horní povrch je pak poďobaný a pod-extrudován.

Tato technika je podobná technice [žehlení](../top_bottom/ironing_enabled.md). Avšak se žehlením se provede další průchod na stejné vrstvě s velmi jemnými liniemi a s vytlačováním pouze nepatrných množství. Při tomto nastavení budou jemné linie nakresleny ve své vlastní vrstvě místo na horním plášti. Žehlení způsobuje nad-extruzi (záměrně). Toto nastavení to neudělá.