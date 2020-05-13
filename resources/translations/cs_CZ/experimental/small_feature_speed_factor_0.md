Rychlost tisku počáteční vrstvy malého prvku
====
Obrysy, které jsou kratší než [maximální délka malých prvků](small_feature_max_length.md), lze tisknout sníženou rychlostí. Tento parametr umožňuje určit rychlost, jakou by se měly tyto obrysy tisknout na počáteční vrstvě, jako faktor jejich [normální tiskové rychlosti](../speed/speed_wall.md). Tuto rychlost lze nakonfigurovat odděleně od [rychlosti tisku malých prvků](small_feature_speed_factor.md) na na ostatních vrstvách.

Malé obrysy nemají příliš velkou plochu, aby se přilepily na podložku tisku. Zejména při [tisku stěn před výplní](../infill/infill_before_walls.md) jsou stěny malých prvků často jen malé kruhy umístěné na tiskové podložce. Pokud do nich tryska při dalším pohybu narazí, mohou být z podložky tisku odtrženy. Z tohoto důvodu může být rychlost tisku těchto malých obrysů ve srovnání s ostatními obrysy snížena. To umožňuje, aby materiál tekl více a lépe se sloučil s tiskovou podložkou, což snižuje pravděpodobnost, že bude z montážní desky odtržena.

Snížení rychlosti tisku u těchto malých obrysů má velmi malý negativní dopad na rychlost tisku. Naštěstí, protože tyto obrysy jsou podle definice malé a ovlivňují pouze první vrstvu, celková přidaná doba tisku není významná.
