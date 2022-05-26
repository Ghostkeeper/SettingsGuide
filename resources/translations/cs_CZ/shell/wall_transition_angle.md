Prahový úhel přechodu mezi stěnami
====
Tento úhel označuje úhel, při kterém Cura začne vytvářet přechody pro správné vyplnění prostoru. Všechny rohy, které jsou ostřejší než tento úhel, budou vyplněny liniemi proměnné šířky.

![Širší než 10°, již nevytváří přechody](../../../articles/images/wall_transition_angle.png)

Tímto způsobem se pro určité rohy zapíná nebo vypíná proměnná šířka linie. Pokud jsou dvě protilehlé stěny téměř rovnoběžné, menší než úhel zadaný v tomto nastavení, oblast mezi nimi se vyplní liniemi, které mohou mít různou šířku. Pokud jsou od sebe vzdáleny pod větším úhlem, prostor mezi nimi se vyplní stěnami s konstantní šířkou.

Jako vždy se jedná o kompromis. Použití proměnné šířky má některé výhody, např:
* Mezi liniemi nezůstávají žádné mezery.
* Nevyplní stejný prostor vícekrát.
* Rozměry výtisku budou přesnější.

Má to však i některé nevýhody:
* V tenkých dílech se objevují rohy, které se mohou na povrchu jevit jako vlnky.
* Vytváří dodatečné pohyby přesunu.
* Tiskárna nemusí přesně měnit šířku linie v rychlém sledu za sebou.

V praxi je dobré, aby byl tento úhel dostatečně velký, aby se zmenšily mezery v ostrých rozích, jak je vidět v zobrazení vrstvy, ale jinak co nejmenší. Menší úhel obecně způsobuje, že povrch vypadá hladší.

Není možné zmenšit úhel na 0°, abyste se zcela zbavili proměnné šířky linie. Rovnoběžné protilehlé stěny budou mít vždy šířku linie upravenou tak, aby odpovídala prostoru.

**Toto nastavení se nevztahuje pouze na běžné stěny, ale také na dodatečné stěny, podpůrné stěny, výplňové stěny a soustředné vzory.**