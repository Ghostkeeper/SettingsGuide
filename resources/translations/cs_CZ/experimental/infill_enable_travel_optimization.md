Optimalizace přesunů při tisku výplně
====
Aktivace tohoto nastavení může mírně zkrátit dobu přesunů ve výtisku. Zkrácením doby přesunů bude tisk o něco rychlejší a také výtok z trysky bude o něco menší. Slicování modelu však bude také trvat déle.

Normálně Cura optimalizuje pořadí, ve kterém jsou linie výplně nakresleny poměrně naivně. Po každém linii vyhledá Cura nejbližší linii pro nakreslení a nakreslí ji. U některých neobvyklých a složitých tvarů však může být cesta k další linii výplně poměrně dlouhá, protože tryska musí provádět objíždění kvůli [režimu objíždění](../travel/retraction_combing.md). V zásadě pak Cura podceňuje vzdálenost a může si vybrat spíše delší cestu než kratší cestu. Když je tento parametr aktivován, vzdálenost se vypočte přesně, aby bylo možné provést lepší výběr.

Toto nastavení bude mít obecně malý dopad na čas slicování. U složitých výtisků s mnoha malými částmi (kde je to nejužitečnější) však může zvýšit dobu slicování o hodnotu řádu.