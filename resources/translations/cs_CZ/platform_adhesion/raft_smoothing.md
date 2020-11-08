Vyhlazení raftu
====
Díky tomuto nastavení jsou vnitřní úhly raftu plynulejší. Nastavení určuje poloměr oblouku. Všechny vnitřní rohy, které jsou ostřejší než uvedený poloměr oblouku, budou vyhlazeny tak, aby měly poloměr oblouku.

![Žádné vyhlazení](../../../articles/images/raft_smoothing_0mm.png)
![Poloměr 5 mm](../../../articles/images/raft_smoothing_5mm.png)

Technický termín pro toto je [morfologická operace uzavírání](https://en.wikipedia.org/wiki/Closing_(morphology)). Všechny otvory menší než specifikovaný poloměr budou uzavřeny. Nejostřejší vnitřní úhly již nebudou tak ostré.

Funkcí tohoto nastavení je zvýšení tuhosti raftu. Pokud je několik částí spojeno jemnými spoji, může se raft v těchto místech ohnout. Díky tomu jsou méně tuhé a méně odolné vůči deformacím. Zvýšením tohoto nastavení budou jednotlivé kusy lépe spojeny, čímž se raft stane pevnějším. Povrch raftu bude větší, což zvýší adhezi. Kromě toho bude mít raft menší celkový obvod, což zmenší místa, kde může dojít k deformaci. Celkově by mělo být méně deformací.

Celkový objem raftu se však také zvýší. To vyžaduje více materiálu a tisk trvá déle, zejména proto, že se raft normálně tiskne velmi pomalu.