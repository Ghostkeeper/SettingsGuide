Práh přidání střední linie
====
Při tisku tenkých dílů přizpůsobí Cura šířku linií stěn tak, aby přesně odpovídala šířce modelu. Cura se také může rozhodnout, že místo toho použije menší počet linií stěn. Toto nastavení představuje hranici, při které Cura uprostřed přidá linii. Lze ho nastavit odděleně od [prahu, při kterém se dvě středové linie spojí](wall_split_middle_threshold.md).

Toto nastavení je stejné jako nastavení [Minimální šírky liché stěny](min_odd_wall_line_width.md), ale používá jinou jednotku. Jednotka tohoto nastavení je ve zlomcích šířky linie, o které se musí zvětšit šířka dílu, aby bylo možné doplnit novou střední linii.

![Pokud je středová linie příliš malá, jsou obě linie kolem ní širší](../../../articles/images/min_wall_line_width_0_34.png)
![Snížením tohoto nastavení začíná a končí středová linie mnohem menší](../../../articles/images/min_wall_line_width_odd_0_1.png)

Sudé vs. liché linie
----
Toto nastavení umožňuje upravit práh pro přidávání linií konkrétně v případě, že se jedná o lichý počet linií. To je tehdy, když je uprostřed jedna linie a ne dvě. Určuje, kdy se přidá nová linie mezi dvě středové linie.

Hranice pro přidání středové linie se může lišit od hranice pro rozdělení středové linie na dvě části, a to kvůli způsobu přechodu. Když se přidává lichá linie, začíná se přidávat teprve tehdy, když jí dvě okolní linie uvolní místo. Během přechodu vzniká určitá mezera, kdy okolní linie ještě neudělaly dostatek místa. To se liší od situace, kdy je počet stěn sudý: Linie uprostřed se pak rozdělí na dvě a tyto dvě linie se mírně překrývají, dokud nejsou dostatečně daleko od sebe. Snížením prahové hodnoty přidání prostřední linie se zmenší velikost mezery na přechodech ze sudých do lichých linií. Snížení hodnoty prahu rozdělení středové linie zmenší přesah na přechodech z lichých do sudých linií.

Mezery vzniklé při začátku liché linie jsou v konečném výsledku viditelnější než trocha převýšení ve spoji, takže by mohlo pomoci nastavit prahovou hodnotu přidávání středních linií o něco níže než prahovou hodnotu rozdělení středních linií.

Snížení tohoto nastavení vede k:
* Menších mezerách při ukončení středové linie.
* Menší maximální šířce dvojice sudých středových linií.
* Tenčím liniím, které se nemusí dobře vytlačovat.
* Delším liniím, které se déle tisknou.

**Toto nastavení se netýká pouze běžných stěn, ale také dodatečných stěn, podpůrných stěn, výplňových stěn a soustředných vzorů.**