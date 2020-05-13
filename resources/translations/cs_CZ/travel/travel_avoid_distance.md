Vzdálenost vyhýbání při přesunu
====
Když je aktivní parametr [Při přesunu se vyhnout tištěným částem](travel_avoid_other_parts.md), definuje tento parametr volný prostor, který tryska udržuje ve vztahu k ostatním objektům, kterým se musí vyhnout.

Nezapomeňte, že tento parametr definuje vzdálenost mezi ostatními objekty a osou pohybu přesunu. Pohyb přesunu nemá žádnou tloušťku. Je vhodné dát tomuto parametru hodnotu, která je dostatečně velká, aby se konec trysky nedotýkal ostatních částí.

Zvýšení hodnoty tohoto nastavení snižuje riziko toho, že se tryska dotkne předmětů, které již byly vytištěny, když je obchází. Zvýšení hodnoty tohoto nastavení však také mírně zvýší délku přesunů, protože tryska musí provádět větší objížďku. To mírně zvyšuje dobu tisku a množství prosakování. Co je možná důležitější, je to, že snižuje šance na nalezení platné cesty, která by se příliš nepřiblížila dříve vytištěným částem. Pokud není nalezena žádná platná cesta, tryska se extrahuje (možná) a místo toho se bude pohybovat v přímé linii, čímž se rezignuje na skutečnost, že se stejně dotkla ostatní části. Příliš velké zvýšení tohoto nastavení může tedy také ovlivnit kvalitu povrchu.
