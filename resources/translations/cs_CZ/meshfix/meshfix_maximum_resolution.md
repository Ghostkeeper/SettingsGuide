Maximální rozlišení
====
I když se vysoké rozlišení může zpočátku zdát lepší, často se stává, že tiskárna nezpracovává G kód s vysokým rozlišením velmi dobře. To je důvod, proč Cura sníží rozlišení svého vstupu během procesu slicování. Toto nastavení určuje rozlišení, které bude Cura udržovat na maximu.

![Před snížením rozlišení](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Po snížení rozlišení (do extrému)](../../../articles/images/meshfix_maximum_resolution_1.png)

Tiskárna musí zpracovat g-kód během jeho provádění. Pokud g-kód obsahuje mnoho malých úseček, může tisková hlava procházet pohybem tak rychle, že procesor 3D tiskárny není schopen držet krok. To má za následek, že tisková hlava se sporadicky zpomalí, aby CPU mohl dohnat nebo jednoduše čekat na další příkaz pohybu. To způsobuje, že povrch je velmi drsný nebo dokonce vykazuje malé kapky, protože průtok z trysky neodpovídá dokonale sporadickému pohybu trysky. Nižší rozlišení někdy vede k lepší kvalitě tisku.

Toto nastavení označuje minimální délku pro segmenty linií. Segmenty linií, které jsou kratší než specifikovaná délka, budou brány v úvahu pro spojení s jinými segmenty linií. Poté se spojí, pokud se nová cesta neodchýlí od své původní cesty o více než [maximální odchylku](meshfix_maximum_deviation.md).

Všimněte si, že neexistuje žádná záruka, že z každé vrstvy budou odstraněny stejné vrcholy, pokud budou vrcholy zarovnány. Redukce rozlišení se provádí ve 2D odstraněním vrcholů tvarů vrstvy a ne ve 3D odstraněním vrcholů sítě. Proto příliš velké snížení rozlišení často povede k nepravidelnému povrchu, a ne k úhlovému povrchu.

Doporučuje se snížit rozlišení modelu tak, aby se tisková hlava významně nezpomalila, aby se procesor nechal dohnat. Pokud není rozlišení dostatečně sníženo, povrch se zdrsní snížením rychlosti tiskové hlavy, zatímco vytlačování pokračuje. Pokud se rozlišení příliš sníží, povrch se také zdrsní stěnami, které se všude přesně nepokládají.

