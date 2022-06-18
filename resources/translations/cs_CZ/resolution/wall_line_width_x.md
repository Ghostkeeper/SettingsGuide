Šířka linie vnitřní stěny
====
Šířka linie vnitřních stěn může být nastavena odděleně od šířky vnější stěny. Toto nastavení označuje šířku linií každé vnitřní stěny.

![Linie vnitřních stěn jsou mnohem širší než ostatní](../../../articles/images/wall_line_width_x.png)

Je známo, že zmenšení vnitřních stěn na šířku linie mírně menší než je velikost trysky, je výhodné pro pevnost. Tryska bude vytlačovat o něco méně materiálu, ale její otvor bude překrývat linie sousedních stěn. Materiál je poté tlačen zpět stěnou dříve umístěnou na správném místě. Ale také umožňuje, aby se plast lépe spojil se sousedními stěnami. To umožňuje, aby se stěny lépe sloučily, takže mohou sloučit svou sílu. To výrazně zlepšuje odolnost stěn.

Zvětšení šířky linie na vnitřní stěně může zkrátit dobu tisku. Budete potřebovat méně vnitřních stěn, abyste získali díly podobné síly. Pevnost však bude poněkud snížena, protože sousední stěny se nebudou spojovat tolik k sobě.

<!--if cura_version>=5.0-->U tenkých dílů se šířka linie automaticky upraví tak, aby odpovídala šířce místního dílu. Není třeba zajišťovat, aby šířka dílu byla násobkem šířky linie. Parametr [Prahový úhel přechodu mezi stěnami](../shell/wall_transition_angle.md) určuje, kde se šířka linie automaticky v ostrých rozích upraví. Parametr [Minimální šířka linie stěny](../shell/min_wall_line_width.md) určuje, jak daleko se mohou v každém směru upravit.<!--endif-->

<!--if cura_version<5.0:
Přizpůsobení linií
----
Při tisku jemných částí je důležitým nástrojem pro získání přesných a pevných součástí úprava šířky linií stěn. Cura nakreslí pouze celé obrysy, takže pokud se obrys nevejde, vloží se stěn mezera, což značně zhorší pevnost a přesnost součásti.

Pokud je aktivována funkce [Vyplnit mezery mezi stěnami](../shell/fill_perimeter_gaps.md), pokusí se Cura tyto mezery mezi stěnami zaplnit, ale tato technika není zdaleka ideální pro libovolné tvary a často zabere hodně času. Když se dvě stěny překrývají, funkce [Kompenzovat překrytí stěn](../shell/travel_compensate_overlapping_walls_enabled.md) zmenší šířku linie stěny, aby byla zajištěna rozměrová přesnost součásti, ale to má za následek změny toku, které také snížit kvalitu a odolnost tisku.

Pro ideální uložení musí být díl přesným násobkem šířky linie stěny tak, aby stěny přesně zapadaly do součásti. Pokud znáte šířku svého součásti, lze to snadno provést úpravou šířky stěn. Nejprve uvidíte, kolik obrysů chcete upravit tak, aby byly linie stále přiměřené šířky. Pak uvidíte, o kolik musíte upravit šířku linií stěny, aby řádky správně zapadly. Mějte na paměti, že můžete upravit [šířku linie vnější stěny](wall_line_width_0.md) a šířku linie vnitřní stěny samostatně. Pečlivě spočítejte, kolikrát bude každý typ stěny nakreslen, aby se mohl předpovědět účinek změny šířky linie stěny.

Přizpůsobení linií stěn je důležitou dovedností pro 3D tisk, který odlišuje odborné operátory 3D tiskáren od ostatních. Je nutná určitá praxe.-->