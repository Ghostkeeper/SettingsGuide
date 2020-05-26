Maximální rozlišení přesunu
====
Pokud má model velmi vysoké rozlišení, Cura sníží rozlišení tak, aby procesor tiskárny byl schopen při zpracování příkazů g-kódu sledovat jejich provádění. Maximální rozlišení přesunu může být určena odděleně od [maximálního rozlišení](meshfix_maximum_resolution.md) při tisku.

Protože se pohyby přesunu provádějí podstatně rychleji než tiskové pohyby, tisková hlava projde segmenty cesty mnohem rychleji než ostatní segmenty linie. CPU by musel tyto segmenty linie zpracovávat mnohem rychleji, aby udržel krok s tryskou. To je důvod, proč by mělo být rozlišení přesunů menší než rozlišení pomalejších extrakčních pohybů.

Rozlišení pohybu během přesunů není často důležité ani pro kvalitu tisku. Protože se nejedná o extruzi, neexistuje žádný povrch, který by se stal rozmazaný nebo hranatý. Z tohoto důvodu nemá snížení rozlišení přesunů žádný významný dopad na kvalitu tisku.

Většina přesunů Cury je přímá. Jedná se o nejrychlejší pohyby a vyvolávají nejmenší vibrace. Pokud se však Cura musí vyhnout kolizím, má sklon sledovat tvar povrchu, kterému se snaží vyhnout. Pohyb po tomto povrchu bude mít podobné rozlišení jako povrch, kterému se vyhýbá. Výsledkem je, že toto nastavení může mít opravdu efekt, pouze pokud je povoleno [objíždění](../travel/retraction_combing.md).
