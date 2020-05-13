Tok pro vnější stěnu
====
Toto nastavení upravuje průtok pouze pro vnější stěnu. Průtok vnější stěny lze nastavit odděleně od průtoku vnitřní stěny.

Úprava toku vnější stěny je způsob zastavení prostoru, aby se vyřešily problémy s rychlostí vytlačování nebo rozměrovou přesností. Stejného účinku lze dosáhnout také úpravou parametrů [Šířka linie vnější stěny](../resolution/wall_line_width_0.md) a [Vnořit vnější stěnu](../shell/wall_0_inset.md), ale toto nastavení by mohlo být intuitivnějším způsobem, jak provést počáteční nastavení.

Pokud je problém s rychlostí vytlačování pouze na vnější stěně, je nejlepší zkontrolovat nastavení [rychlost tisku](../speed/speed_wall_0.md) a [teplotu tisku](material_print_temperature.md). Možná materiál nedostává dostatečnou hybnost z trysky a vyšší rychlost tisku může pomoci. Možná jsou linie příliš tenké, aby mohly být řádně vytlačeny. Možná je materiál příliš chladný nebo příliš horký.

Pokud se vyskytne problém s rozměrovou přesností, je nejlepší se podívat se [šířku linií](../resolution/wall_line_width_0.md), [horizontální rozšíření](../shell/xy_offset.md) a [pořadí tisku](../shell/outer_inset_first.md).
