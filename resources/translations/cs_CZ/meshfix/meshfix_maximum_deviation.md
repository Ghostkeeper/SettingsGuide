Maximální odchylka
====
I když se vysoká přesnost může zpočátku zdát lepší, často se stává, že tiskárna nezpracovává G-kód získaný s vysokou přesností velmi dobře. To je důvod, proč Cura sníží rozlišení během procesu slicování. Toto nastavení určuje, jak daleko se může redukovaná cesta lišit od původní cesty, aby se snížilo rozlišení.

![Před snížením rozlišení](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Po snížení rozlišení (do extrému)](../../../articles/images/meshfix_maximum_resolution_1.png)

Tiskárna musí zpracovat g-kód během jeho provádění. Pokud g-kód obsahuje mnoho malých úseček, může tisková hlava procházet pohybem tak rychle, že procesor 3D tiskárny není schopen držet krok. To má za následek, že tisková hlava se sporadicky zpomalí, aby CPU mohl dohnat nebo jednoduše čekat na další příkaz pohybu. To způsobuje, že povrch je velmi drsný nebo dokonce vykazuje malé kapky, protože průtok z trysky neodpovídá dokonale sporadickému pohybu trysky. Nižší rozlišení někdy vede k lepší kvalitě tisku.

Toto nastavení udává, jak daleko se nová dráha se sníženým rozlišením smí odchýlit od původní dráhy s vysokým rozlišením. Linie jsou považovány za spojené s ostatními segmenty linií, pokud jsou kratší než [maximální rozlišení](meshfix_maximum_resolution.md), ale pokud by tato zkratka způsobila, že se dráha bude lišit o více, než je vzdálenost uvedená v tomto nastavení, nebudou linie spojeny.

Všimněte si, že neexistuje žádná záruka, že z každé vrstvy budou odstraněny stejné vrcholy, pokud budou vrcholy zarovnány. Redukce rozlišení se provádí ve 2D odstraněním vrcholů tvarů vrstvy a ne ve 3D odstraněním vrcholů sítě. Proto příliš velké snížení rozlišení často povede k nepravidelnému povrchu, a ne k úhlovému povrchu.

Z důvodu strukturální integrity se důrazně nedoporučuje, aby se trajektorie odchýlila o více než polovinu šířky linie. Má-li však být povrch hladký nebo vypadat dobře, toto nastavení v podstatě označuje hloubku nerovností povrchu. Maximální odchylka musí být velmi malá, aby nebyla pouhým okem viditelná.

Příliš velké snížení maximální odchylky však značně omezuje snížení rozlišení. Výsledný g-kód se nemusí vytisknout správně, protože centrální jednotka není schopna zachytit příkazy pro krátký pohyb.
