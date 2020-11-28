Tok pro střechu podpěry
====
Toto nastavení upravuje průtok pouze pro střechu podpěry. Tok pro střechu podpěry může být nastaven odděleně od průtoku pro zbytek podpěry.

Úprava toku během tisku střechy podpěry je metoda zastavení prostoru pro vyřešení problémů s rychlostí vytlačování nebo přilnavostí mezi modelem a podpěrou. Stejného účinku lze dosáhnout úpravou [šířky linií](../resolution/support_roof_line_width.md) nebo [vzdálenosti linií](../support/support_roof_line_distance.md) střechy podpěry, ale nastavení toku může být intuitivnější.

Pokud existuje problém s rychlostí vytlačování, je nejlepší prozkoumat [rychlost tisku](../speed/speed_support_roof.md), [teplotu](material_print_temperature.md) a [šířku linií](../resolution/support_roof_line_width.md). Mezi tokem pro střechu podpěry a ostatními strukturami vrstvy může být příliš velký rozdíl. Možná je šířka linie příliš tenká, aby mohla být řádně vytlačena. Pokud je rozhraní vytištěno pomocí [jiného materiálu](../support/support_interface_extruder_nr.md), je běžným problémem to, že materiál, pomocí kterého je rozhraní vytištěno, nemá dostatek času na to, aby začal řádně vytékat. Tento problém lze vyřešit pomocí [aktivační věže](../dual/prime_tower_enable.md) nebo zvětšením [střechy podpěry](../support/support_roof_offset.md).

Pokud podpěra přilne příliš dobře k modelu, bude nastavení [šířky linií](../resolution/support_roof_line_width.md) obecně efektivnější, protože také umožňuje přiblížení linií za účelem získání stejné hustoty výplně podpěry.