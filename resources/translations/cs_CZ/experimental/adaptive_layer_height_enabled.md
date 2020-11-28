Použít adaptivní vrstvy
====
Adaptivní vrstvy lokálně upraví tloušťku vašeho tisku, aby optimalizovaly čas a kvalitu tisku na základě povrchových vlastností modelu. Vrstvy budou ztenčeny tam, kde jsou mělké svahy nebo zesíleny tam, kde jsou stěny strmé. Účelem je rychlý tisk tam, kde je to možné, ale v případě potřeby stále tisknout podrobně.

![U barevného schématu "tloušťky vrstvy" můžete vidět, že barva tenčí vrstvy je modrá a tlustší vrstvy žlutá](../../../articles/images/adaptive_layer_height_enabled.png)

Výška vrstev je upravena tak, aby horizontální vzdálenost mezi okraji vrstev zůstala konstantní. Mělké povrchy způsobují velké horizontální posuny s malým vertikálním posunem, takže malé vertikální posunutí je provedeno pro udržení horizontálního posunu konstantním. U strmých povrchů existuje malé horizontální posunutí s velkým vertikálním posunem, takže se provádí velké vertikální posunutí, aby se horizontální posunutí udržovalo konstantní. Proto je topografický účinek vrstev udržován konstantní. Maximální vzdálenost mezi dvěma sousedními vrstvami je udržována na konstantní vzdálenosti podle nastavení parametru [Velikost topografie adaptivních vrstev](adaptive_layer_height_threshold.md).

Pokud má model mělké i strmé povrchy ve stejné výšce, považuje se tloušťka vrstvy za nejmenší z tlouštěk vrstvy. To někdy způsobuje, že výška vrstvy je zbytečně malá, protože vedle ní je vodorovná plocha. Můžete to vidět na obrázku výše, stejně jako v polovině výšky sila na levé straně.

Použití adaptivních vrstev je velmi omezené, aby se zlepšila kvalita tisku. Výška vrstvy se nesmí lišit o více než je zadáno parametrem [Maximální variace adaptivních vrstev](adaptive_layer_height_variation.md) uvedená ve vztahu k původnímu parametru [Výška vrstvy](../resolution/layer_height.md). Mezi dvěma sousedními vrstvami nemůže rozdíl ve výšce vrstvy překročit určitou [Velikost kroku variace adaptivní vrstvy](adaptive_layer_height_variation_step.md). Tloušťka vrstvy tak prochází postupně z jedné vrstvy na druhou místo toho, aby ji náhle rozřezala na polovinu.

Adaptivní vrstvy mohou výrazně zkrátit dobu tisku, aniž by došlo ke ztrátě kvality tisku nebo v některých případech dokonce dochází ke zlepšení kvality. Účinek úpravy tloušťky vrstvy je obrovský. Ve většině případů se doba tisku výrazně sníží díky použití silnějších vrstev, když je model svislý. Efekt topografie je také snížen, protože vrstvy jsou horizontálně rozmístěny blíže k sobě.

Tato funkce však může také přinést i řadu problémů.
* Změnou výšky vrstev je obecně nutné upravit další parametry, jako je například teplota trysky. Adaptivní vrstvy tyto další parametry automaticky neupravují. To může způsobit, že tisk nebude optimální např. převisy, které by lépe fungovaly při nižší tiskové teplotě.
* Pokud se výška vrstvy změní po celé vrstvě pro malý prvek umístěný někde v malé části vrstvy, bude ve zbývající vrstvě viditelný pruh.
* S tím jsou také neúmyslně upraveny vertikální vzdálenosti. To může mít negativní vliv na kvalitu tisku. Například [Tloušťka horní/dolní strany](../shell/top_bottom_thickness.md) bude obecně tenčí, protože Cura ponechá parametr [Horní vrstvy](../shell/top_layers.md) jako true a vrstvy budou tenčí. To může způsobit polštářový efekt. Mezi ovlivněná nastavení, která již nemusí být správná, patří:
* [Horní tloušťka](../shell/top_thickness.md)
* [Dolní tloušťka](../shell/bottom_thickness.md)
* [Maximální úhel pláště pro rozšíření](../infill/max_skin_angle_for_expansion.md)
* [Výška kroku postupné výplně](../infill/gradual_infill_step_height.md)
* [Výška kroku postupné výplně podpěry](../support/gradual_support_infill_step_height.md)
* [Tloušťka vrstvy výplně](../infill/infill_sparse_thickness.md)
* [Tloušťka vrstvy výplně podpěry](../support/support_infill_sparse_thickness.md)
* [Vzdálenost Z od podpěr](../support/support_z_distance.md)
* [Tloušťka střechy podpěry](../support/support_roof_height.md)
* [Tloušťka podlahy podpěry](../support/support_bottom_height.md)
* [Úhel převisu pro podpěru](../support/support_angle.md)
* [Výška kroku schodů podpěry](../support/support_bottom_stair_step_height.md)
* [Úhel střechy podpůrné věže](../support/support_tower_roof_angle.md)
* [Úhel ochranného štítu proti výtoku](../dual/ooze_shield_angle.md)
* [Maximální úhel modelu](../experimental/conical_overhang_angle.md)