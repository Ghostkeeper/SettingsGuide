Maximální odchylka plochy extruze
====
Při tisku linií s různou šířkou je běžné, že se linie směrem k jednomu z koncových bodů postupně ztenčuje. Toto nastavení určuje velikost kroku, při kterém se tyto linie ztenčují nebo rozšiřují, tím, že řídí, jak blízko musí linie zůstat k oblasti, kterou by měly v ideálním případě pokrývat.

![Nižší rozlišení při povolení vysoké odchylky](../../../articles/images/meshfix_maximum_extrusion_area_deviation_high.png)
![Hladká šířka linie při požadavku na nízkou odchylku](../../../articles/images/meshfix_maximum_extrusion_area_deviation_low.png)

Příkazy G kódu nemohou tiskárně nařídit, aby vytiskla linii s proměnnou šířkou. Musí tisknout linie s pevnou šířkou. Cura umí linii rozdělit na více segmentů s postupně se měnící šířkou. Tím se však do tisku přidá velké množství segmentů linie. Procesor v tiskárně nemusí při tisku stíhat všechny tyto instrukce. Při tomto nastavení se volí úroveň detailů segmentů linie s proměnlivou šířkou. Větší rozlišení (menší odchylka) teoreticky vede k přesnějším liniím, ale také výrazně zvyšuje množství instrukcí.

V zobrazení vrstvy sice vypadá hezky, když se šířka linie mění postupně, ale na skutečný tisk to nemá prakticky žádný vliv. Fyzické 3D tiskárny neupravují průtok dostatečně přesně na to, aby zde bylo při zvýšení rozlišení vidět nějaké zlepšení. Za normálních okolností by toto nastavení mělo být dostatečně vysoké, aby nikdy nebylo limitujícím faktorem rozlišení g-kódu. Tímto způsobem se minimalizuje možnost, že dojde k nedostatečnému využití vyrovnávací paměti.