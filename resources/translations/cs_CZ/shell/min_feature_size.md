Minimální velikost prvku
====
Toto nastavení určuje minimální šířku detailů modelu, které budou vytištěny. Cokoli tenčího než tato hodnota se nevytiskne.

Detaily, které jsou menší než velikost trysky, se pravděpodobně nebudou dobře tisknout. Jedná se o omezení tiskárny. Cura se je však přesto může pokusit vytisknout, ovšem s tím, že nebude mít pěknou rychlost extruze nebo že detaily budou nakonec tlustší, než bylo modelováno.

Zmenšení minimální velikosti prvku způsobí, že tiskárna vytiskne menší detaily tisku. V závislosti na nastavení [Minimální šířky linie tenké stěny](min_bead_width.md) mohou být tyto drobné detaily vytištěny tak, že se vytlačí velmi málo (což způsobí [podextruzi](../troubleshooting/underextrusion.md)), nebo tak, že se vytlačí rozumnější šířka linie, ale vytiskne se nadměrná velikost. Nastavení této hodnoty na 0 způsobí, že tiskárna projde až na samé špičky každého ostrého rohu.

Zvětšení minimální velikosti prvku způsobí, že se tiskárna nebude zabývat malými detaily, které by stejně nevyšly pěkně. Ušetříte tím trochu času a tisk by mohl vyjít čistší.