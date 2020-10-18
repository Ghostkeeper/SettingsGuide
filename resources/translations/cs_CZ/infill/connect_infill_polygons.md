Propojit polygony výplně
====
Když výplň sestává z uzavřených smyček, mohou být tyto uzavřené smyčky sloučeny do jedné smyčky. To umožňuje vytvoření malých spojení tam, kde polygony sousedí.

Tento parametr je k dispozici, pouze pokud je výplň tvořena sousedícími smyčkami. To znamená, že:
* [Vzor výplně](infill_pattern.md) je nastavena na křížový nebo 3D křížový.
* Linie výplně jsou [násobeny](infill_multiplier.md) sudým číslem.
* Kolem výplně jsou nejméně 2 [další stěny](infill_wall_line_count.md).

![U násobených linií výplně je v tomto vzoru výplně mnoho smyček](../../../articles/images/connect_infill_polygons_disabled.png)
![Aktivace tohoto parametru vám umožní smyčky slučovat](../../../articles/images/connect_infill_polygons_enabled.png)

Účelem této funkce je zabránit pohybům přesunu. Konečná linie bude jednoduchá smyčka pro každou připojenou část výplně, takže nedojde k žádnému přesunu. To usnadňuje práci s ohebnými vlákny, protože ty se obtížněji zatahují a pracují lépe, pokud mohou i nadále v trysce cirkulovat.

Spojení těchto smyček může také posílit materiál výplně zlepšením vnitřního spojení mezi smyčkami. Když jsou však polygony spojeny, musí se tisková hlava často těsně před spojem otáčet o 180 stupňů. Tyto zatáčky někdy zabraňují úplnému připojení spoje. V některých případech to může také výplň oslabit. Vše záleží na tom, jak se smyčky protkávají tvarem vašeho modelu.