Průměr trysky
====
Toto nastavení měří průměr otvoru trysky, kterým protéká materiál.

![Rozměry tiskové hlavy](../images/head_dimensions_cs.svg)

Toto je důležitý rozměr, na kterém mohou ostatní nastavení založit své výchozí hodnoty. Nejdůležitější je, že [šířka linie](../resolution/line_width.md) je normálně nastavena na základě velikosti trysky. Některé profily tiskáren omezují výšku vrstvy také na základě velikosti trysky, protože velikost trysky je nejdůležitějším faktorem v tom, jak rychle lze materiál vytlačovat.

<!--if cura_version < 5.0:Velikost trysek se také používá přímo, pro jeden detail: Když se [vyplňují mezery mezi stěnami](../shell/fill_perimeter_gaps.md), nespojí se linie dále než dvě velikosti trysek od sebe navzájem.-->

Velikost trysky neupravujte, dokud skutečně neupravujete fyzickou trysku. Některé slicery (včetně Cury 15.04 a dřívějších) používají termín "velikost trysek", což znamená, jak široké linie tisku by měly být. Cura k tomu používá nastavení [šířky linie](../resolution/line_width.md).

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné. Pokud má vaše tiskárna specifické profily pro dostupné trysky, můžete si je vybrat z nabídky nastavení tiskárny v horní horní části obrazovky. V opačném případě můžete upravit průměr trysek v dialogu nastavení tiskárny, který najdete v seznamu přidaných tiskáren v dialogu předvoleb.**