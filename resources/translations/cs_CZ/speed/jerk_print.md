Ryv (jerk) tisku
====
Ryv (jerk) určuje rychlost, jakou může tryska procházet rohy. Při vysokých hodnotách ryvu (jerku) se tryska tolik nezpomaluje, když se blíží k rohu, což má za následek konstantní rychlost, ale také větší vibrace.

Termín "Ryv (jerk)" v oblasti 3D tisku byl představen Marlinem, ale **není to totéž jako ryv (jerk) ve fyzice**. Byl navržen jako řešení problému, který se pokouší dokonale sledovat cestu. Protože se tryska nemůže odchýlit od trajektorie (teoreticky), měla by v každém rohu zpomalit na 0 mm/s. To by zničilo váš tisk, protože zpomalení na 0 mm/s by způsobilo kapku v každém rohu. Není dovoleno vytvářet křivky pro zkrácení rohu, ani pro jeho překročení. Místo toho Marlin umožňuje okamžitou změnu vektoru rychlosti v každém rohu. Velikost této změny ve vektoru rychlosti se nazývá "ryv (jerk)". Ryv (jerk) je tedy maximální okamžitá změna rychlosti, aplikovaná na pohyb v každém rohu.

Zvýšené ryvu (jerku) bude mít pozitivní a negativní účinky na váš tisk:
* Doba tisku bude snížena, protože tryska v rozích méně zpomaluje.
* Protože tryska nezpomaluje, bude v rozích méně kapek. Tryska se pohybuje konstantní rychlostí, takže v rozích nezastavuje, zatímco materiál stále protéká otvorem.
* Tiskárna obecně v každém rohu více vibruje, protože tisková hlava je instruována, aby okamžitě změnila směr při teoreticky nekonečném zrychlení. Tyto vibrace mají tendenci vytvářet ve vašem tisku vlnky, což vede ke zvlnění a snížené rozměrové přesnosti.
* Při extrémních hodnotách existuje riziko, že vaše motory ztratí v rozích několik kroků, což může způsobit posun vrstvy.
