Relativní šev v Z
====
Když je šev umístěn na místě určeném uživatelem podle nastavení parametru [Zarovnání švu v Z](z_seam_type.md), můžete zadat souřadnice pozice, kde má být šev umístěn. Tyto souřadnice obvykle označují umístění na tiskové podložce, například na zadní straně tiskárny. Pokud je tento parametr aktivován, budou tyto souřadnice vzaty relativně vzhledem k poloze modelu.

![Vypnuto: Souřadnice označují absolutní polohu ve středu montážní desky, takže všechny bílé pruhy směřují ke středu](../../../articles/images/z_seam_relative_disabled.png)
![Zapnuto: Souřadnice jsou relativní k modelu, takže každý model bude mít bílé pruhy ve stejném rohu](../../../articles/images/z_seam_relative_enabled.png)

Je-li na tiskové podložce duplikován model, toto nastavení způsobí, že šev bude umístěn na přesně stejném místě pro každý duplikát, než aby je směřoval na stejný bod na tiskové podložce. To vám umožní vytisknout každou kopii přesně stejným způsobem, bez ohledu na její polohu na tiskové podložce.