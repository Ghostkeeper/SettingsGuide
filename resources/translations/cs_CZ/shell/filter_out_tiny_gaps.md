Filtrovat velmi malé mezery
====
Vyplňování mezer mezi stěnami přináší další přesuny. Pokud jsou mezery extrémně malé, materiál obvykle nebude mít dost času na to, aby z trysky vytékal velmi dobře. Pokud je toto nastavení povoleno, tiskárna se nebude obtěžovat vyplňovat některé z nejmenších mezer.

![Drobné mezery na špičkách zubů jsou vyplněny](../../../articles/images/filter_out_tiny_gaps_disabled.png)
![Drobné mezery jsou filtrovány, takže zůstávají nevyplněné](../../../articles/images/filter_out_tiny_gaps_enabled.png)

Mezery menší než 2-násobek čtverce o straně šířky linie vnější stěny se počítají jako "malé" mezery. Například, pokud vaše nastavení parametru [Šířka linie vnější stěny](../resolution/wall_line_width_0.md) je 0,4 mm, mezery o ploše 0,4 mm * 0,4 mm * 2 = 0,32 mm^2 již nebudou vyplněny.