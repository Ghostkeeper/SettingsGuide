Strategie drátového tisku
====
Nejdůležitější starostí o spolehlivost drátového tisku se týká spojovacích bodů, kde se vrstvy útku vzájemně spojují. Existuje několik strategií pro posílení těchto spojení. Toto nastavení umožňuje zvolit strategii, kterou bude tiskárna používat. Nejkritičtějším problémem spolehlivosti drátěného tisku jsou spojovací body, ve kterých se spojují vrstvy rámu. Pro posílení těchto spojení je k dispozici několik strategií. Toto nastavení umožňuje zvolit strategii, kterou bude tiskárna používat.

Kompenzace
----
Při použití této strategie se tiskárna pokusí kompenzovat faktory prohýbání materiálu. Jak vychází roztavený materiál z trysky, trochu před ztuhnutím spadne a bude pohyby trysky strháván. Tato strategie deformuje pilový vzor, který spojuje vrstvy rámu tak, aby nakonec skončil na správném místě.

K dispozici jsou dva kompenzační faktory: jeden deformuje pilový vzor pouze vertikálně, aby [kompenzoval prohýbání](wireframe_fall_down.md), a druhý, který deformuje pilový vzor v diagonálním směru, aby [kompenzoval materiál stržený tryskou](wireframe_drag_along.md).

Uzel
----
Pokud je zvolena tato strategie, bude v horní části každého pilového zubu proveden malý pohyb shora dolů a zdola nahoru, aby se vytvořil "uzel" materiálu. Účelem tohoto uzlu je poskytnout vodorovnému kroužku, který má být připevněn k pilovému vzoru, určitý povrch. Uzel se ze strany na stranu mírně mění, takže pokud není horizontální kroužek umístěn přesně, existuje větší šance, že se k sobě připojí. Uzel také způsobí, že horní linie se bude rozprostírat o něco více nahoru, což způsobí, že horizontální kroužek bude na něj přitlačen. Nakonec uzel také způsobí určitý výtok kvůli absenci retrakce v tomto pohybu přesunu. Tím se vytvoří kapka, na které může horizontální kroužek lépe spočívat.

![Kde je uzel nakreslen a jaká je jeho velikost](../images/wireframe_top_jump_cs.svg)

Pohyb pro tento "uzel" je řada přesunů:
1. Nejprve se tryska posune směrem nahoru, jak ukazuje toto nastavení. Současně se tryska pohybuje o polovinu zpět.
2. Pokud je v horní části [pauza](wireframe_top_delay.md), tryska se zastaví po dobu nastavené pauzy. Toto přerušení se koná ve špičce pohybu uzlu.
3. Tryska klesá do obvyklé výšky. Současně se tryska posune o jedenapůlnásobek velikosti uzlu, aby se ocitla ve vzdálenosti uvedené v tomto nastavení vzhledem ke svislé linii.

Retrakce
----
Když je zvolena tato strategie, bude materiál stažen po každém pohybu nahoru během tisku vzoru pily. Myšlenka je, že stažením materiálu je drát přerušen. To snižuje tažný účinek materiálu během pohybu trysky, protože předchozí linie již není k hubici připojena. Poté tryska provede malý skok 1 milimetr a pokračuje ve svém diagonálním pohybu směrem k dolní vrstvě.

Jednou z hlavních nevýhod této strategie je to, že diagonální sestupná linie již není dále připevněna k trysce. Díky tomu je vytlačování během této linie zbytečné. Materiál jednoduše končí jako kulička na spodní vrstvě. Materiál je také podroben většímu obrušování, protože materiál je zatahován tam a zpět bez větší extruze mezi nimi. To vše zabere také hodně času.