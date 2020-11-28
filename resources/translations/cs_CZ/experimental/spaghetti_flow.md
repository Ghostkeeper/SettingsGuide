Tok špagetové výplně
====
Toto nastavení vám umožňuje přímo upravit hustotu špagetové výplně.

Normálně při tisku výplně nastavení parametru [Hustota výplně](../infill/infill_sparse_density.md) ovlivní pouze hodnotu [Vzdálenost linií výplně](../infill/infill_line_distance.md). Protože [Šířka linie výplně](../resolution/infill_line_width.md) zůstává stejná, ale linie jsou blíže k sobě, zvýšení hustoty výplně má nakonec za následek, že se více objemu výplně vyplní materiálem.

Funguje to jinak, pokud je povolena [Špagetová výplň](spaghetti_infill_enabled.md). Vzdálenost linií výplně umožňuje upravit nejen vzdálenost linií výplně, ale také se upraví šířka linie, aby se dosáhlo požadované hustoty, jak je uvedeno v tomto parametru. Tento parametr přesně určuje zlomek celkového objemu výplně, který bude naplněn materiálem. Pokud tento parametr zvýšíte, linie se rozšíří.

Když se pro vytvoření pružné výplně používají špagety, toto nastavení v podstatě určuje tuhost plnicího materiálu. Snížením toku získáme pružnější výplňový materiál, zatímco zvýšením toku získáme pevnější výplňový materiál. Nadměrné snížení toku však zabraňuje rovnoměrnému rozložení plnicího materiálu. Bude mít sklon padat směrem ke dnu objemu a vytvářet hromady špaget, které nepřispějí k tuhosti vrcholu.

Pokud k nalévání materiálu používáte špagetovou výplň, mělo by být toto nastavení pravděpodobně blízko 100%, aby se model zcela naplnil materiálem. Pokud však má váš materiál při pořizování tendenci se stahovat nebo rozšiřovat, můžete ho mírně upravit.

**Tento parametr je vždy násoben parametrem [Tok pro tisk výplně](../material/infill_material_flow.md).**