Úhel převislé stěny
====
Toto nastavení určuje prahový úhel, po kterém bude stěna označena jako "převislá stěna". Tyto převislé stěny lze tisknout různou rychlostí pomocí nastavení [Rychlost tisku převislé stěny](wall_overhang_speed_factor.md).

Pokud je tento parametr nastaven na 0°, bude se všemi stěnami zacházet jako s převislými stěnami. Pokud je tento parametr nastaven na 90°, nebude se žádná stěna považovat za převislou stěna. Stěny, které spočívají na podpěře, se také nepovažují za převislé stěny.

Účelem této funkce je poskytnout lepší převisové vlastnosti pro oblasti, které by bylo téměř třeba podpírat [podpěrou](../support/support_enable.md), ale ne zcela. Místo abyste trávili více času a materiálu na podpěře a zjizvili povrch odstraněním podpěry, můžete se rozhodnout tyto převislé stěny vytisknout trochu pomaleji a nastavit [Úhel převisu pro podpěru](../support/support_angle.md) o něco vyšší. To poskytuje postupnější přístup k lepšímu tisku zvětšujících se úhlů převisu.

Nastavení tohoto parametru nad úhel převisu podpěry výrazně snižuje účinek této funkce, protože stěny nad podpěrou nejsou označeny jako převislé stěny, a proto všechny stěny, které jsou vytištěny pod úhlem převisu, který by byl považován za převislou stěnu, by také byl podepřen a netištěn různými rychlostmi. Tato funkce však stále platí, pokud je podpěra zakázána nebo pro převislé části, které nejsou podpírány z jiných důvodů, například [Minimální podpíraná plocha](../support/minimum_support_area.md).
