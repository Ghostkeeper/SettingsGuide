Špagetová výplň
====
Pokud je toto nastavení povoleno, Cura vytlačí veškerou výplň z více vrstev najednou do horní vrstvy. Jedná se o extrémní formu parametru [Tloušťka vrstvy výplně](../infill/infill_sparse_thickness.md), ale bez cíle udržet tuhost výplně. Má určité funkce, aby se vypořádal s extrémním množstvím vytlačování.

Tato vlastnost není pro běžné materiály funkční. Normálně budete chtít buď sílu běžných vzorů výplně, nebo výplň ignorovat. Existují však dva případy použití.

Případy použití
----
Díky flexibilním materiálům může tato technika vytvářet velmi jemné textury. Špagetová výplň má tendenci vytvářet volně umístěné prsteny, které se k sobě navzájem nelepí. Tyto prsteny jsou rovnoměrně rozmačkané ve všech směrech. K dosažení tohoto efektu však nemůže být hustota výplně příliš nízká nebo všechny špagety skončí na spodní straně tisku. Je vhodné použít [hustotu toku](spaghetti_flow.md) mezi 30% a 60%, v závislosti na šířce a výšce vrstvy. Výsledkem bude výplň, která je stejně tuhá ve všech směrech a poměrně měkká.

Další aplikací pro špagetovou výplň je lití. Pokud máte tiskárnu, která obsahuje nástroj pro odlévání na konkrétních místech, lze tuto funkci použít k vyplnění modelu téměř rovnoměrně pomocí řízeného ukládání materiálu. Pokud se použije, [hustota toku](spaghetti_flow.md) pravděpodobně musí být přibližně 100%, v závislosti na poměru smrštění/roztažení litého materiálu.

Nastavení dalších parametrů pro špagetovou výplň
----
Obě tyto aplikace vyžadují velmi speciální zacházení s vaší výplní. Toto je několik nastavení, která budete pravděpodobně chtít upravit podle svých potřeb:
* [Rychlost výplně](../speed/speed_infill.md) musí být masivně snížena. Pokud má tryska vytlačovat materiál výplně současně pro 10 vrstev, budete muset snížit rychlost tisku alespoň o faktor 8.
* Parametr [Tloušťka vrstvy výplně](../infill/infill_sparse_thickness.md) nastavte tak, aby se rovnala výšce vrstvy.
* Mírně zvyšte svou hodnotu [teploty tisku](../material/material_print_temperature.md) (pro extrudér, který bude tisknout výplň). To umožňuje materiálu, aby správně z trysky vytékal, a umožňuje rychlejší vytlačování.
* Nastavte [Zarovnání švu v Z](../shell/z_seam_type.md) na náhodné, aby se struktura náhodně rozšířila.

**V pohledu vrstev v aplikaci Cura se výplň objeví jako velmi silné linie. Je to proto, že Cura předpokládá, že materiál zůstává na stejné vrstvě a šíří se tam. Ve skutečnosti ten bude klesat.

**Při použití špagetové výplně nemá parametr [Šířka linie výplně](../resolution/infill_line_width.md) žádný efekt. Šířka linie je upravena tak, aby vyhovovala potřebám parametrů [Vzdálenost linií výplně](../infill/infill_line_distance.md) a [hustotě toku](spaghetti_flow.md).**


