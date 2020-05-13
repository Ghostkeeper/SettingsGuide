Šířka linie vnější stěny
====
Šířku linie vnější stěny lze nastavit odděleně od šířky vnitřních stěn. Toto nastavení označuje šířku linie vnější stěny.

![Obrys vnější stěny je mnohem širší než zbytek](../../../articles/images/wall_line_width_0.png)

Je známo, že zmenšení vnější stěny na šířku linie o něco menší, než je velikost trysky, je výhodné pro pevnost. Tryska bude vytlačovat o něco méně materiálu, ale její otvor bude překrývat sousední vnitřní stěnu. Materiál je poté tlačen zpět stěnou dříve umístěnou na správném místě. Umožní to ale také, aby se plast lépe spojil se sousedními stěnami. Vnější stěna se tak lépe spojuje s vnitřními stěnami, takže tyto stěny mohou sloučit své síly. To výrazně zlepšuje odolnost stěn.

Zmenšení šířky linie na vnější stěně také umožňuje, aby tryska tiskla jemnější detaily, protože tenčí linie se lépe přizpůsobí malým detailům.

Zvětšení šířky linie vnější stěny může zkrátit dobu tisku. Můžete získat stěnu podobné tloušťky s menším počtem vnitřních stěn. Pevnost však bude poněkud snížena, protože vnější stěna se nebude slučovat s vnitřními stěnami.

Přizpůsobení linií
----
Při tisku jemných částí je důležitým nástrojem pro získání přesných a pevných dílů úprava šířky linií stěn. Cura nakreslí pouze celé obrysy, takže pokud se obrys nevejde, vloží se do stěn mezera, což značně zhorší pevnost a přesnost součásti.

Pokud je aktivována funkce [Vyplnit mezery mezi stěnami](../shell/fill_perimeter_gaps.md), pokusí se Cura tyto mezery mezi stěnami zaplnit, ale tato technika není zdaleka ideální pro libovolné tvary a často zabere hodně času tisku. Když se dvě stěny překrývají, funkce [Kompenzovat překrytí stěn](../shell/travel_compensate_overlapping_walls_enabled.md) zmenší šířku linie stěny, aby byla zajištěna rozměrová přesnost součásti, ale to má za následek změny toku, které také snížit kvalitu a odolnost tisku.

Pro ideální uložení musí být díl přesným násobkem šířky linie stěny tak, aby stěny do součásti přesně zapadaly. Pokud znáte šířku svého dílu, lze to snadno provést úpravou šířky stěn. Nejprve uvidíte, kolik obrysů chcete upravit tak, aby byly linie stále přiměřené šířky. Pak uvidíte, o kolik musíte upravit šířku linií stěny, aby linie správně zapadly. Mějte na paměti, že můžete upravit šířku linie vnější stěny a [šířku linie vnitřní stěny](wall_line_width_x.md) samostatně. Pečlivě spočítejte, kolikrát bude nakreslen každý typ stěny, aby bylo možné předpovědět účinek změny šířky linie stěny.

Přizpůsobení linií stěn je důležitou dovedností pro 3D tisk, který odlišuje odborné operátory 3D tiskáren od ostatních. Je nutná určitá praxe.
